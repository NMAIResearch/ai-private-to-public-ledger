# The AI Private-to-Public Ledger: capture protocol for the lock-up checkpoints, version 7

**Status: resolved rendering of N.'s selections (selections record 2bb51bcd455c...), from template 5ef41810ed90...; only this rendering is operative.**

Research lead, Anthropic Claude Opus 5.5 through Claude Code, 17 October 2026.

Nothing has been graded, captured or published under this protocol. No close inside a checkpoint window after
14 August 2026 was retrieved or viewed while writing it.

## 0. How this file is approved

- This is the **resolved** rendering of the template. It holds only the options N. selected, listed in section 8. The
  full rendering, with every option, is kept in the project's records for reference and is not operative.
- N. approves the resolved rendering's exact bytes, named by its SHA-256. The receipt that D11 defines for the selected
  registration records that digest, and every grade record carries the digest and the receipt.
- A later substantive change makes a new resolved file with a new digest, and the labels are recalculated under D11.

## 1. What v2 fixes, and this protocol does not change

Quoted from the published v2 (`ipo_marks_ledger_v2.md`, record 21960028):

- The rule: "**What would confirm §5.3 at a checkpoint:** a fall in the SPCX close across the sessions bracketing a
  release date that is not recovered within the following ten sessions."
- The falsifier: "the ladder completing through 12 June 2027 with no such dated fall, which would place any repricing
  outside the release cycle".
- The caveat: "Goldman Sachs & Co. LLC, acting on behalf of the underwriters, may consent to a transfer at its discretion,
  so any checkpoint can be pre-empted by a release no schedule predicts."
- Eligibility: "**A release is permission to sell, not selling.**"
- No threshold: "Both are given here; neither is offered as a threshold." (of the tranche against short interest, and of
  short interest as a share of float)
- Source practice: "every close used in a graded claim in this version was cross-checked against a second independent
  provider, and the one exception is named in §7."
- The ladder: "`spcx_lockup_schedule.csv` (the release ladder as filed)".

**What the ladder file holds against the prospectus.** Each row is matched to its trigger or date line and its ceiling
line in the prospectus's "Shares Eligible for Future Sale" table, and the counts below are generated from that match:

- 16 of its 17 release rows carry the filed ceiling. The 180th day's 797.6 million is the filed branch that applies because clause (b) failed.
- Clause (b)'s row carries 0. That is the outcome, nothing released, and not a filed term; the filed ceiling is 455.8 million.
- 11 rows carry a date the prospectus states.
- 2 rows, clause (a)'s and clause (b)'s, carry 6 August, which comes from the 4 August results release, as v2 records it.
- 4 results-linked rows carry placeholder months. Their dates come from the results releases (D1).

This protocol adds no threshold, no minimum fall and no condition. It fixes in advance only what v2 leaves open: the
sessions, the closes and their sources, the roster of checkpoints, and how the data are captured and kept.

## 2. Definitions

| ID | Term | Selected by N. |
| --- | --- | --- |
| D1 | Release session s0 | fixed, no option |
| D2 to D4 | Reference close, fall and recovery, as one bundle | bundle R |
| D5 | Outcome and evidence status | fixed, no option |
| D6 | The third price source | Yahoo Finance, for disputes only |
| D7 | Short interest | fixed, no option |
| D8 | Overlap | fixed, no option |
| D9 | Checkpoints already passed | graded, with a label |
| D10 | The roster | the ladder |
| D11 | Registration | public registration |
| 4.5 | Extraction and grading | new code |

### D1. Release session s0

- **A fixed-date release.** s0 is the first regular Nasdaq session on or after the date. Every release in the prospectus
  is worded "on or after" its date, so a weekend date gives the following Monday: 24 October 2026 gives 26 October, and
  12 June 2027 gives 14 June.
