#!/usr/bin/env python3
"""Build the COMP34312 deep-double-descent poster as an A2 landscape PDF."""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path

EXTRA = Path("/tmp/codex-poster-pkgs")
if EXTRA.exists():
    sys.path.insert(0, str(EXTRA))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A2, landscape
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


OUT = Path(__file__).with_name("deep-double-descent-poster.pdf")
ASSETS = Path(__file__).with_name("assets")
PAGE_W, PAGE_H = landscape(A2)

GROUP_MEMBERS = os.environ.get("GROUP_MEMBERS", "Ayush Kumar, Jacob Yip, Harshita Dassani")

PURPLE = colors.HexColor("#5E2382")
DARK_PURPLE = colors.HexColor("#3B1457")
DARK = colors.HexColor("#17181C")
MUTED = colors.HexColor("#555A66")
BG = colors.HexColor("#E7E7E4")
LIGHT = colors.HexColor("#F7F7F5")
LINE = colors.HexColor("#BFC2C9")
BLUE = colors.HexColor("#1F5FAE")
TEAL = colors.HexColor("#087E8B")
CORAL = colors.HexColor("#D24F57")
GOLD = colors.HexColor("#D79B00")
GREEN = colors.HexColor("#27823D")
PALE_PURPLE = colors.HexColor("#F0E7F5")


@dataclass
class Box:
    x: float
    y: float
    w: float
    h: float


def text_width(text: str, font: str, size: float) -> float:
    return stringWidth(text, font, size)


def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if text_width(trial, font, size) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = "Helvetica",
    size: float = 14.0,
    leading: float | None = None,
    color=colors.black,
) -> float:
    if leading is None:
        leading = size * 1.22
    c.setFillColor(color)
    c.setFont(font, size)
    yy = y
    for line in wrap(text, font, size, width):
        c.drawString(x, yy, line)
        yy -= leading
    return yy


def bullets(
    c: canvas.Canvas,
    items: list[str],
    x: float,
    y: float,
    width: float,
    size: float = 14.0,
    leading: float = 17.2,
    color=colors.black,
    bullet_color=PURPLE,
) -> float:
    yy = y
    for item in items:
        lines = wrap(item, "Helvetica", size, width - 17)
        c.setFillColor(bullet_color)
        c.circle(x + 4, yy + 4.8, 2.5, fill=1, stroke=0)
        c.setFillColor(color)
        c.setFont("Helvetica", size)
        c.drawString(x + 15, yy, lines[0])
        yy -= leading
        for line in lines[1:]:
            c.drawString(x + 15, yy, line)
            yy -= leading
        yy -= 4
    return yy


def draw_image_fit(c: canvas.Canvas, path: Path, b: Box) -> None:
    if not path.exists():
        c.setFillColor(colors.white)
        c.rect(b.x, b.y, b.w, b.h, fill=1, stroke=0)
        c.setFillColor(CORAL)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(b.x + b.w / 2, b.y + b.h / 2, f"Missing image: {path.name}")
        return
    reader = ImageReader(str(path))
    iw, ih = reader.getSize()
    scale = min(b.w / iw, b.h / ih)
    dw, dh = iw * scale, ih * scale
    c.drawImage(reader, b.x + (b.w - dw) / 2, b.y + (b.h - dh) / 2, dw, dh, preserveAspectRatio=True, mask="auto")


