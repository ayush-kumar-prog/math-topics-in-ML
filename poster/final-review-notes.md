# Final Poster Review Notes

## Current Artifact

- Poster PDF: `poster/deep-double-descent-poster.pdf`
- Source: `poster/build_poster.py`
- Format: A2 portrait, one page.
- Main topic: Deep double descent via effective model complexity.
- Central evidence: Nakkiran et al. ResNet18/CIFAR-10 heatmap plus sample-wise IWSLT Transformer inset.

## Review Passes Completed

- Repository/coursework/rubric inspection.
- Prerequisite dossier created and updated.
- Presentation and Q&A prep created and expanded.
- Visual review pass: layout, hierarchy, font size, footer, and chart clarity.
- Hostile marker pass: factual defensibility, overclaim risk, source attribution, EMC precision, and Q&A risk.
- Rendered-preview inspection using `qlmanage`.
- Mechanical PDF check using `pypdf`: one page, A2 dimensions, expected text present.

## Issues Fixed In The Latest Iteration

- Replaced generic/top-heavy draft with a clean A2 layout.
- Added a dominant paper-specific empirical figure.
- Added source/context caption for the main heatmap.
- Added explicit "what the paper did" content.
- Hardened effective model complexity notation:
  `EMC_D,eps(T) = max{m : E_{S~D^m}[train_error(T(S), S)] <= eps}`.
- Labelled the sample-wise inset as schematic/digitized from Nakkiran et al.
- Reworded the mechanism as the paper's proposed intuition, not a theorem.
- Added a final-style AI declaration.
- Expanded presentation prep with figure-level explanations and hostile follow-ups.

## Remaining Human Inputs

1. Replace `Name 1, Name 2, Name 3` with the exact group member names.
2. Confirm the final AI declaration wording is acceptable for the module.
3. Have each group member rehearse all three figure explanations, not only their own section.
4. Confirm whether the marker expects direct figure numbers; current poster attributes by source rather than paper figure number.

## Build Command

```bash
GROUP_MEMBERS="Person One, Person Two, Person Three" PYTHONPATH=/tmp/codex-poster-pkgs python3 poster/build_poster.py
```

## Final Submission Risk

The current poster is a strong draft, but it should not be submitted with placeholder group names. The AI declaration is present, but the group should verify it against the exact module policy before upload.
