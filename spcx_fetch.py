#!/usr/bin/env python3
"""Re-pull the SPCX daily close series and short interest, and re-grade 424B4 clause (b).

WHY THIS EXISTS
---------------
From the IPO to 2026-08-15, spcx_daily.csv held one row (12 June) and the project had no working
price source: stooq is proof-of-work walled, Yahoo rate-limits. Everything downstream of it — the
clause (b) grade, the lock-up rewrite, the positioning column — was blocked on a manual pull. This
does the pull in one command so the grade is reproducible rather than a one-off.

SOURCE, AND ITS TIER
--------------------
api.nasdaq.com, the JSON endpoint behind nasdaq.com's own pages. Nasdaq is the LISTING EXCHANGE and
the short-interest table is the FINRA bi-monthly report, so this is exchange-operator data, not
press. It is still an UNDOCUMENTED endpoint: no terms, no stability guarantee, can change or block.
Better than the press tier this project was running on; not a filing. Check the closes against a
second source before minting a grade on them.

    python3 spcx_fetch.py            # re-grade from the CSVs already on disk
    python3 spcx_fetch.py --pull     # re-fetch from Nasdaq, rewrite both CSVs, then grade
"""
import argparse
import csv
import datetime as dt
import json
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DAILY = HERE / "spcx_daily.csv"
SHORTS = HERE / "spcx_short_interest.csv"
API = "https://api.nasdaq.com/api/quote/SPCX"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126 Safari/537.36",
      "Accept": "application/json"}

OFFER = 135.0
# Filing-derived, and it must NOT be re-derived from a press "float" figure. 424B4 cover
# (acc. 0001628280-26-042639): 555,555,555 base + 83,333,333 over-allotment. The 10-Q filed
# 2026-08-04 (acc. 0001628280-26-052535) confirms the option was exercised in full, 638.9M
# sold. Every short-interest settlement to date predates the 6 Aug 2026 unlock, so this is
# the correct denominator throughout; a settlement dated after 6 Aug needs the then-current
# float instead and the pct column must be left blank rather than computed against this.
IPO_FLOAT = 555_555_555 + 83_333_333
UNLOCK_DATE = "2026-08-06"
THRESHOLD = 175.50  # clause (b): 30% above the offer price
# The 424B4 sets the window as the ten consecutive trading days ending on and including the First
# Earnings Release Date. That date is not filing-confirmed in this project (HANDOVER §7b), so all
# three candidates are graded. They agree, which is why the grade holds without it.
CANDIDATE_ENDS = ("2026-08-04", "2026-08-05", "2026-08-06")


def money(s):
    return float(s.replace("$", "").replace(",", ""))


def get(path):
    with urllib.request.urlopen(urllib.request.Request(f"{API}/{path}", headers=UA), timeout=30) as r:
        return json.loads(r.read().decode())