- **A results-linked release.** The prospectus says "on or after the second full trading day on Nasdaq immediately
  following the public release of our quarterly financial results", which "for this purpose does not include “flash”
  numbers or preliminary, partial earnings". So s0 is the second regular Nasdaq session that opens after the time of
  the results' public release, timed by the release itself, which is kept as an original.
- **The 180th day.** Clause (e) gives 8 December 2026. The period's own end, "immediately after the close of the trading
  day on the 180th day", would give 9 December. D1 fixes 8 December. Choosing 9 December would change which closes are
  compared, so the choice is fixed here, before any December price exists.
- **The founder block.** Its lock-up lasts until "immediately after the close of the trading day on the 366th day". 12
  June 2027 is a Saturday, so its first session is Monday 14 June, the same s0 as the extended 20% release.

### D2 to D4. Reference close, fall and recovery

"Below" and "at or above" are compared as D6 sets out.

- **Bundle R**: the reference is the close of s-1; a fall is the close of s+1 below it; recovery is any
  close at or above the reference from s+2 to s+11.
  - The two closes lie on either side of the release date for every checkpoint, weekday or weekend, with the release
    session between them.
  - With s0 fixed, the grade does not depend on whether a release takes effect at the open of s0 or after its close.
  - Ten sessions follow the fall close.

### D5. Outcome and evidence status

- **Three price outcomes.**
  - *Fall, not recovered*: confirms section 5.3 at that checkpoint.
  - *Fall, recovered*, and *no fall*: neither confirms.
- **An evidence status, kept separate.**
  - *Corroborated*: every decisive close agrees in two sources.
  - *Single-source*: a decisive close comes from one source only, named as v2 named its one exception.
  - *Disputed, outcome unchanged*, or *unresolved*: as below.
- **Decisive closes.**
  - The reference close and the fall close.
  - For *fall, recovered*: one recovering close.
  - For *fall, not recovered*: all ten closes of the recovery window.
- **Disputed or missing closes.** Each is tried at every value it could take: each candidate value for a disputed close,
  and any value for a missing one.
  - If the outcome is the same every time, it stands as *disputed, outcome unchanged*.
  - If not, the checkpoint is *unresolved*.
  - An unresolved checkpoint never counts as *no fall* (D10).

### D6. Closes, sources, sessions and exceptional days

**The close.**

- The value is the listing exchange's closing price for the regular session, as its historical endpoint reports it:
  the `close` field that `spcx_fetch.py` reads.
- It is in US dollars per SPCX Class A share, taken as published, at the cent.
- That this field is Nasdaq's official closing price is an assumption. `spcx_fetch.py`'s own note calls the endpoint
  undocumented.

**Comparison and precision.**

- Two sources agree on a close when their published values are equal at the cent.
- "Below" and "at or above" compare values exactly. Published closes are compared as published.
- If a corporate action applies (below), the adjusted value is computed in exact decimal arithmetic from the published
  close and the exchange's published factor, and is compared without rounding. For example, 2.01 after a 1-for-2 reverse
  split is 1.005 on the old share basis, which is below a 1.01 reference.

**The sources.**

- **Second source.** The close from stockanalysis.com's SPCX history, as in v2's second-source file.
- **Third source, for disputes only**. Yahoo Finance's SPCX history, read from its close column that is
  not dividend-adjusted; the first retrieval records the column used. If Yahoo Finance cannot be reached at capture, no
  other source is substituted.

**Adjudication.**

- The exchange value is the close. If the second source agrees at the cent, the close is corroborated.
- If they disagree, the third source is read:
  - If it equals the exchange value, the close is corroborated by the third source.
  - Otherwise the close is disputed. Every distinct value is a candidate, and D5 decides.
- No source ever overrides the exchange value.
- If the exchange has no value and the second source has one, the close is single-source.

**The calendar.**

