# The AI Private-to-Public Ledger: A Pre-Registered Benchmark for Venture Marks and Liquidity Realisation

**Scoring private AI valuations against primary SEC filings, IPO pricing, and post-listing lock-up mechanics.**

**Author:** NM AI Research · ORCID 0009-0003-4213-7769
**Version:** 2 · 2026-08-15 · CC BY 4.0 · concept DOI 10.5281/zenodo.20672581 · supersedes v1.1.1
**Status:** *living record*. The concept DOI resolves to the latest version. **v2 grades the first lock-up checkpoint, which failed.** What changed, in full, is in the version history.

*AI disclosure: the research is the author's; this text was drafted with AI
assistance and reviewed by the author. The model, and the conflict it creates,
are named in the Conflict of interest and scope section.*

---

## 1. Purpose

Track how well private AI valuations survive contact with a real (public) price, scoring each company's valuation *marks* over time. This is not a forecast, a price target, or a bubble call. It is a referee layer: a private mark is written down, then checked against the next real repricing event, and the gap is reported.

The method is a successor to the *AI Energy-Demand Forecast Scorecard* (concept DOI 10.5281/zenodo.20572928) and the *AI Capital-Infrastructure Barbell* risk assessment (concept DOI 10.5281/zenodo.20586863), applied to finance rather than to forecasting or to supply.

## 2. Rationale

The institutions that produce private valuations cannot afford to be publicly falsifiable, so no honest, primary-sourced scoreboard of *mark vs. subsequent real price* is kept. This ledger fills that gap with four properties:

1. **Reproducible**, full data plus a standard-library script; anyone can re-run it.
2. **Primary-sourced**, S-1s, prospectuses, IPO prints, post-IPO placements, fund N-PORT marks. Press is used only where no filing exists, and labelled as such.
3. **Motive-neutral**, no book, no underwriting fee, no subscription to sell.
4. **Pre-registered**, predictions are recorded before the event, then graded.

## 3. Agnostic by design

This is not an "these are overvalued" thesis. As of scoping (2026-06-06) the prevailing direction was mark-ups, not downs. A "valuation ÷ trailing revenue = overvalued" claim falsifies instantly, because a valuation is a forward claim. The instrument instead measures each mark against the next real price or repricing, and lets the reader conclude.

## 4. Data spine

Every source below is primary and motive-independent, which is the selection rule rather than a description of what happened to be available.

| Source | What it gives | Note |
|---|---|---|
| S-1 / 424B4 / IPO price vs last private round | the public market's verdict on a private mark | primary |
| Post-IPO private placements | fresh marks after a public price exists | primary (CoreWeave: Nvidia $87.20, Jane Street $109) |
| Mutual-fund N-PORT filings | quarterly marks on still-private holdings | lagged and smoothed, a stated limitation |
| Lock-up release schedules, from the prospectus | dated, binary terms the seller's own agent wrote | primary; new in v2 |
| Exchange short-interest reports | the positioning against which a release lands | primary; new in v2, see §5.3 |
| Form 4 insider sales | what the best-informed holders do when first allowed to sell | primary |

**On source tier, stated once and applied throughout.** Filings are tier 1. Daily closing prices come from the listing exchange's public historical endpoint, which is better than press and is not a filing; every close used in a graded claim in this version was cross-checked against a second independent provider, and the one exception is named in §7.

## 5. Pre-registered predictions and their resolution

The credibility of this ledger rests on calls made before the event. The two below were recorded in the project's dated working files on 2026-06-06, with a baseline correction on 2026-06-10, ahead of the 11 to 12 June pricing. Those working files are not part of this deposit.

**Time-stamp honesty:** those were file-dated internal records; v1 was their first *public* time-stamp.

### 5.1 "Honest step-up is ≈1.4x, not the rumoured 5.1x", RESOLVED 2026-06-11

The "5.1x" figure ($350B to $1.77T) was a stale-baseline artefact: it used SpaceX's Dec-2024 tender mark and ignored four later, higher marks. Against the correct last private mark, the ≈$1.25T xAI-merger valuation (closed 30 Jan 2026), the step-up to the $1.77T IPO price is 1.42x.
**Outcome:** priced 11 Jun at $135 / $1.77T, so 1.42x. Confirmed. The catch is itself a worked example of the method: naive baselines mislead.