def panel(c: canvas.Canvas, b: Box, title: str, color=PURPLE, title_size: float = 16.0) -> Box:
    c.setFillColor(colors.white)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.rect(b.x, b.y, b.w, b.h, fill=1, stroke=1)
    header_h = 28
    c.setFillColor(color)
    c.rect(b.x, b.y + b.h - header_h, b.w, header_h, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", title_size)
    c.drawString(b.x + 11, b.y + b.h - 20, title)
    return Box(b.x + 12, b.y + 12, b.w - 24, b.h - header_h - 22)


def rule(c: canvas.Canvas, y: float, color=PURPLE, width: float = 4.0) -> None:
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(30, y, PAGE_W - 30, y)


def draw_title(c: canvas.Canvas) -> None:
    c.setFillColor(colors.white)
    c.rect(0, PAGE_H - 145, PAGE_W, 145, fill=1, stroke=0)

    c.setFillColor(PURPLE)
    c.rect(36, PAGE_H - 104, 176, 60, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Times-Roman", 23)
    c.drawCentredString(124, PAGE_H - 72, "MANCHESTER")
    c.setFillColor(colors.HexColor("#F6D21B"))
    c.setFont("Times-Bold", 19)
    c.drawCentredString(145, PAGE_H - 92, "1824")

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 42)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 58, "Deep Double Descent")
    c.setFillColor(PURPLE)
    c.setFont("Helvetica-Bold", 23)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 89, "When bigger models, longer training, and more data can hurt")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 13)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 115, f"COMP34312 Mathematical Topics in Machine Learning | {GROUP_MEMBERS}")

    c.setFillColor(DARK_PURPLE)
    c.setFont("Helvetica-Bold", 13)
    c.drawRightString(PAGE_W - 35, PAGE_H - 54, "The University of Manchester")
    rule(c, PAGE_H - 145, PURPLE, 5.2)


def draw_short_story(c: canvas.Canvas, b: Box) -> None:
    c.setFillColor(colors.white)
    c.rect(b.x, b.y, b.w, b.h, fill=1, stroke=0)
    rule(c, b.y + b.h - 3, PURPLE, 4.0)

    rows = [
        ("Objective", "explain why test error can peak near interpolation and then fall again"),
        ("Problem", "classical U-shaped overfitting intuition is incomplete for modern interpolating models"),
        ("Approach", "compare test and train error while changing width, epochs, samples, noise, optimizer, and regularization"),
        ("Contribution", "Nakkiran et al. unify model-wise, epoch-wise, and sample-wise effects using effective model complexity"),
    ]
    yy = b.y + b.h - 34
    label_w = 112
    for label, text in rows:
        c.setFillColor(PURPLE)
        c.setFont("Helvetica-Bold", 17.5)
        c.drawRightString(b.x + label_w, yy, f"{label}:")
        c.setFillColor(DARK)
        c.setFont("Helvetica", 16.5)
        c.drawString(b.x + label_w + 16, yy, text)
        yy -= 27.5


def curve_points(x: float, y: float, w: float, h: float, f, n: int = 120) -> list[tuple[float, float]]:
    vals = [f(i / (n - 1)) for i in range(n)]
    mn, mx = min(vals), max(vals)
    pad = (mx - mn) * 0.08 or 1
    mn -= pad
    mx += pad
    return [(x + i / (n - 1) * w, y + (val - mn) / (mx - mn) * h) for i, val in enumerate(vals)]


def draw_curve(c: canvas.Canvas, pts: list[tuple[float, float]], color, width: float) -> None:
    c.setStrokeColor(color)
    c.setLineWidth(width)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    c.drawPath(p, stroke=1, fill=0)


def dd_curve(t: float) -> float:
    first = 1.10 - 0.88 * min(t / 0.43, 1)
    peak = 1.30 * math.exp(-((t - 0.53) / 0.072) ** 2)
    second = 0.28 + 0.13 * math.exp(-4.0 * max(t - 0.60, 0))
    return first + peak + second


def draw_classical_panel(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "1. The classical story is not enough", TEAL, 15.5)
    draw_wrapped(
        c,
        "Lecture 5.3 introduces the surprise. The paper asks what controls the bad regime, and why the same pattern appears when we vary width, training time, or sample count.",
        inner.x,
        inner.y + inner.h - 4,
        inner.w,
        size=14.0,
        leading=16.5,
        color=DARK,
    )
    ax = inner.x + 28
    ay = inner.y + 22
    aw = inner.w - 45
    ah = inner.h - 96
    c.setStrokeColor(colors.HexColor("#777B86"))
    c.setLineWidth(1.0)
    c.line(ax, ay, ax + aw, ay)
    c.line(ax, ay, ax, ay + ah)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 10.5)
    c.drawCentredString(ax + aw / 2, ay - 16, "model / effective complexity")
    c.saveState()
    c.translate(ax - 18, ay + ah / 2)
    c.rotate(90)
    c.drawCentredString(0, 0, "test error")
    c.restoreState()
    classical = curve_points(ax, ay, aw, ah, lambda t: 0.42 + 1.8 * (t - 0.42) ** 2)
    modern = curve_points(ax, ay, aw, ah, dd_curve)
    draw_curve(c, classical, colors.HexColor("#868B94"), 2.0)
    draw_curve(c, modern, CORAL, 3.0)
    ix = ax + 0.53 * aw
    c.setDash(4, 3)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.line(ix, ay, ix, ay + ah)
    c.setDash()
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(ix, ay + ah + 10, "interpolation")
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(ax + aw * 0.62, ay + ah * 0.70, "second descent")
    c.setFillColor(MUTED)
    c.drawString(ax + aw * 0.05, ay + ah * 0.22, "classical U-shape")