- Sessions are Nasdaq's regular sessions: weekdays that are not full-day holidays in Nasdaq's published schedule.
- Nasdaq's published 2026 schedule is retained as retrieved on 17 October 2026 (SHA-256 72329043...).
- Nasdaq does not yet list 2027. NYSE's published 2027 schedule, retained as retrieved on 17 October 2026 (SHA-256
  79602f7b...), gives the provisional 2027 sessions until Nasdaq's is retained.
  - If the two differ, Nasdaq's governs. The change is recorded before the affected checkpoint's s-1.
- The project's session-date tool holds the complete lists for 2026 and 2027, and refuses dates outside those years.

**Exceptional days.**

- **Early closes** count as sessions, with their closes: 27 November and 24 December 2026, and 26 November 2027. Each
  closes at 13:00 New York time.
- **Halts.** A session in which SPCX traded at all counts, with its close. A session in which SPCX did not trade at all,
  through a full-day halt or a suspension, still counts, so the window never moves. Its close is missing, and D5 decides.
- **An unscheduled market-wide closure** is not a session. The window is counted over the sessions Nasdaq actually held,
  with Nasdaq's notice retained. D11's labels are then recalculated from the session that actually becomes s-1.
- **Corporate actions.** If a split, reverse split or stock distribution takes effect between s-1 and s+11, every close
  is compared on the share basis of s-1, as above. Raw and adjusted values are both kept. No cash dividend is adjusted.
- **Corrections.** A correction published after a grade record is written does not replace the record. A dated erratum
  records the corrected value and the outcome it gives, and both stay visible.

### D7. Short interest: context, never part of the grade

- **Settlements used.** The last settlement date on or before s0 and the first settlement date after s0. With next-day
  settlement, a settlement on s0 reflects trades through s-1 at the latest.
- **What is recorded.** Short interest, average daily volume and days to cover, in shares and as published. The
  tranche's ceiling is set against the short interest, as v2 did.
- **No float denominator.**
  - After the 6 August unlock, the IPO float is no longer a justified denominator unless there is a supported
    contemporaneous float measure.
  - None is derived from the schedule. Its running sum is, in the file's own warning, a sum of ceilings and not a float
    projection.
  - The note in the published fetcher to compute the float from the schedule is not followed. The script itself stays
    unchanged.
- **Pending reports.** A settlement not yet published at capture is recorded as pending and added later. It never
  delays or changes a grade.
- **One inherited ambiguity, stated rather than resolved.** v2 says it "makes the lock-up call conditional on" short
  interest, yet states no condition and offers no threshold. The protocol grades the price rule as v2 words it and
  records short interest beside it.

### D8. Overlap

- Every checkpoint is graded. Overlap is recorded, and never used to exclude a checkpoint.
- An overlap is another release session on any session from s-1 to s+11, inclusive.
- Releases with the same s0 form one checkpoint, with every tranche named. On 14 June 2027 these are the extended 20%
  release and the founder block.
- A discretionary early release, a consent under the lock-up, is recorded when a filing or a press release discloses it.
  v2's caveat stands for any that are not disclosed.
- No outcome is attributed to a tranche, overlapped or not.

### D9. Checkpoints already passed

- **Graded, with a label**. The passed checkpoints are graded by the same rule, each labelled under D11.
  Every passed checkpoint, clause (a) on 6 August and the 70th to the 120th day, is *graded after the fact*, and so is
  any later one if registration comes late.

### D10. The roster: which checkpoints count for v2's rule

**The ladder**. Every release in v2's ladder file with a release date from 6 August 2026 to 12 June 2027
counts: v2's table plus clause (a) on 6 August, a passed checkpoint treated under D9, and the extended lock-up's two
results-linked releases after the Q4 2026 and Q1 2027 results. Clause (b) released nothing, so it is not a checkpoint.

- v2's rule speaks of "a release date", and its falsifier of "the ladder"; v2 calls the file "the release ladder as
  filed".
- v2's falsifier says no fall "would place any repricing outside the release cycle", and a fall at a results-linked
  release would be inside it.
