# Poster Prerequisite Dossier

## Purpose

This document defines what must be true before we build the poster. The goal is not to make a decent coursework poster. The goal is to produce the strongest poster we can justify against the marking criteria: content mastery, visual clarity, oral delivery, and Q&A readiness.

Topic: **Deep Double Descent: Where Bigger Models and More Data Hurt**

Primary reference:
- Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, Ilya Sutskever. *Deep Double Descent: Where Bigger Models and More Data Hurt*. arXiv:1912.02292. https://arxiv.org/abs/1912.02292

Supporting context:
- OpenAI overview: https://openai.com/index/deep-double-descent/
- Belkin et al. *Reconciling modern machine learning practice and the bias-variance trade-off*. https://arxiv.org/abs/1812.11118
- Zhang et al. *Understanding deep learning requires rethinking generalization*. https://arxiv.org/abs/1611.03530
- COMP34312 course notes, especially sections on risk decomposition, double descent, overparameterized linear regression, implicit regularization, and Rademacher complexity.

## Non-Negotiable Coursework Constraints

- Group of 3.
- One poster PDF must be submitted.
- The poster is presented in person for 15 minutes.
- Poster, oral presentation, and Q&A are all graded.
- Everyone in the group gets the same score.
- The topic must be related to lectures but not just material already covered in lectures.
- If generative AI is used, its usage must be declared.
- Difficulty tier does not create a higher grade ceiling. The correct strategy is mastery and clarity, not unnecessary difficulty.
- If a theorem or lemma is included as a central result, the proof must be presentable, and any invoked proof results must also be explainable.

## Format Assumption

The coursework specification allows PowerPoint, Google Slides, or LaTeX. The local official UoM template is a LaTeX `beamerposter` template with:

```tex
\usepackage[orientation=portrait,size=a2,scale=1.4,debug]{beamerposter}
```

Therefore the default production target is:

- A2 portrait.
- Single-page PDF.
- Large-screen readable.
- No debug grid in the final.
- Vector figures wherever possible.
- No low-resolution screenshots unless unavoidable and visually clean.

Important local limitation: this machine currently does not have `pdflatex`, ImageMagick, or Ghostscript installed. We can still design the source locally, but serious PDF compilation and screenshot iteration will need Overleaf, a TeX install, or another rendering pipeline.

## The Rubric, Converted Into Requirements

### 1. Master the Content

The poster must prove that the group understands the reference beyond summary level.

Visible poster evidence:
- A precise statement of the central question: why can larger or longer-trained deep models generalize better after interpolation?
- Clear definitions of test error, train error, interpolation threshold, overparameterized regime, and effective model complexity.
- The paper's goal, empirical method, key findings, and conclusion.
- The difference between model-wise, epoch-wise, and sample-wise double descent.
- A critical limitations block.

Speaker evidence:
- Every member can explain every figure, axis, definition, and claim.
- Every member can explain why this is not just a repeat of the lecture notes.
- Every member can explain the mechanism hypothesis without pretending it is fully solved.

Failure modes:
- Poster just says "double descent exists."
- Poster merely copies the OpenAI article.
- Poster repeats COMP34312 section 5.3 without deeper material.
- One person understands the technical content and the others only memorize a section.

### 2. Critical Thinking

The poster must include original evaluation, not just exposition.

Required critical angles:
- Classical bias-variance intuition is incomplete, not simply false.
- Parameter count is not the same thing as effective capacity.
- The interpolation threshold is the danger zone, but it is not always exactly "parameters equals samples."
- Label noise amplifies the effect but is not the whole phenomenon.
- Early stopping and regularization can suppress or avoid the effect.
- Effective model complexity is a useful unifying idea, not a complete theorem for deep networks.
- The mechanism in deep nets remains open.

Claims to avoid:
- "Bigger is always better."
- "More data is bad."
- "Double descent disproves bias-variance."
- "Overfitting is good."
- "SGD implicit bias fully explains deep double descent."
- "The peak occurs exactly when parameter count equals sample count."