def draw_emc_panel(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "2. Mathematical anchor: effective model complexity", PURPLE, 15.0)
    c.setFillColor(PALE_PURPLE)
    c.setStrokeColor(colors.HexColor("#D5BFE2"))
    c.setLineWidth(1.0)
    c.roundRect(inner.x, inner.y + inner.h - 118, inner.w, 105, 10, fill=1, stroke=1)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(inner.x + inner.w / 2, inner.y + inner.h - 39, "critical regime:  EMC_D,eps(T) is approximately n")
    c.setFont("Helvetica-Bold", 13)
    formulas = [
        "R(f) = E_(x,y)~D [ loss(y, f(x)) ]",
        "Rhat_S(f) = (1/n) sum_i loss(y_i, f(x_i))",
        "EMC_D,eps(T) = max { m : E_{S~D^m}[train_error(T(S), S)] <= eps }",
    ]
    yy = inner.y + inner.h - 66
    for line in formulas:
        c.drawCentredString(inner.x + inner.w / 2, yy, line)
        yy -= 20
    bullets(
        c,
        [
            "T is the full training procedure: architecture, optimizer, epochs, data augmentation, labels, and regularization.",
            "The threshold is not simply parameter count equals sample count.",
            "Changing epochs or data size can move the same system into or out of the peak.",
        ],
        inner.x,
        inner.y + inner.h - 145,
        inner.w,
        size=14.0,
        leading=16.2,
        bullet_color=PURPLE,
    )


def draw_mechanism_panel(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "3. Interpretation: a local danger zone", CORAL, 15.5)
    gap = 9
    box_w = (inner.w - 2 * gap) / 3
    regimes = [
        ("EMC << n", "underfit", "more fitting ability usually helps", TEAL),
        ("EMC ~= n", "critical", "barely fits; noise or misspecification can dominate", CORAL),
        ("EMC >> n", "overparameterized", "many interpolants; optimizer bias can matter", GREEN),
    ]
    top_y = inner.y + inner.h - 92
    for i, (head, name, note, col) in enumerate(regimes):
        x = inner.x + i * (box_w + gap)
        c.setFillColor(colors.white)
        c.setStrokeColor(col)
        c.setLineWidth(1.5)
        c.roundRect(x, top_y, box_w, 78, 8, fill=1, stroke=1)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 15)
        c.drawCentredString(x + box_w / 2, top_y + 52, head)
        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(x + box_w / 2, top_y + 33, name)
        draw_wrapped(c, note, x + 8, top_y + 18, box_w - 16, size=10.5, leading=11.8, color=MUTED)
    draw_wrapped(
        c,
        "Proposed intuition, not a theorem: near the threshold, noise is costly; far beyond it, many interpolants make optimizer bias matter.",
        inner.x,
        inner.y + 46,
        inner.w,
        size=13.6,
        leading=15.0,
        color=DARK,
    )
    c.setFillColor(PALE_PURPLE)
    c.roundRect(inner.x, inner.y + 3, inner.w, 24, 6, fill=1, stroke=0)
    c.setFillColor(PURPLE)
    c.setFont("Helvetica-Bold", 13.2)
    c.drawCentredString(inner.x + inner.w / 2, inner.y + 11, "Double descent refines overfitting; it does not say overfitting is good.")