- v2's table already includes one results-linked release, clause (d).

**Membership of a results-linked release.** Its release date is fixed by D1 from the results release. It belongs to v2's
falsifier only if that date falls on or before 12 June 2027 and the roster includes it. The release after the Q2 2027
results falls after 12 June 2027 on any reading: it is graded and reported separately, and whether a later version
registers it is N.'s decision.

**Confirmation and completion.**

- Confirmation is per checkpoint, as v2 words it. The record lists every confirming checkpoint and adds no count
  threshold.
- The falsifier is met only when every included checkpoint is graded, none is *fall, not recovered* and none is
  *unresolved*, after the latest recovery window among the included checkpoints has closed.
- For the 12 June 2027 release that is 30 June 2027. That window ends last among the included checkpoints,
  so a release dated after 12 June 2027, which is outside the falsifier, cannot delay completion.

### D11. Freeze, registration and labels

- **The freeze.** N. approves the resolved rendering's exact bytes, named by its SHA-256 (section 0).
- **Registration**. The resolved file is committed, with its SHA-256 in the commit message, to the
  ledger's public repository, and pushed. The registration time is the host's recorded push time, and the receipt is the
  commit identifier with that time. This is a public step and N.'s decision.
- **Labels.** Each checkpoint gets one:
  - *pre-registered*: the public registration comes before the scheduled close of the checkpoint's s-1, the reference
    close. That is 16:00 New York time, or 13:00 on an early-close day.
  - *pre-registered, internal only*: only N.'s recorded approval comes before that close. This keeps v2's line between
    file-dated internal records and a public timestamp.
  - *graded after the fact*: otherwise.
- **Deadlines.** Section 3 gives each fixed-date checkpoint's label deadline in UK time. A results-linked checkpoint's
  deadline is the scheduled close of its own s-1, once its results release dates it.
- **The nearest deadline.** For the 135th-day checkpoint (release date Saturday 24 October 2026), s-1 is Friday
  23 October, a full session, so its label deadline is 21:00 BST that day.
  The host's recorded push must come before it.
  Missing it changes only that checkpoint's label and those of later checkpoints whose s-1 passes first; no grade
  changes.

## 3. Dates

Generated from the project's session-date record (sessions as in D6).