### 5.2 "Day-1 pop, not day-1 drop; the real correction is deferred to lock-up", RESOLVED 2026-06-12

The "it will drop on debut" intuition was judged mis-timed: a ≈4% float, Nasdaq-100 fast-entry, and a 15-day retail anti-flip rule make a supported day-1 price the likely outcome, with any real correction deferred.
**Outcome:** SPCX opened $150 (+11.1%), peaked $176.52, closed $160.95 (+19.22%, ≈$2.11T). The issue price was never broken. Confirmed.

**Correction to v1.** v1 stated that the open was the day's low, so the stock never traded below its opening price. The exchange bar records a low of $149.34 against the $150.00 open, so that detail is wrong by 66 cents. The claim resting on it is unaffected: $149.34 is still $14.34 above the $135 offer, and the issue price was not broken on debut. Logged rather than silently amended, and see §7 on its sourcing.

### 5.3 "The real correction, if any, lands at lock-up expiry, not day-1": PARTIALLY GRADED

**v1 specified this prediction defectively.** v1 §5.3 undertook to grade the call "at the lock-up date". The Form 424B4 (Space Exploration Technologies Corp, filed 12 June 2026, accession 0001628280-26-042639) sets no such date. It sets a staged release: a price-contingent tranche, two earnings-linked tranches, five fixed calendar dates, a separate extended lock-up running into 2027, and a founder lock-up longer than both. A resolution date has to match the instrument's actual release cycle rather than the shorthand used for it. That is a defect in the specification, logged as one rather than as a corrected figure. §5.3 is restated below as dated checkpoints, one of which has now resolved.

#### Clause (b): failed

The early-release condition at clause (b) required a closing price of at least $175.50, being 30% above the $135 offer price, on at least five of the ten consecutive trading days ending on and including the First Earnings Release Date. The filing defines that date as the date of public release of the Q2 2026 results, which SpaceX made on 4 August 2026, so the window is 22 July to 4 August.

**Outcome: 0 of the required 5.** The best close in the window was $125.33 on 4 August, $50.17 below the threshold, a shortfall of ≈ 29%. The result is identical if the window is ended on 5 or 6 August instead, so it does not turn on the date. The last close at or above $175.50 was 18 June; four sessions in the life of the stock have cleared it, all in the debut week, all outside every candidate window.

The level was written by the underwriters, in a binding term, as a threshold they expected the stock to clear inside two months of listing. It closed ≈ 29% short. The term is dated and binary, set by the seller's own agent rather than by a critic.

#### The remaining checkpoints

| Date | Tranche (424B4) | Shares, up to |
|---|---|---|
| 20 Aug 2026 | clause (c), 7%, 70th day | 319.0M |
| 9 Sep 2026 | clause (c), 7%, 90th day | 319.0M |
| 10 Sep 2026 | Rule 144 affiliate catch-up | 59.1M |
| 24 Sep, 9 Oct, 24 Oct 2026 | clause (c), 7% each | 328.4M each |
| after Q3 2026 results, date not announced | clause (d), 28% | ≈ 1.3bn |
| 8 Dec 2026 | clause (e), 180th day, remainder | 797.6M |
| 18 Mar 2027, 17 May 2027 | extended, 10% each, 280th and 340th days | 176.0M each |
| 12 Jun 2027 | extended 20%, plus the founder block, no early release | 351.9M, plus 6.4bn |

**What would confirm §5.3 at a checkpoint:** a fall in the SPCX close across the sessions bracketing a release date that is not recovered within the following ten sessions. What would falsify it: the ladder completing through 12 June 2027 with no such dated fall, which would place any repricing outside the release cycle. One term the schedule cannot predict bounds all of this: Goldman Sachs & Co. LLC, acting on behalf of the underwriters, may consent to a transfer at its discretion, so any checkpoint can be pre-empted by a release no schedule predicts.

**A release is permission to sell, not selling.** Every figure above is an eligibility ceiling. Nothing here asserts that any share was sold.

#### The wrong-sign finding