def pull():
    today = dt.date.today().isoformat()
    hist = get(f"historical?assetclass=stocks&fromdate=2026-06-01&todate={today}&limit=400")
    bars = sorted(({"date": dt.datetime.strptime(r["date"], "%m/%d/%Y").date().isoformat(),
                    "open": money(r["open"]), "high": money(r["high"]), "low": money(r["low"]),
                    "close": money(r["close"]), "volume": int(r["volume"].replace(",", ""))}
                   for r in hist["data"]["tradesTable"]["rows"]), key=lambda b: b["date"])

    keep = {r["date"]: r["notes"] for r in csv.DictReader(DAILY.open())} if DAILY.exists() else {}
    with DAILY.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "open", "high", "low", "close", "volume", "short_volume", "notes"])
        for b in bars:
            note = keep.get(b["date"]) or f"Nasdaq historical endpoint, pulled {today}. Regular-session bar."
            w.writerow([b["date"], f"{b['open']:.2f}", f"{b['high']:.2f}", f"{b['low']:.2f}",
                        f"{b['close']:.2f}", b["volume"], "", note])

    si = get("short-interest?assetclass=stocks")["data"]["shortInterestTable"]["rows"]
    rows = sorted(({"settlement_date": dt.datetime.strptime(r["settlementDate"], "%m/%d/%Y").date().isoformat(),
                    "short_interest_shares": int(r["interest"].replace(",", "")),
                    "avg_daily_volume": int(r["avgDailyShareVolume"].replace(",", "")),
                    "days_to_cover": round(float(r["daysToCover"]), 4)}
                   for r in si), key=lambda r: r["settlement_date"])
    for r in rows:
        pre = r["settlement_date"] < UNLOCK_DATE
        r["float_shares"] = IPO_FLOAT if pre else ""
        r["pct_of_float"] = (f"{r['short_interest_shares'] / IPO_FLOAT * 100:.1f}" if pre else "")
        r["note"] = (f"Nasdaq/FINRA bi-monthly short-interest report, pulled {today}. "
                     + (f"Float = the {IPO_FLOAT:,} Class A shares sold in the IPO (424B4 cover "
                        "acc. 0001628280-26-042639 + 10-Q acc. 0001628280-26-052535, "
                        "over-allotment exercised in full). This settlement PREDATES the 6 Aug "
                        "2026 unlock, so the IPO float is the correct denominator. Upper bound: "
                        "it assumes nothing else became freely tradable first."
                        if pre else
                        "pct_of_float LEFT BLANK: this settlement POSTDATES the 6 Aug 2026 "
                        "unlock, so the IPO float is the wrong denominator. Compute the "
                        "then-current float from spcx_lockup_schedule.csv before filling it, "
                        "and do not carry the 32.5% figure forward."))
    with SHORTS.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
        # Provenance travels with the data. A reader who opens this file alone should be
        # able to see where the denominator came from without opening the paper.
        fh.write(
            "# DENOMINATOR, and it is the number the positioning argument turns on.\n"
            "# float_shares = 555,555,555 base offering + 83,333,333 over-allotment\n"
            "#              = 638,888,888 Class A shares.\n"
            "# Source: SEC Form 424B4, Space Exploration Technologies Corp, filed 12 Jun 2026,\n"
            "#   accession 0001628280-26-042639 (cover: offering size and option), and Form 10-Q\n"
            "#   filed 4 Aug 2026, accession 0001628280-26-052535, which states 638.9 million\n"
            "#   shares sold 'including the full exercise of the underwriters' over-allotment\n"
            "#   option' for net proceeds of $85,675M after $575M of costs. 638,888,888 x $135\n"
            "#   = $86.25bn gross, which ties to that disclosure.\n"
            "# Shares outstanding at 28 Jul 2026 (10-Q cover): 7,696,293,669 Class A plus\n"
            "#   5,485,486,276 Class B = 13,181,779,945.\n"
            "# UPPER BOUND: assumes no other Class A became freely tradable before 6 Aug 2026.\n"
            "#   The 424B4 release schedule supports that; it does not prove it.\n"
            "# Short interest itself is the Nasdaq/FINRA bi-monthly report, a settlement-date\n"
            "#   snapshot and not a continuous series.\n"
            "# 6 AUG 2026 UNLOCK: up to 911.5M shares released, more than doubling the float.\n"
            "#   Any settlement dated after it needs the then-current float, not this one.\n"
            "#   spcx_fetch.py leaves pct_of_float blank for those rows rather than guessing.\n")
    print(f"pulled {len(bars)} sessions and {len(rows)} short-interest settlements\n")


def grade():
    bars = [{"date": r["date"], "close": float(r["close"]), "low": float(r["low"]),
             "high": float(r["high"])} for r in csv.DictReader(DAILY.open())]
    print(f"series {bars[0]['date']} .. {bars[-1]['date']}  ({len(bars)} sessions)")
    print(f"last close ${bars[-1]['close']:.2f} ({(bars[-1]['close'] / OFFER - 1) * 100:+.1f}% vs "
          f"${OFFER:.0f} offer); series intraday low ${min(b['low'] for b in bars):.2f}; "
          f"high ${max(b['high'] for b in bars):.2f}")
    over = [b["date"] for b in bars if b["close"] >= THRESHOLD]
    print(f"closes >= ${THRESHOLD}: {', '.join(over) if over else 'NONE'} "
          f"(last: {over[-1] if over else 'n/a'})\n")

    for end in CANDIDATE_ENDS:
        idx = next((i for i, b in enumerate(bars) if b["date"] == end), None)
        if idx is None:
            print(f"window ending {end}: no session")
            continue
        win = bars[max(0, idx - 9): idx + 1]
        hits = sum(b["close"] >= THRESHOLD for b in win)
        best = max(b["close"] for b in win)
        print(f"clause (b), window {win[0]['date']}..{win[-1]['date']}: {hits}/5 closes >= "
              f"${THRESHOLD} -> {'TRIGGERS' if hits >= 5 else 'FAILS'} "
              f"(best close ${best:.2f}, short by ${THRESHOLD - best:.2f})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pull", action="store_true", help="re-fetch from Nasdaq before grading")
    if ap.parse_args().pull:
        pull()
    grade()