| Release (ladder file) | Release date | In v2's table | s-1 | s0 | s+1 | s+10 | s+11 | Label deadline | Other release sessions from s-1 to s+11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clause (a), 20%, 2nd trading day after the 4 August results | Thu 6 Aug 2026 | no | 5 Aug | Thu 6 Aug 2026 | 7 Aug | 20 Aug | Fri 21 Aug 2026 | 21:00 BST, 5 Aug | clause (c), 7%, 70th day |
| clause (c), 7%, 70th day | Thu 20 Aug 2026 | yes | 19 Aug | Thu 20 Aug 2026 | 21 Aug | 3 Sep | Fri 4 Sep 2026 | 21:00 BST, 19 Aug | none |
| clause (c), 7%, 90th day | Wed 9 Sep 2026 | yes | 8 Sep | Wed 9 Sep 2026 | 10 Sep | 23 Sep | Thu 24 Sep 2026 | 21:00 BST, 8 Sep | Rule 144 affiliate catch-up, 91st day; clause (c), 7%, 105th day |
| Rule 144 affiliate catch-up, 91st day | Thu 10 Sep 2026 | yes | 9 Sep | Thu 10 Sep 2026 | 11 Sep | 24 Sep | Fri 25 Sep 2026 | 21:00 BST, 9 Sep | clause (c), 7%, 90th day; clause (c), 7%, 105th day |
| clause (c), 7%, 105th day | Thu 24 Sep 2026 | yes | 23 Sep | Thu 24 Sep 2026 | 25 Sep | 8 Oct | Fri 9 Oct 2026 | 21:00 BST, 23 Sep | clause (c), 7%, 120th day |
| clause (c), 7%, 120th day | Fri 9 Oct 2026 | yes | 8 Oct | Fri 9 Oct 2026 | 12 Oct | 23 Oct | Mon 26 Oct 2026 | 21:00 BST, 8 Oct | clause (c), 7%, 135th day |
| clause (c), 7%, 135th day | Sat 24 Oct 2026 | yes | 23 Oct | Mon 26 Oct 2026 | 27 Oct | 9 Nov | Tue 10 Nov 2026 | 21:00 BST, 23 Oct | none |
| clause (e), 180th day, remainder (up to 797.6M) | Tue 8 Dec 2026 | yes | 7 Dec | Tue 8 Dec 2026 | 9 Dec | 22 Dec | Wed 23 Dec 2026 | 21:00 GMT, 7 Dec | none |
| extended (b), 10%, 280th day | Thu 18 Mar 2027 | yes | 17 Mar | Thu 18 Mar 2027 | 19 Mar | 2 Apr | Mon 5 Apr 2027 | 20:00 GMT, 17 Mar | none |
| extended (d), 10%, 340th day | Mon 17 May 2027 | yes | 14 May | Mon 17 May 2027 | 18 May | 1 Jun | Wed 2 Jun 2027 | 21:00 BST, 14 May | none |
| extended (e), 20%, and the founder block, 366th day | Sat 12 Jun 2027 | yes | 11 Jun | Mon 14 Jun 2027 | 15 Jun | 29 Jun | Wed 30 Jun 2027 | 21:00 BST, 11 Jun | none |
| clause (d), 28%, after the Q3 2026 results | dated by the results release | yes | | | | | | scheduled close of its s-1 | recorded once dated |
| extended (a), 20%, after the Q4 2026 results | dated by the results release | no | | | | | | scheduled close of its s-1 | recorded once dated |
| extended (c), 20%, after the Q1 2027 results | dated by the results release | no | | | | | | scheduled close of its s-1 | recorded once dated |
| extended (f), remainder, after the Q2 2027 results | dated by the results release | no | | | | | | scheduled close of its s-1 | recorded once dated |

The last column lists every overlap among the dated releases (D8). Clause (d)'s session may fall inside the 135th-day
window once it is dated.

## 4. Capture

### 4.1 Before and after each capture

Check the SHA-256 of every v2 file in the project home against the record. These checks are read only.

### 4.2 Retrieval

- Each response is kept as an original. A capture log line records its URL, the request time in UTC, the HTTP status, the
  response headers and the SHA-256.
- Requests carry a declared user-agent naming the project, with no contact address. A page that refuses it is saved
  through the shared agent browser, and the record says so.

1. **Exchange closes.**
   `https://api.nasdaq.com/api/quote/SPCX/historical?assetclass=stocks&fromdate=2026-08-01&todate=<capture date>&limit=400`,
   fetched with `curl -sS -A '<declared user-agent>' -D <headers file> -o <body file> -w '%{http_code} %{size_download} %{url_effective}'`,
   then `sha256sum`.
2. **Second source.** `https://stockanalysis.com/stocks/spcx/history/`, fetched the same way.
3. **Third source, only when D6 calls for it.** `https://finance.yahoo.com/quote/SPCX/history/`, fetched the same way.
4. **Short interest.** `https://api.nasdaq.com/api/quote/SPCX/short-interest?assetclass=stocks`.
5. **Results-linked checkpoints.** The results release and its 8-K, kept with their times, to fix s0 under D1. SEC pages
   come by N.'s hand download, because SEC refuses undeclared automated requests.
6. **FINRA's calendars.** FINRA's published short-interest calendars for 2026 and 2027, kept once, to time each capture
   after a settlement is published.

### 4.3 Extraction and grade

- An extraction step reads only the kept originals and writes a dated table: each session's close from each source,
  with the original's digest. It never edits an original or a v2 file.
