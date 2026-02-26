# Second Group Meeting — Topic Selection

## Context

COMP34312 Mathematical Topics in Machine Learning — Poster Coursework.

Group of 3 picks a reference paper (related to lectures but not covered in them), makes a poster, does a 15-minute presentation, and handles Q&A. The poster, oral presentation, and Q&A are all graded. Everyone in the group gets the same score.

**Notification deadline:** 27th March
**Presentation date:** 8th May

---

## How We're Graded (from How-To-Score-High PDF)

4 criteria:

1. **Master the Content**
   - (a) **Understanding** — every member deeply understands goals, methods, conclusions
   - (b) **Critical Thinking** — original insights on assumptions, strengths, limitations
   - (c) **Contextual Awareness** — broader impact and implications of the research

2. **Design for Clarity**
   - (a) **Organization** — well-organized layout
   - (b) **Conciseness** — precise wording, equations over words wherever possible
   - (c) **Visuals** — relevant graphs, diagrams, charts

3. **Deliver a Balanced Oral Presentation** (15 minutes)
   - (a) **Equal Participation** — all members contribute equally
   - (b) **Confidence** — present without relying on notes
   - (c) **Engagement** — capture the marker's interest

4. **Excel at Question Handling**
   - (a) **Thoughtful Accuracy** — answer accurately and in depth
   - (b) **Active Engagement** — treat questions as discussion; own up if you don't know
   - (c) **Team Readiness** — all members prepared to answer; collective understanding assessed

---

## What the Course Covers (OFF-LIMITS for the poster)

From the COMP34312 lecture notes, the course covers:

1. Foundations of supervised learning (risk, empirical risk, Bayes model, generalization gap)
2. Probabilistic view of learning (MLE, loss functions from probability assumptions)
3. Bias-variance tradeoff
4. Combining multiple models / ensembles
5. Sources of risk, double-descent phenomenon (introduced but not deeply)
6. PAC learning
7. Math toolkit (Lipschitz, convexity, smoothness, convergence, spectral norms)
8. Formal intro to gradient descent (convergence proof)
9. GD in overparameterized linear regression
10. Rademacher complexity (definition + elementary bounds)

The poster topic must be **related to but not covered in** the lectures.

---

## Topic Difficulty Tiers (from coursework spec)

The suggested references are labelled:

- **[CORE]** — could have been covered in a few additional lecture sessions
- **[INTERMEDIATE]** — slightly more involved ideas than what's taught
- **[CHALLENGING]** — requires learning significantly new concepts beyond the lectures

> **Important:** Selecting a CHALLENGING reference does NOT guarantee higher grades, and choosing CORE does NOT restrict what grades you can achieve. Difficulty tier does not affect grade ceiling.

**Our approach:** Go CORE. Maximize grade by picking a topic all 3 members can deeply master, not by picking something hard.

---

## Topic Analysis

### Strategy

Since difficulty tier doesn't affect scoring, the ideal topic is:
- CORE difficulty (manageable for all 3 members)
- Rich enough for 15 minutes + visuals
- Strong on criteria 1(b) Critical Thinking and 1(c) Contextual Awareness
- All members can confidently handle Q&A on the full topic

### Why some CORE topics were deprioritized

**Proof-heavy topics** (GD convergence, Nesterov Level 1, Sub-Gradient Descent, SGD for Strongly Convex, Step-Length for GD Level 1, Algorithmic Stability):
- The coursework spec requires that if a theorem is suggested, its proof AND proofs of all invoked results must be presented
- Makes criteria 1(b) harder — less room for "original insights on assumptions and limitations" when walking through known proofs
- Makes criteria 3(c) harder — presenting proofs for 15 minutes in an engaging way is difficult
- Makes criteria 4 riskier — if any member can't reconstruct a proof step under pressure, it shows

**MLE and MAP:**
- Chapter 2 already covers MLE in depth. Topic is borderline — hard to "go beyond just summarizing" (criterion 1) when the marker already teaches this material

**AdaBoost:**
- Criterion 1(c) is harder — "broader impact and implications" angle is thinner compared to topics that challenge fundamental assumptions

**KNN in high-dimensions:**
- Decent topic but narrower "broader impact" (1c) — it's about a specific failure mode of a specific algorithm

**Deep-learning optimizers (survey of SGD, Adam, etc.):**
- **Strength:** Easy to split work (criterion 3a), strong on broader impact (1c), natural chronological narrative structure
- **Weakness:** Breadth over depth — hard for all 3 members to deeply understand ALL algorithms (1a). Poster conciseness suffers with 8+ update rules (2b). Q&A risk — if algorithms are split between members, knowledge is siloed, but marker assesses collective understanding (4c). Risk of repetitive "here's the problem with X, so Y was proposed" structure (3c)
- Optimizes for "easy to split workload" at the cost of criteria that actually get marked

**Causal ML:**
- Requires learning substantially new concepts not in the course — more work for criterion 1(a) with no scoring benefit

---

## Our Rankings

