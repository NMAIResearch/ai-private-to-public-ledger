# The AI Private-to-Public Ledger, reproduction bundle (v2)

**A pre-registered benchmark for venture marks and liquidity realisation: scoring private AI valuations against primary SEC filings, IPO pricing, and post-listing lock-up mechanics.**

Published as *The AI Private-Valuation Marks-vs-Reality Ledger* through v1.1.1 and retitled at v2. The concept DOI is unchanged.

NM AI Research · ORCID 0009-0003-4213-7769 · CC BY 4.0 · concept DOI 10.5281/zenodo.20672581

*AI disclosure: the research is the author's; this text was drafted with AI assistance and reviewed by the author. The model, and the conflicts it creates, are named in the Conflict of interest and scope section.*

The paper is `ipo_marks_ledger_v2.md`. This file is the bundle's front door: what is in it, how to re-run it, and what not to conclude from it.

## Headline

The first SpaceX lock-up checkpoint has resolved and it failed. Clause (b) of the prospectus lock-up required a close at or above **$175.50**, being 30% above the $135 offer, on five of the ten trading days ending on the first earnings release date. **None of the ten qualifying closes reached it.** The best was $125.33, about 29% short, and the result is identical at every candidate window end, so the grade does not turn on a contested date. The level was written by the underwriters, in a binding term, as one they expected the stock to clear inside two months of listing.

Two things follow that matter more than the grade.

**v1 specified the prediction defectively.** It promised grading "at the lock-up date" and the governing prospectus sets no such date, but a staged release running to mid-2027. That is a defect in specification, not a wrong figure, and v2 says so and restates the prediction as dated checkpoints.

**The ledger's own lock-up model predicted the wrong sign.** On 6 August up to 911.5 million shares were released, more than doubling the float, and the stock rose 6.14%. Short interest stood at 32.5% of the 638,888,888-share float, so the marginal buyer was a covering short rather than a passive allocator absorbing supply. Short interest as a share of float is now part of the method. A single observation is not enough to calibrate where positioning stops dominating and supply starts, and v2 declines to fit a threshold to it.

## Contents

| File | What it is |
|---|---|
| `ipo_marks_ledger_v2.md` | the paper |
| `ipo_marks_data.csv` | the marks, 31 rows, one per observation, with a `verified` column carrying `yes`, `pending` or `superseded` |
| `ipo_marks_reproduce.py` | regenerates the ledger tables, including the graded checkpoints, from the CSV |
| `spcx_fetch.py` | re-pulls the price series and short interest, and re-grades clause (b) |
| `spcx_daily.csv` | SPCX daily bars, 12 Jun to 14 Aug 2026 |
| `spcx_daily_secondsource.csv` | the same series from an independent provider, for cross-checking |
| `spcx_short_interest.csv` | bi-monthly settlement short interest, with the filing-derived float and its derivation |
| `spcx_lockup_schedule.csv` | the release ladder exactly as filed, including the 2027 extended and founder dates |
| `skhy_daily.csv` | SK Hynix ADS daily bars from listing |

## Reproduce

```
python3 ipo_marks_reproduce.py   # the ledger and the graded checkpoints
python3 spcx_fetch.py            # re-grade clause (b) from the data on disk
python3 spcx_fetch.py --pull     # re-fetch prices and short interest first, then grade
```

Pure Python 3 standard library. No dependencies, no API keys. Edit the CSV, re-run, the ledger moves.

## What not to conclude

- **A lock-up release is permission to sell, not selling.** Every share figure in the schedule is a ceiling on eligibility. Nothing here says a share was sold.
- **The 6 August rise is a positioning event, not a re-rating.** The capital expenditure against revenue disclosed on 4 August is unchanged by it.
- **SK Hynix is not a private-mark test.** The company was already listed in Korea, so its US listing scores issue pricing only. It is absent from the public-verdict table by design.
- **This ledger issues no verdict on whether anything is overvalued.** A valuation is a claim about the future. The instrument scores marks against later prices and stops there.
- **One figure is single-sourced**, the 12 June day-1 low used to correct v1, and it is labelled as such in the paper.

## Verification note

The lock-up terms, the release ladder, the tranche sizes, the definition of the first earnings release date, the share counts and the public float are traced to SEC filings: SpaceX Form 424B4, accession 0001628280-26-042639, and Form 10-Q, accession 0001628280-26-052535; SK hynix Inc. Form 424B4, accession 0001193125-26-299963.

The public float of 638,888,888 shares is derived, and the derivation is shown in `spcx_short_interest.csv` and in the paper: the base offering plus the over-allotment the 10-Q states was exercised in full, which ties to the disclosed net proceeds.

Daily prices and short-interest settlements come from the listing exchange's public historical endpoint. That is better than press and it is not a filing. Every close used in a graded claim was cross-checked against an independent provider and matched to the cent across all 43 shared sessions.

Modelled, estimated or press-reported inputs are identified as such rather than presented as measurements: the fund marks for the still-private companies, the SpaceX retail-allocation split, and the compute-supply arrangement disclosed below.

## Conflict of interest and scope

The research design, method, sourcing decisions and analytical judgements are the
author's. Anthropic Opus 5 assisted with data retrieval, calculation, literature
search and drafting, so this text was artificially generated and was reviewed by
the author before publication. The assisting model is not always a neutral party
to the subject matter, and in this version there are two exposures rather than one.
Anthropic is one of the private companies tracked here and is scored on a fund mark
alone. Separately, Anthropic is reported to take compute capacity from Colossus, an
xAI facility, and xAI merged into SpaceX on 30 January 2026, which is the merger
mark this ledger uses as the last private valuation before the IPO. On that
reporting the issuer graded here supplies the assisting model's maker. The merger is
primary-sourced and dated in the data; the compute arrangement is press-reported and
is not confirmed in a filing, so the second exposure is disclosed at the strength of
the weaker source rather than asserted.

Guarantee: every measured claim is traced to the primary document named in the
Verification note, and ipo_marks_reproduce.py regenerates every table from
ipo_marks_data.csv. Modelled or estimated inputs are identified as such in the
Verification note rather than presented as measurements. A reader can check
this without trusting either party.

What the author cannot guarantee: a language model's output can be wrong in
ways that survive review. In prose the error is locally plausible and
consistent in tone with what surrounds it; in code it simply runs, and a wrong
constant or a mis-set filter still returns a clean number. Several methods have
been deployed to mitigate this, including explicit instructions, internal
red-teaming and cross-lab blindspot checks, but the author does not claim the
review is exhaustive. Corrections are logged against the DOI when surfaced.

No warranty is offered beyond the terms of the CC BY 4.0 licence. Independent
analysis and open-science documentation only, not investment advice.