- A grading step applies D1 to D11 to that table and writes one grade record per checkpoint.

### 4.4 Storage

Each capture goes into a new dated folder in the project home, made after N.'s approval. Nothing is overwritten. A
re-capture is a new folder.

### 4.5 Tools

- **v2's `spcx_fetch.py` is not the capture tool.**
  - It discards the response bytes (lines 57 to 59), rewrites both CSVs (lines 71 and 100) and grades clause (b) (lines
    128 to 149).
  - It stays unchanged as published, and its clause (b) output is never a checkpoint grade.
- **Retention needs no new tool:** curl and sha256sum do it.
- **Extraction and grading: new code**. No existing tool in the project does this: its fetchers, v2's
  included, keep parsed values only.
  - Before first use, it must pass synthetic fixtures for: the impossible pairing; recovery only at s+11; a change of s0
    from 8 to 9 December; a reverse split giving a half-cent value; an early-close reference session; a disputed close
    that changes the outcome; and a missing decisive close.
  - It is run read-only on v2's own CSVs as a baseline, and reviewed by another model family before first use.

### 4.6 The grade record

One record per checkpoint, with these fields:

- the resolved protocol's SHA-256 and the receipt D11 defines for the selected registration;
- the selections in force (section 8) and the roster's decision on this checkpoint (D10);
- the checkpoint and its tranches, the release date and the s0 rule;
- the session dates s-1 to s+11;
- for each session: each source's close with its original's digest, the agreement, and any exception (a halt, an early
  close or a corporate action);
- the bundle, the outcome, the evidence status and the decisive closes;
- the overlaps and the short-interest context;
- the label (D11), the capture time and any errata.

## 5. Sources to log in the register

Entries for the project's source register are prepared, to be added after N.'s approval. In the register's backfill
dated 23 August 2026, the prospectus's entry names the EDGAR index page as its URL and records the document as not
retrieved; the register's current state is checked when the entries are added. The entries:

- the 424B4 primary document, now retained: N.'s hand download, e686a5b4..., and 6e2ca070... once the delivery
  network's injected tag is removed;
- Nasdaq's and NYSE's holiday schedules, retained;
- the price sources: the exchange's historical endpoint, stockanalysis.com, and Yahoo Finance for disputes only;
- the short-interest sources: the exchange's short-interest endpoint, and FINRA's 2026 and 2027 calendars;
- the results releases and 8-Ks that date clause (d) and the extended lock-up's results-linked releases.

What the maker's records cannot show from text extractions alone: the fidelity of each extraction to its original, and
the provenance of the injected tag the delivery network adds. The originals and their digests are retained for that.

## 6. Still open

1. Nasdaq's 2027 schedule, retained once published. Until then NYSE's provisional 2027 calendar applies (D6); a
   difference is recorded before the s-1 of the checkpoint it affects.
2. The checks that 4.5 requires, before the extraction or grading they cover. Retrieval needs no new tool (4.5), so
   captures can be kept before then.

## 7. Conflicts

The drafting model is Anthropic's, and Anthropic and OpenAI are both tracked private companies in this ledger. The
protocol's reviewer, GPT-6.1 Sol, is OpenAI's. The protocol concerns SpaceX's lock-up and grades nothing for either
company.

## 8. Selections

- Reference close, fall and recovery, as one bundle (D2 to D4): **bundle R**
- The third price source (D6): **Yahoo Finance, for disputes only**
- Checkpoints already passed (D9): **graded, with a label**
- The roster (D10): **the ladder**
- Registration (D11): **public registration**
- Extraction and grading (4.5): **new code**

Selections record SHA-256 2bb51bcd455c076cffc1004fa031fb46a74bf16f43c5f0bf0ca7cba85d45adca; template SHA-256 5ef41810ed90166f44f65a9fa2e9c3913c3d1075ff401701f52109702ede471d.