The lock-up model as published was supply-only: shares unlock, the float grows, supply meets a fixed bid, the mark falls. Going into the 6 August tranche the float was 638,888,888 Class A shares, of which 207,781,764 were sold short at the 31 July settlement, or 32.5%. The tranche released up to 911.5M shares, ≈ 6.9% of the 13,181,779,945 shares outstanding at 28 July. The stock rose, closing $114.92 against $108.27 the day before, up 6.14%; by 14 August the close was $140.00, 3.7% above the issue price. The model did not misfire under stress; the mechanism that operated, a marginal buyer covering a short rather than a passive allocator absorbing supply, was never in it. v2 therefore carries short interest as a percentage of public float as a column, and makes the lock-up call conditional on it. The move is a positioning event rather than a re-rating: the capital expenditure against revenue disclosed on 4 August is unchanged by it.

#### Limits of a single observation

A tempting reading is that positioning dominates when the tranche is small relative to short interest, with supply dominating otherwise. That does not hold as stated. The 6 August tranche was 4.4x the 31 July short interest, large by that measure, and the stock still rose. The framing conflates two quantities: the tranche against short interest (4.4x) and short interest as a share of the prior float (32.5%). Both are given here; neither is offered as a threshold. One observation cannot calibrate a crossover, and fitting one to n=1 would be the failure this ledger exists to catch. Later checkpoints supply further observations, at which point a ratio can be tested.

#### The 8 December consequence

The 424B4 release table makes 8 December conditional on the clause (b) outcome: up to 328.4M shares if the Additional Release Shares were released on the First Earnings Release Date, or up to 797.6M if they were not. They were not.
**8 December therefore releases up to 797.6M shares rather than 328.4M.**
The 455.8M Additional Release Shares withheld in August do not reconcile arithmetically with the 469.2M difference between the two ceilings, because both are "up to" limits and several rows carve out Rule 144 affiliates; the difference is not presented as a reconciliation. Clause (b)'s failure deferred supply into the date this ledger has always treated as the main event rather than withholding it.

## 6. The ledger (current state)

Run `python3 ipo_marks_reproduce.py` to regenerate. Summary:

- **CoreWeave, the one fully-closed loop.** Private $23B, IPO priced *at* $23B / $40 (below range), +367% to ≈$70B / $187, settled ≈$68B / $129, with two post-IPO placements above IPO once a public price existed. A private mark the public market first matched, then exceeded, then partly gave back.
- **SpaceX, live capture.** Tender ladder $210B to $350B to $400B to $800B, then the $1.25T merger mark, the $1.77T IPO (1.42x) and a $2.11T day-1 close. Two calls resolved (§5.1, §5.2); the lock-up call is now on dated checkpoints with the first one graded (§5.3).
- **SK Hynix, a second issue-pricing instance and not a private-mark test.** The US ADS listing (Nasdaq: SKHY, 424B4 accession 0001193125-26-299963) sold 177,900,000 ADSs at $149.00, raising ≈$26.5bn. The company was already listed on the KRX KOSPI, so no private mark met a public price here, and it is absent from the ledger's public-verdict table by design. What it does test is issue pricing: the ADSs closed $168.01 on debut, closed below the issue price on 27 July at $143.02, troughed at $126.79 on 29 July, and stood at $166.33 on 14 August, 11.6% above issue. A broken issue that recovered, which makes "oversubscribed does not mean correctly priced" a two-instance claim while stopping well short of a verdict on the company.
- **OpenAI ($852B) and Anthropic ($965B), still private.** No public price test yet; fund N-PORT marks are the only outside read (lagged, smoothed). Named as a limitation, not scored.

## 7. Limitations (read before citing)

