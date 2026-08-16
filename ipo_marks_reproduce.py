#!/usr/bin/env python3
"""
ipo_marks_reproduce.py — the marks-vs-reality ledger, computed.

Reads ipo_marks_data.csv and prints:
  1. PUBLIC VERDICT     — for companies that went public, the step-up from the
                          last private mark to the IPO/public valuation. Did the
                          real price confirm, exceed, or reject the private mark?
  2. MARK TRAJECTORY    — each company's marks over time (the living ledger).
  3. STILL PRIVATE      — companies with only private marks = no public price
                          test yet (fund N-PORT marks are the only outside read).
  4. PENDING CAPTURE    — rows to fill as live events land (e.g. SpaceX 11-12 Jun).

Pure Python 3 stdlib. Edit the CSV, re-run, the ledger moves.
This scores how private valuations survive contact with a real price.
It is NOT a forecast or a market call.
"""
import csv, os
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "ipo_marks_data.csv")


def num(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def public_verdict(rows):
    print("1. PUBLIC VERDICT  (last private mark -> IPO/public valuation, $bn)")
    by_ent = defaultdict(list)
    for r in rows:
        by_ent[r["entity"]].append(r)
    for ent, rs in by_ent.items():
        privs = [r for r in rs if r["mark_type"] in
                 ("secondary_private", "private_round", "merger_mark")
                 and num(r["implied_val_usd_bn"])]
        priv = max(privs, key=lambda x: x["date"] or "") if privs else None
        pub = next((r for r in rs if r["mark_type"] == "IPO_price"), None)
        if not priv or not pub:
            continue
        pv, uv = num(priv["implied_val_usd_bn"]), num(pub["implied_val_usd_bn"])
        if pv and uv:
            mark = "" if pub["verified"].strip() == "yes" else f"  [{pub['verified']}]"
            print(f"   {ent:11s}: ${pv:g}B (private) -> ${uv:g}B (IPO)  "
                  f"= {uv/pv:.1f}x step-up{mark}")
    print()


def trajectory(rows):
    print("2. MARK TRAJECTORY  (each company's marks over time)")
    by_ent = defaultdict(list)
    for r in rows:
        by_ent[r["entity"]].append(r)
    for ent, rs in by_ent.items():
        print(f"   {ent}:")
        for r in sorted(rs, key=lambda x: x["date"] or "9999"):
            val = f"${num(r['implied_val_usd_bn']):g}B" if num(r["implied_val_usd_bn"]) else "  -  "
            pps = f"@ ${num(r['price_per_share']):g}/sh" if num(r["price_per_share"]) else ""
            flag = "" if r["verified"].strip() == "yes" else f" «{r['verified']}»"
            print(f"      {r['date'] or 'TBD':10s} {r['mark_type']:18s} {val:8s} {pps}{flag}")
    print()


def still_private(rows):
    print("3. STILL PRIVATE  (no public price test — fund N-PORT marks only)")
    ents = sorted({r["entity"] for r in rows})
    for ent in ents:
        rs = [r for r in rows if r["entity"] == ent]
        has_public = any(r["mark_type"] in ("IPO_price", "public_close", "public_peak")
                         and r["verified"].strip() == "yes" for r in rs)
        if not has_public:
            privs = [r for r in rs if num(r["implied_val_usd_bn"]) and r["mark_type"]
                     in ("secondary_private", "private_round", "merger_mark")]
            priv = max(privs, key=lambda x: x["date"] or "") if privs else None
            v = f"${num(priv['implied_val_usd_bn']):g}B" if priv else "?"
            print(f"   {ent:11s}: {v} private — never price-tested (smoothed/lagged fund marks)")
    print()


def pending(rows):
    print("4. PENDING CAPTURE  (fill as live events land)")
    any_p = False
    for r in rows:
        if r["verified"].strip().lower() == "pending":
            any_p = True
            print(f"   {r['entity']:11s} {r['mark_type']:16s} ({r['date'] or 'TBD'}) — {r['notes']}")
    if not any_p:
        print("   (none)")
    print()


def graded(rows):
    """Checkpoints that have RESOLVED. The ledger's whole claim is that calls get
    graded, so a resolved checkpoint has to be visible without reading the CSV."""
    print("5. GRADED CHECKPOINTS  (resolved, scored against the filing)")
    any_g = False
    for r in rows:
        if r["mark_type"].startswith("lockup_") and r["verified"].strip() == "yes":
            any_g = True
            pps = f" @ ${num(r['price_per_share']):g}/sh" if num(r["price_per_share"]) else ""
            print(f"   {r['date']:10s} {r['mark_type']}{pps}")
            print(f"      {r['notes'][:300]}")
    if not any_g:
        print("   (none yet)")
    print()


def main():
    rows = load(CSV_PATH)
    print(f"\nTHE AI PRIVATE-TO-PUBLIC LEDGER  ({len(rows)} marks)\n" + "=" * 60)
    public_verdict(rows)
    trajectory(rows)
    still_private(rows)
    pending(rows)
    graded(rows)
    print("Reminder: scores how private marks survive a real price. NOT a forecast.\n"
          "SpaceX CAPTURED (priced 11 Jun $1.77T; day-1 close 12 Jun $160.95/+19.2%/~$2.11T).\n"
          "s5.3 RESPECIFIED (v2): v1 promised grading 'at the lock-up date' and there is no such\n"
          "date. The 424B4 sets a staged release, so the prediction is now dated checkpoints.\n"
          "FIRST CHECKPOINT GRADED: clause (b) FAILED, 0 of 5 closes at or above $175.50.\n"
          "Next: 8 Dec 2026 (up to 797.6M shares, higher BECAUSE clause (b) failed), then 12 Jun 2027.\n"
          "NOTE: SK Hynix carries no private mark (already KOSPI-listed), so it is absent from the\n"
          "public verdict by design. It scores issue pricing, not a private mark meeting a price.")


if __name__ == "__main__":
    main()