### 3. Contextual Awareness

The poster must connect the paper to modern ML.

Required context:
- Modern deep networks often interpolate training data while still generalizing.
- This challenges the old practical warning that very expressive models necessarily generalize worse.
- The paper broadens double descent from a model-size story to a training-procedure and dataset-size story.
- The practical message is not "ignore validation"; it is "avoid or understand the critical regime."
- This connects to implicit regularization, benign overfitting, and why classical capacity measures are insufficient.

### 4. Design for Clarity

The poster is a visual explanation, not a compressed essay.

Design requirements:
- One clear reading order.
- 5-7 content blocks total.
- Strict two-column A2 portrait grid unless a full-width top visual is clearly better.
- Main visual in the upper or middle visual path.
- References small and at the bottom.
- No block should look like pasted lecture notes.
- Each figure caption must state the conclusion, not merely describe the figure.
- Every graph must have readable axes, labels, and regime annotations.
- The viewer should understand the main message in under one minute.

Typography targets:
- Title: roughly 1-2 lines.
- Body: do not go below readable A2 body size except references.
- References: small is acceptable.
- Text density target: approximately 450-750 words, adjusted downward if equations and figures are dense.
- Bullets preferred over paragraphs.
- 3-5 bullets per block.
- 1-2 lines per bullet.

Spacing requirements:
- No overlapping text, equations, figures, or captions.
- No cramped axis labels.
- No blocks touching page edges.
- Consistent margins and gutters.
- Enough whitespace that the poster feels intentionally composed.

## Exact Intellectual Scope

### What The Poster Must Say

Central thesis:

> Deep double descent is not just a larger-model curve. It is a broader phenomenon across model size, training time, and sample size, organized around the critical regime where the training procedure is just able to fit the data.

Essential claims:
- The classical U-shaped risk curve is a useful baseline but incomplete.
- Test error can show a second descent after the interpolation threshold.
- Double descent appears model-wise, epoch-wise, and sample-wise.
- Effective model complexity is the paper's proposed unifying lens.
- Around the interpolation threshold, fitting noise or misspecification can damage global structure.
- Far into the overparameterized regime, many interpolating solutions may exist, and SGD may find solutions that generalize better.
- This mechanism is plausible and experimentally supported, but not a solved theory for deep networks.

### What The Poster Must Not Become

It must not become:
- A general poster about bias-variance only.
- A general poster about overfitting only.
- A survey of all generalization theory.
- A theorem/proof poster.
- A copied OpenAI explainer.
- A plot gallery without explanation.
- A dense wall of equations.

## Required Figures

Minimum figure set:

1. **Classical vs double descent curve**
   - Shows textbook U-shape beside or overlaid with second descent.
   - Purpose: hook and lecture baseline.

2. **Main model-wise double descent figure**
   - Test error vs model size or effective model complexity.
   - Train error included or indicated.
   - Underparameterized, interpolation threshold, and overparameterized regimes labelled.
   - This is the poster's central visual.

3. **Effective model complexity schematic**
   - Shows that the critical regime is approximately when effective model complexity matches sample count.
   - Must not imply EMC is only raw parameter count.

4. **Three modes panel**
   - Model-wise: varying model size.
   - Epoch-wise: varying training time.
   - Sample-wise: varying dataset size can locally hurt near the critical region.

5. **Mechanism diagram**
   - Near threshold: few fitting solutions, noisy labels distort structure.
   - Far overparameterized: many fitting solutions, SGD may find a simpler/better one.

Optional if space allows:
- A compact practical implication graphic: avoid the critical regime with validation, regularization, early stopping, or sufficient scale.

## Required Equations

Use only equations that compress meaning.

Candidate equations:

```tex
R(f) = \mathbb{E}_{(x,y)}[\ell(y, f(x))]
```

Purpose: anchors population/test risk.