- **Per-share figures are not comparable across the SpaceX merger and recap** ($421 tender against $135 IPO reflects a share-count change). Compare valuations, not per-share prices, across that boundary.
- **A release is permission to sell, not selling.** Every lock-up figure in §5.3 is a ceiling on eligibility.
- **Short interest is measured bi-monthly at settlement**, so it is a snapshot and not a continuous series. The 32.5% figure is the 31 July settlement against the IPO float, and every settlement used here predates the 6 August unlock, which is why the IPO float is the correct denominator throughout.
- **The public float is an upper bound.** It is the count of shares sold in the offering and assumes nothing else became freely tradable before 6 August, which the release schedule supports but does not prove.
- **One figure in this version is single-sourced.** The 12 June day-1 low of $149.34, used to correct v1 §5.2, comes from the exchange endpoint only; the independent provider used to check every other close does not carry the IPO session. The correction is published with that basis named rather than presented as settled.
- **SK Hynix is not a private-mark observation** and must not be read as one, see §6.
- **The SpaceX retail-allocation figure is press-sourced, not a filed term.** SpaceX announced up to 30% of the offering for retail; reporting on 11 June (CNBC, citing a person familiar) put the delivered tranche in the low 20s of a percent as institutional demand overwhelmed the book. The split is a bookrunner decision and does not appear in the prospectus, so it stays reported rather than primary. Carried since v1 and logged as an announced-against-delivered datapoint, flagged provisional. It grounds no claim in this version.
- **Fund N-PORT marks lag and smooth**, they are an estimate of a private value, not a price.
- **Forward-claim caution.** A valuation is a claim about the future; this ledger scores marks against later prices and issues no "overvalued" verdict.
- **Pre-registration value is prospective from v1.** §5.1 and §5.2 were recorded in dated working files before the event but were first time-stamped publicly at v1, so a reader is asked to take the pre-registration of those two on trust. §5.3 and every checkpoint in it were published before resolving, and clause (b) is the first of them to be graded, which is the first fully public instance of the method working end to end.

## 8. Reproducibility

```
python3 ipo_marks_reproduce.py   # the ledger, including graded checkpoints
python3 spcx_fetch.py --pull     # re-pull the price series and re-grade clause (b)
```

Pure Python 3 standard library, no dependencies, no API keys. Files: `ipo_marks_data.csv` (the marks), `spcx_daily.csv` and `spcx_daily_secondsource.csv` (the price series and its independent check), `spcx_short_interest.csv` (settlement short interest against float), `spcx_lockup_schedule.csv` (the release ladder as filed), `skhy_daily.csv`, `ipo_marks_reproduce.py`, `spcx_fetch.py`.

## 9. Versioning (the "living" part)

| Version | Trigger | Adds |
|---|---|---|
| v1 | SpaceX day-1 close captured | §5.1 and §5.2 resolved; §5.3 opened |
| v2 (this) | clause (b) price condition resolved, 4 Aug 2026 | grades clause (b); respecifies §5.3 as dated checkpoints; adds short interest as a share of float and makes the lock-up call conditional on it; adds SK Hynix |
| v3 | 8 Dec 2026, clause (e), now up to 797.6M shares | the main supply wave, with the positioning test run forward |
| v4 | 12 Jun 2027 | the founder block, the one tranche positioning is unlikely to absorb |
| v(n) | next AI IPO (OpenAI / Anthropic) or fresh placement | new private-to-public verdict |

## 10. Disclosure

The author holds no financial position in, and receives no compensation from, any entity named in this ledger. No third party reviewed, funded, or directed this work.

Two conflicts are disclosed and neither is financial. Both are argued in the Conflict of interest and scope section, which also names the assisting model. In short: one of the companies tracked here is still private and is the maker of that model, and the issuer graded in this version is reported to supply compute capacity to it. Any reading that touches either is non-neutral and is deflated accordingly, and primary, motive-independent sources (prospectuses, 10-Q filings, exchange prints) are preferred throughout over any framing favourable to either.

## 11. Sources (v2)

SpaceX Form 424B4 filed 12 June 2026 (accession 0001628280-26-042639) and Form 10-Q filed 4 August 2026 (accession 0001628280-26-052535), both SEC EDGAR; SK hynix Inc. Form 424B4 (accession 0001193125-26-299963); Nasdaq daily historical prints and the Nasdaq/FINRA bi-monthly short-interest reports for SPCX and SKHY, cross-checked against an independent price provider; SpaceX S-1 and IPO coverage (3 to 12 Jun 2026); Morningstar fair-value estimate; CoreWeave S-1 and post-IPO placement filings. Specific figures and their grading are carried in the CSV `notes` and `verified` columns.

---

## Version history (for reference)

*Corrections are logged rather than silently applied. The living-record versioning plan is separate, see §9.*

**Retitled at v2.** Versions 1 through 1.1.1 were published as *The AI Private-Valuation Marks-vs-Reality Ledger*. The concept DOI is unchanged and resolves to this version, so citations of the earlier title and of the concept DOI both remain valid. The new title states what the instrument does rather than how it was first described.

