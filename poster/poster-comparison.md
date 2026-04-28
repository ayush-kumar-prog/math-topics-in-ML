# Comparison: `deep-double-descent-poster.pdf` vs `poster.pdf`

## Files Compared

- Current generated landscape poster: `poster/deep-double-descent-poster.pdf`
- Alternative LaTeX poster: `poster/poster.pdf`
- Source for alternative poster: `poster/poster.tex`

## Executive Verdict

`poster/poster.pdf` is the stronger final-submission base.

The landscape poster is cleaner and easier to scan, but it is too shallow for maximum marks. `poster/poster.pdf` is more intellectually serious, more defensible in Q&A, and much closer to what the rubric rewards under "Master the Content", "Critical Thinking", and "Question Handling".

The best final poster should be based on `poster/poster.pdf`, with polish from the landscape version:

- fewer AI-looking dashes and phrases,
- slightly less text density,
- clearer visual entry point,
- a tighter final AI declaration,
- rehearsal notes aligned to its actual block order.

## Format And First Impression

### `deep-double-descent-poster.pdf`

Strengths:

- A2 landscape works well for wide heatmaps.
- Cleaner and less intimidating.
- Has a useful Objective / Problem / Approach / Contribution strip.
- Main test/train heatmaps are easy to see.
- Looks less like a text wall.

Weaknesses:

- Feels simplified compared with the provided sample posters.
- Mathematical content is thin.
- Some sections feel like an executive summary rather than a mathematical poster.
- It does not show the course decomposition or the formal hypothesis.
- It is safer visually, but less impressive academically.

### `poster/poster.pdf`

Strengths:

- Looks like a real mathematical/scientific poster.
- Uses the official portrait-style academic structure.
- Contains a clear thesis, course bridge, definitions, hypothesis, evidence, mechanism, limitations, and practical implications.
- Much stronger for Q&A.
- Closely matches the style of `Poster-Information.pdf`, `Poster-LMC.pdf`, and `Poster-Burgers.pdf`: dense but structured, with equations and evidence.

Weaknesses:

- More text dense.
- Some body text may be small on a screen.
- Uses several en dash/em dash style constructions, which can read as AI-generated or overly polished.
- AI declaration is a bit too explicit/awkward in phrasing.
- The title area is less visually branded than the sample posters.

## Rubric Comparison

### 1. Master The Content

Winner: `poster/poster.pdf`

Reason:

- It includes the lecture decomposition and connects to course notation.
- It defines effective model complexity more formally.
- It states the Generalised Double Descent Hypothesis with three regimes.
- It includes paper setup details: ResNet18, CIFAR-10, label noise, Adam, width ranges, 4k epochs.
- It distinguishes empirical result from theorem.

The landscape poster has the right idea, but it does not prove mastery as strongly.

### 2. Critical Thinking

Winner: `poster/poster.pdf`

Reason:

- It has a full "What we do not claim" block.
- It explicitly says EMC is not a finished theory.
- It distinguishes label noise as an amplifier rather than the sole cause.
- It names where results are rigorous only for linear models.

The landscape poster has a critical view, but it is less specific.

### 3. Contextual Awareness

Winner: `poster/poster.pdf`

Reason:

- It connects the paper to lecture notes, Belkin, Mei and Montanari, Bartlett, and Zhang.
- It includes practical messages and open scientific questions.
- It gives a better sense of where this paper sits in the literature.

### 4. Design For Clarity

Winner for scanability: `deep-double-descent-poster.pdf`

Winner for academic poster style: `poster/poster.pdf`

Reason:

- The landscape poster is easier to scan quickly.
- The portrait poster has more content but follows the dense academic sample-poster style better.
- The sample posters are not minimal. They are dense but organized, so density alone is not a failure.

Final recommendation: use `poster/poster.pdf`, but reduce clutter and polish typography if time allows.

### 5. Oral Presentation Support

Winner: `poster/poster.pdf`

Reason:

- It gives a natural 15-minute path:
  1. textbook U-curve,
  2. lecture decomposition,
  3. EMC definition and hypothesis,
  4. main evidence,
  5. sample-wise evidence,
  6. mechanism,
  7. limitations,
  8. practical message.

This is easier to divide among three speakers than the landscape poster, which compresses too many ideas.

### 6. Q&A Readiness

Winner: `poster/poster.pdf`

Reason:

- It pre-answers likely hostile questions:
  - Is this beyond the lecture?
  - What is EMC?
  - Is this a theorem?
  - Does it contradict bias-variance?
  - Is label noise the only cause?
  - Is more data bad?
  - Where is the mechanism rigorous?

## Best Final Direction

Use `poster/poster.pdf` as the final base.

Keep from `poster/poster.pdf`:

- Formal lecture decomposition.
- Definition of EMC.
- Generalised Double Descent Hypothesis.
- Main empirical evidence block.
- Sample-wise figure and explanation.
- Mechanism block.
- "What we do not claim."
- Practical message and open questions.

Borrow from `deep-double-descent-poster.pdf`:

- The cleaner Objective / Problem / Approach / Contribution framing.
- Less AI-sounding declaration wording.
- Avoid em dashes/en dashes.
- Slightly more whitespace where possible.

## Specific Fixes Needed In `poster/poster.pdf`

1. Remove em dash/en dash style punctuation where possible.
2. Replace the AI declaration with a shorter compliant version:
   "AI tools assisted with drafting and layout. The group verified all mathematical claims and source references."
3. Consider adding a tiny Objective / Problem / Approach / Contribution strip, or make the existing thesis/beyond lecture block more visibly serve that function.
4. Reduce 5-10% of body text in the densest blocks:
   - Setting block.
   - Heatmap setup paragraph.
   - Mechanism references paragraph.
5. Keep the formal content. Do not simplify it down to the landscape poster level.
6. Run final screen-legibility check from 2 metres.

## Final Recommendation

Submit a polished version of `poster/poster.pdf`, not the current `deep-double-descent-poster.pdf`.

The landscape poster is cleaner, but the portrait LaTeX poster is much more likely to score highly because it visibly demonstrates understanding, mathematical precision, paper-specific evidence, limitations, and Q&A readiness.