```tex
\widehat{R}(f) = \frac{1}{n}\sum_{i=1}^{n}\ell(y_i, f(x_i))
```

Purpose: anchors training/empirical risk.

```tex
\text{critical regime:}\quad \mathrm{EMC}(\mathcal{T}) \approx n
```

Purpose: gives the main paper lens. Here `\mathcal{T}` means the full training procedure, not just the architecture.

```tex
R(\hat f)-R(f^\star)
  \approx \text{optimization}+\text{estimation}+\text{approximation}
```

Purpose: connects to course notes without redoing the lecture.

Do not include a theorem unless we are prepared to present its proof.

## Poster Block Architecture

Recommended A2 portrait structure:

1. **Title**
   - Working title: "Deep Double Descent: When Bigger Models and More Data Can Hurt"
   - Subtitle or one-line thesis: "The risk peak is tied to the interpolation threshold, not raw size alone."

2. **The Classical Story Breaks**
   - Classical U-shape.
   - Why interpolation should look dangerous.
   - One sentence: the lecture introduced this; we go deeper into where and why the peak appears.

3. **The Paper's Core Observation**
   - Main model-wise double descent plot.
   - Train/test error.
   - Mark interpolation threshold.

4. **Effective Model Complexity**
   - Define EMC as depending on model, optimizer, training time, data, labels, and regularization.
   - Critical regime: EMC near sample count.
   - Explain why raw parameter count is insufficient.

5. **Three Ways Double Descent Appears**
   - Model-wise.
   - Epoch-wise.
   - Sample-wise.
   - One compact panel with concise captions.

6. **Why Might This Happen?**
   - Few interpolating solutions near threshold.
   - Many interpolating solutions far beyond threshold.
   - SGD implicit bias may find better/simple solutions.
   - State that this is an explanation, not a complete proof.

7. **Critical View and Implications**
   - Limitations and assumptions.
   - What not to conclude.
   - Practical message: avoid the critical regime; validate, regularize, early stop, or scale carefully.

8. **References**
   - Nakkiran et al.
   - OpenAI overview.
   - Belkin et al.
   - Zhang et al. if used.

## Fifteen-Minute Presentation Architecture

The poster must support a unified 15-minute group presentation, roughly 5 minutes per member.

Speaker 1: problem and setup.
- Classical bias-variance intuition.
- Risk/train/test definitions.
- Interpolation threshold.
- Why the phenomenon is surprising.

Speaker 2: paper evidence.
- Model-wise double descent.
- Epoch-wise double descent.
- Sample-wise non-monotonicity.
- Effective model complexity as the organizing lens.

Speaker 3: mechanism, critique, implications.
- Why the critical regime may be bad.
- Why overparameterized models may recover.
- Limitations and open questions.
- Practical meaning for deep learning.

Requirement:
- Each speaker must be able to answer questions on the whole poster, not only their section.

## Q&A Preparation Requirements

Every member must be able to answer:

1. What is new beyond the lecture notes?
2. What is the interpolation threshold?
3. What is effective model complexity?
4. How is EMC different from parameter count?
5. Does double descent contradict bias-variance?
6. Does double descent mean bigger is always better?
7. Why can more data locally hurt?
8. Why can training longer eventually help after overfitting?
9. What role does label noise play?
10. What role does SGD or implicit bias play?
11. Is the mechanism proven for deep networks?
12. What are the paper's main limitations?
13. What should a practitioner do with this knowledge?
14. Why did we choose this topic instead of a proof-heavy one?
15. What would make our explanation wrong or incomplete?

Answer policy:
- If we know, answer precisely.
- If uncertain, state the uncertainty and reason from definitions.
- Never invent a theorem, proof, or empirical result.

## Review Agents For Iteration

Each poster iteration must be reviewed through four roles:

1. **Marker**
   - Would this earn marks for mastery, critique, context, clarity, delivery, and Q&A?