### 1st Choice: Double-Descent Phenomenon in Deep Learning

**Reference:** [OpenAI Deep Double Descent](https://openai.com/index/deep-double-descent/) + [detailed paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74)

**Why it's #1:**

- **1(b) Critical Thinking:** The paper challenges classical ML wisdom (bias-variance tradeoff breaks down in overparameterized models). A paper that *challenges a known idea* gives a natural structure to critique: what assumptions does it rely on? When does the argument break? Does it always hold? Much easier to generate "original insights" compared to a paper that just presents an algorithm.
- **1(c) Contextual Awareness:** Directly connects to the biggest question in modern ML: why do massively overparameterized deep networks generalize? Huge, relevant, ongoing research question. Broader impact is easy to articulate.
- **2(c) Visuals:** Naturally strong plots — the U-shaped classical curve vs the double-descent curve, test error vs model complexity graphs.
- **Builds on course:** Section 5.3 of the course introduces double-descent but doesn't go deep. The poster would go into the full paper — clearly "related but not covered."
- **Q&A:** All 3 members study the same single concept, so any member can field any question (criterion 4c).

### 2nd Choice: Momentum Gradient Descent

**Reference:** [Distill.pub — Why Momentum Really Works](https://distill.pub/2017/momentum/)

**Why it's #2 (and not Reconciling bias-variance):**

Reconciling bias-variance (arxiv 1812.11118) is very similar in flavour to double-descent — both are about "overparameterized models shouldn't work but they do." If the group rejects double-descent, it's likely because they don't want that type of topic. Pitching a near-duplicate wastes a pick.

Momentum GD is a **completely different kind of topic** — more visual, more algorithmic, "here's how something works" rather than "here's why something is surprising." Gives a genuinely different pitch if double-descent doesn't land.

- **3(b) Confidence + 3(c) Engagement:** The distill.pub article is interactive and visual by nature, giving strong poster design material. The concept (adding momentum to GD) is intuitive enough that all members can explain confidently without notes.
- **2(c) Visuals:** Distill.pub is famous for visual explanations — direct inspiration for poster design.
- **Weakness:** Criterion 1(b) is weaker — less to "critique." Momentum works, here's why. Less natural critical angle compared to double-descent.

### 3rd Choice: Reconciling Modern ML Practice and the Bias-Variance Tradeoff

**Reference:** [arxiv 1812.11118](https://arxiv.org/abs/1812.11118)

**Why it's #3:**

Fallback if the group likes the direction of double-descent but wants a slightly different paper. Same strengths on criteria 1(b) and 1(c). But since it's so similar to #1, it's the backup rather than the alternative.

### Honourable mention: Understanding Deep Learning Requires Rethinking Generalization

**Reference:** [arxiv 1611.03530](https://arxiv.org/abs/1611.03530)

Similar strengths to double-descent and reconciling bias-variance — challenges conventional wisdom, great for critical thinking, clear broader impact. A strong 4th option.

---

## Summary Table

| Criterion | Double-Descent | Momentum GD | Reconciling B-V | Optimizers Survey |
|---|---|---|---|---|
| 1(a) Understanding | Deep on one idea | Deep on one idea | Deep on one idea | Spread thin |
| 1(b) Critical thinking | Strong — challenges assumptions | Weaker — less to critique | Strong — challenges assumptions | Compare/contrast only |
| 1(c) Broader impact | Strong | Moderate | Strong | Strong |
| 2(b) Conciseness | Focused | Focused | Focused | Hard — too many algorithms |
| 2(c) Visuals | Strong (curves) | Strong (distill.pub) | Strong (curves) | Decent |
| 3(a) Work splitting | Needs coordination | Needs coordination | Needs coordination | Easy and natural |
| 3(c) Engagement | Strong narrative hook | Visual/intuitive | Strong narrative hook | Risk of repetition |
| 4(c) Team readiness | All study same thing | All study same thing | All study same thing | Siloed knowledge risk |
<\!-- revision 0 -->
<\!-- revision 1 -->
<\!-- revision 2 -->
<\!-- revision 3 -->

<\!-- revision 5 -->
<\!-- revision 6 -->
<\!-- revision 7 -->
<\!-- revision 8 -->
<\!-- revision 9 -->
<\!-- revision 10 -->
<\!-- revision 11 -->

<\!-- revision 13 -->
<\!-- revision 14 -->
<\!-- revision 15 -->
<\!-- revision 16 -->
<\!-- revision 17 -->
<\!-- revision 18 -->
<\!-- revision 19 -->

<\!-- revision 21 -->
<\!-- revision 22 -->
<\!-- revision 23 -->
<\!-- revision 24 -->
<\!-- revision 25 -->
<\!-- revision 26 -->
<\!-- revision 27 -->

<\!-- revision 29 -->
<\!-- revision 30 -->
<\!-- revision 31 -->
<\!-- revision 32 -->
<\!-- revision 33 -->
<\!-- revision 34 -->
<\!-- revision 35 -->

<\!-- revision 37 -->
