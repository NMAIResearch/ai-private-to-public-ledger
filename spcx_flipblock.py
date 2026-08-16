#!/usr/bin/env python3
"""
spcx_flipblock.py — the "flipblock air-pocket" test, the honest (free-data) version.

Hypothesis under test (NOT asserted): SPCX day-1..15 pricing is supported by
engineered supply control (retail anti-flip + underwriter stabilization). If so,
liquidity-adjusted price impact should SHIFT measurably when each support expires.

Method: rolling Amihud illiquidity = |daily return| / dollar volume  (x1e9 for
readability) from free DAILY data — no L2/order-book feeds needed. With n=1 stock
and no counterfactual, a spike at a boundary is EVIDENCE CONSISTENT WITH the
hypothesis, never proof. Boundaries are marked, reader concludes.

Event boundaries (from the S-1 / Fidelity terms — keep distinct):
  2026-06-12  IPO / first trade ($135 offer)
  2026-06-27  retail anti-flip FREE (sell-flagging window = 15 calendar days -> free day 16+)
  ~2026-07-12 underwriter stabilization/greenshoe window ends (~30 days, APPROXIMATE)
  TBD         staged insider lock-up tranches (20% after Q2 earnings; +10% if >=30% above
              IPO 5-of-10 days; 7% tranches at 70/90/105/120/135d; 28% after Q3 earnings)

Data entry (daily, ~1 min): append a row to spcx_daily.csv after each close.
  Free sources: Stooq CSV  https://stooq.com/q/d/l/?s=spcx.us&i=d   (or run with --fetch)
  Optional short_volume column: FINRA daily short sale files (cdn.finra.org, CNMSshvol).

Pure Python 3 stdlib. Run:  python3 spcx_flipblock.py   (in your terminal)
"""
import csv, os, sys, urllib.request
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "spcx_daily.csv")
STOOQ_URL = "https://stooq.com/q/d/l/?s=spcx.us&i=d"
ROLL = 5  # rolling window (trading days) for the Amihud median

EVENTS = {
    date(2026, 6, 12): "IPO day ($135 offer)",
    date(2026, 6, 27): "retail anti-flip FREE (day 16+)",
    date(2026, 7, 12): "~stabilization/greenshoe end (approx)",
}


def fetch_stooq():
    print(f"Fetching {STOOQ_URL} ...")
    with urllib.request.urlopen(STOOQ_URL, timeout=30) as r:
        text = r.read().decode()
    if "Date" not in text.splitlines()[0]:
        sys.exit("Stooq returned no data (ticker may not be live yet). Enter rows manually.")
    rows = list(csv.DictReader(text.splitlines()))
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "open", "high", "low", "close", "volume", "short_volume", "notes"])
        for r_ in rows:
            w.writerow([r_["Date"], r_["Open"], r_["High"], r_["Low"],
                        r_["Close"], r_["Volume"], "", ""])
    print(f"Wrote {len(rows)} rows -> {CSV_PATH}")


def num(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def main():
    if "--fetch" in sys.argv:
        fetch_stooq()

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if num(r.get("close")) and num(r.get("volume"))]
    if len(rows) < 2:
        print("Need >=2 filled rows in spcx_daily.csv for returns. "
              "Day-1 capture: just fill the 2026-06-12 row after Thursday's close.")
        return

    print(f"\nSPCX FLIPBLOCK LEDGER  ({len(rows)} sessions)\n" + "=" * 78)
    print(f"{'date':12s}{'close':>9s}{'ret%':>8s}{'$vol(B)':>10s}{'amihud':>9s}"
          f"{'roll5':>9s}{'srt%':>7s}  event")
    print("-" * 78)

    amihuds = []
    prev_close = None
    for r in rows:
        d = date.fromisoformat(r["date"])
        close, vol = num(r["close"]), num(r["volume"])
        dollar_vol = close * vol
        ret = (close / prev_close - 1) if prev_close else None
        ami = abs(ret) / dollar_vol * 1e9 if ret is not None and dollar_vol else None
        if ami is not None:
            amihuds.append(ami)
        window = sorted(amihuds[-ROLL:])
        roll = window[len(window) // 2] if window else None
        sv, tv = num(r.get("short_volume")), vol
        srt = f"{sv / tv * 100:5.1f}" if sv and tv else "    -"
        ev = EVENTS.get(d, "")
        print(f"{r['date']:12s}{close:9.2f}"
              f"{(f'{ret * 100:7.2f}' if ret is not None else '      -'):>8s}"
              f"{dollar_vol / 1e9:10.2f}"
              f"{(f'{ami:8.4f}' if ami is not None else '       -'):>9s}"
              f"{(f'{roll:8.4f}' if roll is not None else '       -'):>9s}"
              f"{srt:>7s}  {ev}")
        prev_close = close

    print("-" * 78)
    print("Read: amihud = |ret|/$vol x1e9 (higher = less liquid). The test is the LEVEL\n"
          "SHIFT of roll5 across each marked boundary — not any single day's spike.\n"
          "n=1, no counterfactual: consistent-with, never proof.")


if __name__ == "__main__":
    main()
