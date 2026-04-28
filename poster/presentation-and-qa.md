# Deep Double Descent Presentation And Q&A Prep

## Point Of The Poster

The poster is not trying to prove a new theorem. The point is:

> Deep double descent is a structured phenomenon around the interpolation threshold. Nakkiran et al. show that the same risk peak appears when changing model width, training time, or sample count, and effective model complexity is the lens that unifies these cases.

The poster needs to convince the marker of four things:

1. We understand the classical overfitting story and why double descent is surprising.
2. We understand what Nakkiran et al. add beyond lecture 5.3.
3. We can explain the empirical evidence without overclaiming.
4. We can critique the assumptions, limitations, and implications.

## Why These Elements Are On The Poster

- **Objective / Problem / Approach / Contribution strip:** gives the whole story in under 30 seconds, matching the style of the sample posters.
- **Classical curve:** connects to the course and sets up why the result is surprising.
- **Effective model complexity definition:** the main conceptual contribution. Without this, the poster is just "look at these curves."
- **Test and train heatmaps:** the strongest paper evidence. Test error shows the bad ridge; train error shows the interpolation frontier.
- **Three-routes panel:** makes the unification clear: model-wise, epoch-wise, and sample-wise double descent are not separate stories.
- **Sample-wise figure:** supports the title claim that more data can locally hurt.
- **Critical view and takeaway:** directly addresses the rubric's critical thinking and contextual awareness criteria.

## Speaker Split

### Ayush Kumar: setup and mathematical framing

Target time: 5 minutes.

Cover:
- Title and short-story strip.
- Classical U-shaped overfitting story.
- Why lecture 5.3 is only the starting point.
- Train error, test error, interpolation threshold.
- Effective model complexity.

Core sentence:
"The paper's key move is to measure the capacity of the whole training procedure, not just raw parameter count."

### Jacob Yip: paper evidence

Target time: 5 minutes.

Cover:
- Main test-error heatmap.
- Train-error companion heatmap.
- Horizontal slices as model-wise double descent.
- Vertical slices as epoch-wise double descent.
- Sample-wise figure showing local non-monotonicity.

Core sentence:
"The same critical regime appears when we vary model size, training time, or sample count."

### Harshita Dassani: interpretation, critique, and implications

Target time: 5 minutes.

Cover:
- Three regimes: underfit, critical, overparameterized.
- Why the peak may happen.
- What not to overclaim.
- Practical implications.
- Final takeaway and Q&A framing.

Core sentence:
"Double descent refines the overfitting story; it does not say overfitting is good."

All three members must be able to answer questions on the whole poster, not only their assigned section.

## What We Are Not Going To Talk About

- We are not proving a deep-network generalization theorem.
- We are not presenting every experiment in Nakkiran et al.
- We are not giving a full survey of benign overfitting, PAC learning, Rademacher complexity, or neural tangent kernels.
- We are not deriving SGD implicit bias from first principles.
- We are not presenting the OpenAI blog as the main source.
- We are not saying bias-variance is false.
- We are not saying bigger models are always better.
- We are not saying more data is generally bad.
- We are not saying effective model complexity is a finished theory.

## What Is Deliberately Not On The Poster

- Long experimental tables.
- Every architecture, optimizer, and hyperparameter from the paper.
- Full proofs from related linear-model theory.
- Extended derivations of bias-variance or approximation/estimation decompositions.
- A literature survey of every double-descent paper.
- Dense presenter notes.
- More than a few references.

Reason: the poster is a visual tool for a 15-minute explanation. Anything that does not support the core story, the central evidence, or the likely Q&A has been cut.

## Figure-Level Talk Prompts

### Classical curve

Say:
"The grey curve is the classical U-shaped story: too simple underfits, too complex overfits. The red curve shows the modern surprise: after interpolation, test error can fall again."

Do not say:
"Bias-variance is wrong."

### Effective model complexity

Say:
"EMC is the largest sample size on which the full training procedure can reach small training error. The full procedure includes model, optimizer, epochs, labels, data augmentation, and regularization."

Likely question:
"Expectation over what?"

Answer:
"Over training samples drawn from the data distribution. It is an operational definition, not a closed-form theory."

### Main heatmaps

Say:
"The left heatmap is test error over model width and epochs. The right heatmap is train error. The dashed frontier in train error marks where the model first interpolates. The test-error ridge sits around that frontier."

Likely question:
"Does this prove the mechanism?"

Answer:
"No. It supports the empirical pattern. The mechanism remains an open theoretical problem."

### Sample-wise figure

Say:
"More data usually helps, but it also moves the interpolation threshold. For a fixed model family and training procedure, adding samples can move the system into the critical regime. That is why more data can locally hurt."

Do not say:
"More data is bad."

## Hostile Q&A Bank

### What is new beyond the lecture notes?

Lecture 5.3 introduces double descent. Nakkiran et al. extend it across model size, training time, and sample count, and propose effective model complexity as the unifying lens.

### Does double descent contradict bias-variance?

No. It contradicts the oversimplified monotone story that more capacity must keep worsening test error after interpolation.

### What exactly is the interpolation threshold?

The point where the training procedure first becomes able to fit the training data, usually seen when train error approaches zero.

### Why include train error?

Because the claim is not just that test error has a ridge. The claim is that the ridge aligns with the interpolation frontier.

### Is EMC the same as parameter count?

No. Parameter count is one input. EMC also depends on optimizer, training time, regularization, data, and labels.

### What role does label noise play?

Label noise makes the peak more visible because fitting noise is damaging near interpolation. But the broader claim is not only about label noise.

### What should a practitioner do?

Use validation. Avoid blindly operating near the critical regime. Regularization, early stopping, more scale, or different data/model choices can move the system away from the peak.

### What is the biggest limitation?

The mechanism is not a complete theorem for real deep networks. EMC organizes the evidence, but it is not a finished predictive theory.