2. **Designer**
   - Can the main message be scanned in under one minute?
   - Is it beautiful, readable, and non-overlapping?

3. **Hostile Examiner**
   - Where are the unsupported claims?
   - Which axis, definition, or assumption could be attacked?
   - Are we overclaiming?

4. **Presenter**
   - Can three people talk from this for 15 minutes without notes?
   - Does the poster cue the story rather than contain the full script?

## Recursive Iteration Workflow

Each cycle:

1. Produce or update poster source.
2. Compile/render to PDF.
3. Render screenshot or high-resolution preview.
4. Review visually and intellectually.
5. Log issues.
6. Fix the highest-impact problems first.
7. Repeat.

Minimum required passes:

1. **Content pass**
   - Are the claims true?
   - Is the scope right?
   - Is the poster beyond lecture material?

2. **Rubric pass**
   - Does every marking criterion have visible evidence?
   - Is Q&A readiness built in?

3. **Design pass**
   - Is there overlap?
   - Is text readable?
   - Are figures clean?
   - Is the hierarchy obvious?

4. **Hostile Q&A pass**
   - What would the marker challenge?
   - Are the answers on the poster or in speaker prep?

5. **Presentation pass**
   - Can the group deliver in 15 minutes?
   - Are transitions natural?
   - Is participation balanced?

6. **Final polish pass**
   - References correct.
   - AI-use declaration handled.
   - PDF opens cleanly.
   - No debug artifacts.
   - No template filler.
   - No hidden junk from old drafts.

## Production Baseline Now In The Repo

The current build path is no longer only a specification. We now have:

- `poster/build_poster.py`: ReportLab source for a one-page A2 portrait poster.
- `poster/deep-double-descent-poster.pdf`: generated poster artifact.
- `poster/assets/Intro-ocean-test.png`: main Nakkiran et al. paper figure for model-wise and epoch-wise evidence.
- `poster/assets/NLP-small-data-vary-MDD.png`: paper figure for sample-wise non-monotonicity.
- `poster/assets/errorvscomplexity.png`: paper intro figure available as backup.
- `poster/presentation-and-qa.md`: 15-minute presentation split and Q&A bank.

The production toolchain is ReportLab rather than LaTeX because the local machine did not have `pdflatex`. This is acceptable for producing a valid PDF, but it means final design quality must be checked by rendered previews rather than LaTeX layout conventions.

## Definition Of Done Before Submission

The poster is not final until all of these are true:

- Group member names have replaced the title placeholder.
- AI-use declaration wording has been checked against the coursework policy.
- The poster PDF opens cleanly as a single A2 portrait page.
- No text, figure, title, caption, or footer overlaps in the rendered preview.
- Every scientific claim on the poster can be defended from the reference paper or course context.
- Every graph has a clear source, axis meaning, and spoken interpretation.
- The poster shows at least one concrete paper experiment, not only conceptual cartoons.
- The poster visibly covers understanding, critical thinking, contextual awareness, clarity, visuals, and implications.
- The presentation notes let three speakers talk for roughly 5 minutes each without section silos.
- The Q&A bank covers the most likely hostile questions.

## Current Risks In The Repository

- Most coursework PDFs, sample posters, notes, and generated poster files are untracked.
- `.DS_Store` is untracked and should not be committed.
- `second-group-meeting-topic-selection.md` contains visible escaped revision markers at the bottom.
- Local LaTeX compilation is unavailable; final PDF is generated through Python/ReportLab.
- Group names are still placeholders unless `GROUP_MEMBERS` is passed to the build command.
- The AI declaration exists but may need exact module-specific wording.
- The poster uses adapted paper figures; attribution must remain visible.

## Immediate Next Steps

1. Add the paper-specific sample-wise figure to the evidence panel.
2. Rebuild the poster PDF.
3. Render a high-resolution preview and inspect actual spacing/readability.
4. Run one final hostile marker/design review.
5. Apply final fixes.
6. Insert exact group names and final AI declaration wording.
