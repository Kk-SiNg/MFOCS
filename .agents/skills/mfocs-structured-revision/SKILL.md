---
name: mfocs-structured-revision
description: >-
  Deliver a complete, bottom-up, confusion-clearing structured walkthrough of a
  single CS208 (MFOCS) topic anchored strictly to the class Readable_notes
  transcription, and optionally export it as an offline pre-rendered KaTeX
  HTML sheet in Final_rev. Use whenever the user says a topic is getting
  confusing, asks to cover one subject/stage thoroughly in depth at once
  without jumping to later topics, wants a structured revision guide from
  Readable_notes.html or Part_01..Part_04, or asks to save a revision
  explanation as HTML in Final_rev.
---

# MFOCS Structured Revision

This skill turns dense MFOCS topics into fast-to-master, exam-ready mental
models grounded strictly in the class notes — combining interleaved micro-chunks
with high-ROI 48-hour exam-prep workflows (worked-example anchors, cue-to-method
triggers, active retrieval, and zero-bloat triage) without sacrificing proof
rigor or depth.

## Core Principles (Why Each Step Matters)

1. **Single-unit scope lock:** Cover **only** the requested topic or stage
   completely in one structured pass — do not jump ahead to later topics or mix
   adjacent chapters. Introducing later machinery before the current mental model
   settles recreates confusion.
2. **Ground strictly in `Readable_notes`:** Always read the matching pages in
   `Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/Part_01..04.md` (using
   `Page_index.md` or `Endsem_Study_Checklist.md` to locate the exact page
   range) before writing. Match the instructor's exact notation (`0`/`1` vs
   `T`/`F`, indexing conventions), examples, and **Textbook/Source
   clarifications**, and cite exact PDF page tags (`pp. X–Y`) inline so the
   learner can cross-check `Readable_notes.html#pdf-page-XXX`.
3. **Interleaved micro-chunks (`Short Theory → Immediate Examples → Next Chunk`):**
   Never front-load all definitions, taxonomies, traps, and abstract
   mental-model resets across the whole unit before showing worked problems,
   and never dump all worked examples at the bottom. Partition the unit into
   small concept chunks: give **only** the short theory needed for Chunk 1,
   immediately solve Chunk 1's example(s) right beneath it (with that chunk's
   trap/layer split in place), then move to Chunk 2's short theory + examples,
   and so on.
4. **Never reference an unspecified question early:** Do not cite a question,
   proof, or failure case by shorthand (such as *"the $3n+2$ example"* or
   *"the balls problem"*) before stating the full problem. Every example must
   state the complete claim, domain, and hypotheses the first time it appears.
5. **Connect along the way (*"Why not use a previous trick?"*):** Whenever you
   introduce a new chunk or solve a new example, explicitly connect back to
   previous chunks or earlier units:
   - **When an earlier trick stalls:** Show the exact step where the previous
     method breaks down (for example, why a direct attempt on $3n+2=2k+1$
     stalls at $3n+1=2k$) before pivoting to the new method.
   - **When an earlier trick helps:** Point out where a previous rule or proof
     fires inside a sub-step or shortcut (for example, using contraposition of
     an earlier parity result inside a contradiction proof).
6. **48-hour exam-speed engineering (80/20 Triage, Exam Cues & Key Moves):**
   - **Triage effort:** Tag each chunk with its note-backed depth (`Core Tool`,
     `Supporting Proof`, or `Context Only`) so the learner spends 80% of their
     focus on derivable patterns rather than memorizing remarks the notes leave
     conceptual.
   - **Cue-to-method recognition:** Give each chunk a 1-line **Exam Cue**
     (`If you see ... → use ...`) so time isn't lost picking tools under exam
     stress.
   - **Anchor-step compression:** Call out **The Key Move** (1 sentence naming
     the creative leap) atop every worked proof so the learner reconstructs
     multi-step proofs from one anchor instead of rote-memorizing lines.
7. **Separate confused layers inside the chunk where they happen:** Confusion in
   discrete math comes from conflating two distinct layers (for example,
   *assigning `0`/`1` to variables* vs. *evaluating compound premises*, or
   *global universal target* vs. *local $P(k) \Rightarrow P(k+1)$ link*). Name
   both layers right inside the relevant chunk alongside its concrete example.

---

## Workflow

### Step 1: Locate & Read the Exact Unit Range

1. Map the user's requested topic to its PDF page range in
   [Endsem_Study_Checklist.md](../../../Endsem_Study_Checklist.md) or
   [Page_index.md](../../../Post_midsem_exam_prep_2026-11-25/Readable_notes/Page_index.md).
2. Read the corresponding sections in
   [Part_01](../../../Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/Part_01_pages_001-075.md),
   [Part_02](../../../Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/Part_02_pages_076-150.md),
   [Part_03](../../../Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/Part_03_pages_151-205.md),
   or
   [Part_04](../../../Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/Part_04_pages_206-221.md).
3. Extract every definition, notation detail, class example, failure case, and
   source clarification within that exact page range, group them into natural
   sequential chunks (`Chunk 1, Chunk 2, ..., Chunk N`), and classify each
   chunk's depth (`Core Tool`, `Supporting Proof`, or `Context Only`) strictly
   from what the notes actually prove vs. mention informally.

### Step 2: Deliver the Interleaved Chunked Explanation

Start with a compact 2–4 line **Triage Roadmap** listing the chunks (`pp. ...`)
with their depth tags so the learner knows where to focus, without front-loading
abstract traps or citing unstated problems. Then walk through each chunk
sequentially, ending with a high-yield consolidation block:

#### Repeated Cycle: For Each Chunk (`Chunk 1` … `Chunk N`, tagged `pp. ...` + Depth Tag)

1. **Short Theory, Exam Cue & Domain Boundaries (`pp. ...`)**
   - **Exam Cue (1 line):** When a problem takes shape X, pick this tool.
   - **Short Theory:** Present only the definitions, schema, formula, or
     mental-model distinction needed for **this** chunk in exact class
     notation.
   - Bold exact deciding conditions (e.g., *"False ONLY when $p=1$ and
     $q=0$"*) and explicitly state any domain restrictions or non-examples from
     the notes.
   - Call out any layer confusion or trap **specific to this chunk** right here
     (citing concrete examples only after or alongside stating them in full).
2. **Immediate Worked Examples & Cross-Connections (`pp. ...`)**
   - State the **full problem/claim** cleanly (exact quantifiers, sets, and
     hypotheses — zero cryptic shorthand).
   - **Connection check (*"Why not use a previous trick?"*):** Briefly test or
     explain how prior chunks relate to this problem — either showing the exact
     algebraic/logical block where an earlier method stalls, or noting where an
     earlier trick handles a sub-step directly.
   - **The Key Move (1 sentence):** State the single anchor leap or setup trick
     that unlocks the entire solution.
   - **Step-by-step solution (zero split attention):**
     - For **testing/disproving/diagnosing** (counterexample search, broken
       induction link, invalid argument): walk backwards from the failure
       condition or pinpoint the exact index/assignment where the step breaks
       (e.g., tracing $k=1$ explicitly).
     - For **forward proofs/derivations**: present multi-step arguments in a
       `Step | Formula / Expression | Why / Sub-goal` table with zero skipped
       steps so reasoning stays adjacent to every line of math.
   - If the notes leave an exercise unproved (stating only the claim), label
     the completed proof clearly as completing the stated class exercise.

#### Final 48-Hour Consolidation (Only After All Chunks Are Complete, `pp. ...`)

- **Trigger-to-Action Matrix:** Compact table mapping exam cues to methods
  across Chunks `1..N` (`Problem Cue | Choose Method | Reject / Why Earlier Tool Fails | Key Move`).
- **Two-Bucket Error-Trap Checklist:** Separate **Type A (Conceptual / Hypothesis Traps)**
  (e.g., missing $\gcd(p,q)=1$, untested first link $k=n_0$) from **Type B (Execution / Index / Sign Slips)**
  (e.g., algebra typo, De Morgan flip on $\lor \to \land$, wrong base index),
  anchored to the examples already solved above.
- **90-Second Cold-Recall Check (No Notes):** 3–5 specific definitions,
  anchors, or templates the learner should be able to reproduce on a blank
  scratch page before moving to the next unit *(lists blank-page retrieval
  targets only — not unrequested homework problem sets)*.

### Formatting & Restraint Rules

- **No future spoilers:** Do not append material from later stages when the user
  asked for one topic only.
- **No unrequested quizzes:** When the user asks to clear confusion with a full
  structured guide, deliver the complete guide cleanly without tacking on
  unrequested homework questions (use the 90-Second Cold-Recall targets or
  collapsed HTML self-checks instead).
- **Exact citations:** Only state definitions, examples, page numbers, and
  counterexamples actually present in the read notes.

---

### Step 3: Optional Export to Offline HTML in `Final_rev/`

When the user asks to save the revision guide as an HTML file in `Final_rev/`:

1. Match the base layout and styling conventions of
   [Logic_Revision.html](../../../Final_rev/Logic_Revision.html):
   - Sticky left sidebar (`Sections` + links back to `Readable_notes.html#pdf-page-...`
     and the relevant `Part_0X` Markdown file).
   - Main `.card` sections matching the **interleaved chunk structure**: each
     chunk gets its own `.card` containing a `.triage` / `.page-tag` badge,
     Exam Cue + short theory + `.callout.warn` / `.callout.good` (when needed
     for that chunk) + immediate fully-specified `.example` blocks with
     *"Why not use a previous trick?"* bridges and **The Key Move** highlight,
     followed by one final 48-Hour Consolidation `.card` at the bottom.
   - Support **Cover-and-Recalc / Faded Active Recall** cleanly in HTML using
     collapsed `<details>` blocks inside worked examples or the Cold-Recall
     section (e.g., `<details><summary>Cover-and-Recalc: check the Key Move / step</summary>...</details>`),
     so fast initial reading stays uncluttered while pre-exam self-testing works
     in one click.
   - Use `.page-tag` pills, `.grid-3` mini cards where helpful, and `@media print`
     rules (open or clearly printable).
   - Link the local KaTeX stylesheet via
     `../Post_midsem_exam_prep_2026-11-25/Readable_notes/vendor/katex/katex.min.css`.
2. Wrap all inline math in `<span class="math-source" data-display="false">...</span>`
   and display math in `<div class="math-source" data-display="true">...</div>`
   (do not put `<span>` or `<div>` inside `.math-source`).
3. Pre-render all math statically and verify zero parse errors and zero broken
   links using the bundled helper script:

   ```powershell
   node ./.agents/skills/mfocs-structured-revision/scripts/prerender_katex.cjs ./Final_rev/<Topic>_Revision.html
   ```

4. Confirm the script reports `"leftover_math_source": 0`, `"css_exists": true`,
   and all `href` targets exist.