- **v2 (2026-08-15).** First lock-up checkpoint graded: clause (b) failed, 0 of 5. §5.3 respecified from a single date to dated checkpoints, and v1's specification named as defective. Short interest as a share of public float added to the method and to the data, after the 6 August unlock coincided with a 6.14% rise against a supply-only model that predicted a fall. SK Hynix added as an issue-pricing instance, explicitly not a private-mark test. v1 §5.2's "the open was the day's low" corrected to a $149.34 low, with the call unaffected. 8 December quantified at up to 797.6M shares as a consequence of clause (b) failing. Two limitations carried since v1, on the press-sourced retail allocation and on the prospective value of the pre-registration, were dropped in an early draft of this version and are restored; the compute-supply exposure in the conflict of interest section is now disclosed at the strength of its weakest source rather than asserted.
- **v1.1.1 (external red-team, 2026-07-04).** Disclosure expanded to name the non-financial conflict; "propped" softened to "supported"; house-style formatting pass. No call or datapoint changed.
- **v1.1 (standards refresh).** Corrected a stray day-1 intraday high, standardised the Morningstar gap, tidied the Anthropic Series H note. Repackaged to portfolio standard. No call or datapoint changed.
- **v1 (2026-06-12).** Initial release; SpaceX day-1 close captured, §5.1 and §5.2 resolved, §5.3 opened.

## Verification note

Which figures were traced to which primary document, and which were not.

**Traced to a filing (tier 1).** The lock-up terms, the clause (b) threshold as a percentage of the offer price, the definition of the First Earnings Release Date, the 911.5M and 455.8M tranche sizes, the 797.6M against 328.4M conditional at 8 December, the full release ladder including the 2027 extended and founder dates, and the discretionary-consent party: all from SpaceX Form 424B4, accession 0001628280-26-042639. Shares outstanding of 13,181,779,945 at 28 July 2026, and the confirmation that the over-allotment was exercised in full for 638.9M shares sold: SpaceX Form 10-Q, accession 0001628280-26-052535. The SK Hynix offering size, ADS ratio and $149.00 issue price: SK hynix Inc. Form 424B4, accession 0001193125-26-299963.

**Derived, with the derivation shown.** The 638,888,888-share public float is the 555,555,555-share base offering plus the 83,333,333-share over-allotment, which the 10-Q states was exercised in full; 638,888,888 multiplied by $135 gives $86.25bn gross against the $85,675M net proceeds plus $575M of costs disclosed, which ties. The $175.50 threshold is 30% above the $135 offer price, computed here because the filing states the condition as a percentage. Short interest as a percentage of float divides a reported settlement figure by that float.

**Exchange data, not a filing.** All daily opening, high, low and closing prices for SPCX and SKHY, and the bi-monthly short-interest settlements, come from the listing exchange's public historical endpoint. Every SPCX close used in a graded claim was cross-checked against an independent price provider and matched to the cent across 43 shared sessions.

**Single-sourced, and named as such.** The 12 June 2026 day-1 low of $149.34, used in §5.2 to correct v1. The independent provider does not carry the IPO session, so this figure rests on one source.

**Secondary or estimated, not used to ground a graded claim.** The Morningstar fair-value estimate, which appears only in the version history and in the superseded data row it belonged to, not in any claim made here. The SpaceX retail-allocation split, press-reported and flagged in §7. The compute arrangement between the assisting model's maker and a SpaceX facility, disclosed in the conflict of interest section and press-reported rather than filed; the underlying xAI merger is primary and dated. Fund N-PORT marks for OpenAI and Anthropic, which are lagged and smoothed estimates rather than prices and are named as a limitation rather than scored.

**Not established here.** Whether any released share was actually sold. The ledger records eligibility, not transactions.

## Conflict of interest and scope

The research design, method, sourcing decisions and analytical judgements are the
author's. Anthropic Opus 5 assisted with data retrieval, calculation, literature
search and drafting, so this text was artificially generated and was reviewed by
the author before publication. The assisting model is not always a neutral party
to the subject matter, and in this version there are two exposures rather than one.
Anthropic is one of the private companies tracked here and is scored in §6 on a fund
mark alone. Separately, Anthropic is reported to take compute capacity from Colossus,
an xAI facility, and xAI merged into SpaceX on 30 January 2026, which is the merger
mark this ledger uses as the last private valuation in §5.1. On that reporting the
issuer graded in §5.3 supplies the assisting model's maker. The merger is
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