def draw_main_evidence(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "4. Main empirical evidence from Nakkiran et al.", PURPLE, 16.2)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(inner.x, inner.y + inner.h - 4, "ResNet18 on CIFAR-10 with 15% label noise")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 12.5)
    c.drawString(inner.x, inner.y + inner.h - 25, "Width and training time move the system through the same interpolation frontier.")

    test_box = Box(inner.x + 3, inner.y + 54, inner.w * 0.59, inner.h - 91)
    train_box = Box(test_box.x + test_box.w + 18, inner.y + 72, inner.w - test_box.w - 21, inner.h - 116)
    draw_image_fit(c, ASSETS / "Intro-ocean-test.png", test_box)
    draw_image_fit(c, ASSETS / "Rn-cifar10-p15-adam-aug-train.png", train_box)

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(test_box.x, inner.y + 29, "Test error: the bright ridge is the bad generalization zone.")
    c.drawString(train_box.x, inner.y + 49, "Train error companion: dashed curve marks interpolation threshold.")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 10.5)
    c.drawString(inner.x, inner.y + 8, "Adapted from Nakkiran et al. arXiv:1912.02292. Horizontal slices show model-wise double descent; vertical slices show epoch-wise double descent.")


def route_card(c: canvas.Canvas, b: Box, title: str, axis_label: str, text: str, color) -> None:
    c.setFillColor(LIGHT)
    c.setStrokeColor(colors.HexColor("#D3D4D8"))
    c.setLineWidth(0.8)
    c.rect(b.x, b.y, b.w, b.h, fill=1, stroke=1)
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(b.x + 9, b.y + b.h - 18, title)
    ax = b.x + 23
    ay = b.y + 42
    aw = b.w - 42
    ah = b.h - 76
    c.setStrokeColor(colors.HexColor("#80858E"))
    c.setLineWidth(1.0)
    c.line(ax, ay, ax + aw, ay)
    c.line(ax, ay, ax, ay + ah)
    f = dd_curve if "sample" not in axis_label else (lambda t: 0.40 + 0.25 * math.exp(-4 * t) + 0.95 * math.exp(-((t - 0.55) / 0.17) ** 2))
    draw_curve(c, curve_points(ax, ay, aw, ah, f), color, 2.5)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9.5)
    c.drawCentredString(ax + aw / 2, ay - 13, axis_label)
    draw_wrapped(c, text, b.x + 8, b.y + 20, b.w - 16, size=10.6, leading=11.8, color=DARK)


def draw_synthesis(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "5. Three routes through the same critical regime", BLUE, 15.4)
    gap = 11
    card_w = (inner.w - 2 * gap) / 3
    card_h = inner.h - 68
    cards = [
        ("Model-wise", "width", "horizontal slice of heatmap", CORAL),
        ("Epoch-wise", "epochs", "vertical slice of heatmap", TEAL),
        ("Sample-wise", "samples n", "fixed model; n can move into peak", BLUE),
    ]
    for i, args in enumerate(cards):
        route_card(c, Box(inner.x + i * (card_w + gap), inner.y + 51, card_w, card_h), *args)
    c.setFillColor(PALE_PURPLE)
    c.roundRect(inner.x, inner.y + 5, inner.w, 34, 6, fill=1, stroke=0)
    c.setFillColor(PURPLE)
    c.setFont("Helvetica-Bold", 14.2)
    c.drawString(inner.x + 9, inner.y + 17, "Unifying claim:")
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 13.0)
    c.drawString(inner.x + 124, inner.y + 17, "the peak appears when EMC_D,eps(T) and n are close.")


def draw_sample_panel(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "6. More data can locally hurt", TEAL, 15.4)
    draw_image_fit(c, ASSETS / "NLP-small-data-vary-MDD.png", Box(inner.x + 4, inner.y + 42, inner.w - 8, inner.h - 60))
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(inner.x, inner.y + 25, "IWSLT Transformer: 18k samples can be worse than 4k for some widths.")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 10.8)
    c.drawString(inner.x, inner.y + 8, "This is local non-monotonicity, not the claim that data is bad overall.")


def draw_critical_conclusion(c: canvas.Canvas, b: Box) -> None:
    inner = panel(c, b, "7. Critical view and practical message", GREEN, 15.4)
    left = Box(inner.x, inner.y, inner.w * 0.55, inner.h)
    right = Box(inner.x + inner.w * 0.58, inner.y, inner.w * 0.42, inner.h)
    bullets(
        c,
        [
            "Bias-variance is not false; the monotone overfitting story is incomplete.",
            "Bigger, longer-trained, or more-data systems can still be worse inside the critical interval.",
            "EMC is an empirical organizing lens, not a complete deep-net theory.",
        ],
        left.x,
        left.y + left.h - 8,
        left.w,
        size=13.0,
        leading=15.4,
        bullet_color=GREEN,
    )
    c.setFillColor(PALE_PURPLE)
    c.roundRect(right.x, right.y + 18, right.w, right.h - 25, 8, fill=1, stroke=0)
    c.setFillColor(PURPLE)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(right.x + right.w / 2, right.y + right.h - 16, "Takeaway")
    draw_wrapped(
        c,
        "Generalization depends on the trained system, not model size alone. Use validation, regularization, early stopping, or enough scale to avoid the peak.",
        right.x + 14,
        right.y + right.h - 45,
        right.w - 28,
        font="Helvetica-Bold",
        size=13.5,
        leading=16.0,
        color=DARK,
    )


def draw_footer(c: canvas.Canvas, b: Box) -> None:
    c.setFillColor(colors.white)
    c.rect(b.x, b.y, b.w, b.h, fill=1, stroke=0)
    c.setStrokeColor(PURPLE)
    c.setLineWidth(2)
    c.line(b.x, b.y + b.h, b.x + b.w, b.y + b.h)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(b.x + 8, b.y + b.h - 16, "References")
    c.drawString(b.x + b.w * 0.52, b.y + b.h - 16, "Declaration")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9.5)
    c.drawString(b.x + 8, b.y + b.h - 32, "Nakkiran et al. Deep Double Descent, arXiv:1912.02292. Belkin et al. PNAS 2019. Zhang et al. ICLR 2017.")
    draw_wrapped(
        c,
        "Figures adapted from Nakkiran et al. arXiv source. AI tools assisted with drafting and layout; the group retains responsibility for verifying all mathematical and source claims.",
        b.x + b.w * 0.52,
        b.y + b.h - 32,
        b.w * 0.46,
        size=9.5,
        leading=11.0,
        color=MUTED,
    )


def build() -> None:
    c = canvas.Canvas(str(OUT), pagesize=landscape(A2))
    c.setTitle("Deep Double Descent Poster")
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    draw_title(c)

    margin = 30
    gutter = 14
    story = Box(margin, PAGE_H - 292, PAGE_W - 2 * margin, 124)
    draw_short_story(c, story)

    footer_h = 49
    footer = Box(margin, 22, PAGE_W - 2 * margin, footer_h)
    draw_footer(c, footer)

    body_top = story.y - 14
    body_bottom = footer.y + footer.h + 14
    body_h = body_top - body_bottom
    col_w = (PAGE_W - 2 * margin - 2 * gutter) / 3
    x1 = margin
    x2 = x1 + col_w + gutter
    x3 = x2 + col_w + gutter
    span_w = col_w * 2 + gutter

    left_h1 = 232
    left_h2 = 264
    left_h3 = body_h - left_h1 - left_h2 - 2 * gutter
    draw_classical_panel(c, Box(x1, body_top - left_h1, col_w, left_h1))
    draw_emc_panel(c, Box(x1, body_top - left_h1 - gutter - left_h2, col_w, left_h2))
    draw_mechanism_panel(c, Box(x1, body_bottom, col_w, left_h3))

    evidence_h = 386
    draw_main_evidence(c, Box(x2, body_top - evidence_h, span_w, evidence_h))

    lower_top = body_top - evidence_h - gutter
    lower_h = lower_top - body_bottom
    mid_h = 246
    draw_synthesis(c, Box(x2, lower_top - mid_h, col_w, mid_h))
    draw_sample_panel(c, Box(x3, lower_top - mid_h, col_w, mid_h))
    draw_critical_conclusion(c, Box(x2, body_bottom, span_w, lower_h - mid_h - gutter))

    c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    build()
