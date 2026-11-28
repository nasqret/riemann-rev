#!/usr/bin/env python3
"""Compute and draw every figure of the atlas (SVG), and record the numbers they show.

    python3 -B scripts/build_figures.py          # writes assets/figures/*.svg and facts.json

Each computed figure asserts the facts it displays before writing anything; a failed
assertion aborts the build. Schematic figures (chain, descent, choreography) are labelled
as such in their <desc>. The numbers quoted on the pages come from facts.json.
"""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import rhlib  # noqa: E402
from svg import (ACCENT, ANA, ARITH, Axes, DEST, EST, FAINT, GRID, INK, MONO, MOTIV, MUTED,  # noqa: E402
                 NIGHT, NUM, OK, READ, SANS, SURFACE, SURFACE_ALT, SVG, TEXT, f)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "figures"
FACTS: dict = {}


def save(name: str, svg: SVG) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.svg").write_text(svg.render(), encoding="utf-8")


def envelope(xs: np.ndarray, ys: np.ndarray, x0: float, x1: float, cols: int):
    """Min/max of ys in each of ``cols`` equal bins of [x0, x1] (faithful downsampling)."""
    idx = np.clip(((xs - x0) / (x1 - x0) * cols).astype(int), 0, cols - 1)
    lo = np.full(cols, np.inf)
    hi = np.full(cols, -np.inf)
    np.minimum.at(lo, idx, ys)
    np.maximum.at(hi, idx, ys)
    centers = x0 + (np.arange(cols) + 0.5) / cols * (x1 - x0)
    ok = np.isfinite(lo)
    return centers[ok], lo[ok], hi[ok]


def zigzag(ax: Axes, cx, lo, hi) -> str:
    pts = []
    for x, a, b in zip(cx, lo, hi):
        pts.append(f"{f(ax.X(x))},{f(ax.Y(a))}")
        pts.append(f"{f(ax.X(x))},{f(ax.Y(b))}")
    return "M" + " L".join(pts)


# =====================================================================================
# 1. Hero: the normalized centered prime sum, computed exactly up to 10^7
# =====================================================================================
def fig_hero(ps: rhlib.PrimeSums) -> None:
    y_max = 1.0e7
    ys = np.exp(np.linspace(math.log(10.0), math.log(y_max), 400_000))
    r = (ps.G(ys) - rhlib.LOG_2PI) / np.sqrt(ys)
    band = rhlib.RH_BAND
    rmax, rmin = float(r.max()), float(r.min())
    assert -band < rmin < rmax < band, (rmin, rmax, band)
    FACTS["hero"] = {"y_min": 10, "y_max": int(y_max), "samples": int(ys.size),
                     "r_max": round(rmax, 5), "r_min": round(rmin, 5),
                     "rh_band": round(band, 6),
                     "y_at_min": round(float(ys[np.argmin(r)]), 1),
                     "y_at_max": round(float(ys[np.argmax(r)]), 1)}

    W, H = 1500, 720
    s = SVG(W, H, "The centered prime sum, normalized",
            "Computed: (G(y) - log 2pi)/sqrt(y) for 10 <= y <= 10^7, where G(y) = sum_{n<=y} "
            "Lambda(n)(y/n-1) - y log y + (1+gamma) y. Dotted lines: +-(2+gamma-log 4pi), the band "
            "that RH forces. Shaded column: one power window [Y, Y^(3/2)], Y = 10^4, with an "
            "illustrative one-sided ceiling C y^theta (theta = 0.55) in the same normalization.", bg=NIGHT)
    s.defs.append('<filter id="glow" x="-5%" y="-30%" width="110%" height="160%">'
                  '<feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/>'
                  '<feMergeNode in="SourceGraphic"/></feMerge></filter>')
    s.defs.append('<linearGradient id="fadeL" x1="0" x2="1" y1="0" y2="0">'
                  f'<stop offset="0" stop-color="{NIGHT}" stop-opacity="1"/>'
                  f'<stop offset="0.42" stop-color="{NIGHT}" stop-opacity="0.92"/>'
                  f'<stop offset="0.62" stop-color="{NIGHT}" stop-opacity="0"/></linearGradient>')
    s.defs.append('<linearGradient id="gold" x1="0" x2="1" y1="0" y2="0">'
                  '<stop offset="0" stop-color="#fde68a"/><stop offset="0.5" stop-color="#fbbf24"/>'
                  '<stop offset="1" stop-color="#f59e0b"/></linearGradient>')
    ax = Axes(240, 110, 1200, 500, (1.0, 7.0), (-0.062, 0.062))
    # one power window [Y, Y^(3/2)] with Y = 10^4 (log10 coordinates [4, 6]) and an illustrative
    # one-sided ceiling C y^theta (theta = 0.55), drawn in normalized units C y^(theta - 1/2).
    L = 4.0
    x0, x1 = ax.X(L), ax.X(1.5 * L)
    s.rect(x0, ax.y0 - 18, x1 - x0, ax.h + 36, fill="#ffffff", opacity=0.05, rx=6)
    s.line(x0, ax.y0 - 18, x0, ax.y0 + ax.h + 18, stroke="#c7d2fe", sw=1, opacity=0.3)
    s.line(x1, ax.y0 - 18, x1, ax.y0 + ax.h + 18, stroke="#c7d2fe", sw=1, opacity=0.3)
    cx_ = np.linspace(L, 1.5 * L, 60)
    ceil = 0.030 * (10 ** (cx_ - L)) ** 0.05
    s.path(ax.polyline(cx_, ceil), stroke="#fda4af", sw=3, opacity=0.9)
    s.rich((x0 + x1) / 2, ax.y0 - 30, [("window [Y, Y", {}), ("3/2", {"sup": True}), ("],  Y = 10", {}),
                                       ("4", {"sup": True})], size=15, fill="#c7d2fe", anchor="middle")
    s.text(x1 - 8, ax.Y(float(ceil[-1])) - 12, "one-sided ceiling C·y^θ, θ > ½", size=14, fill="#fda4af",
           anchor="end")
    # zero line and RH band
    s.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), stroke="#334155", sw=1)
    for v in (band, -band):
        s.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), stroke="#a5b4fc", sw=1.2, opacity=0.45,
               dash="2 6")
    s.text(ax.x0 + ax.w - 4, ax.Y(band) - 10, "+(2 + γ − log 4π)", size=15, fill="#a5b4fc",
           anchor="end", opacity=0.9)
    s.text(ax.x0 + ax.w - 4, ax.Y(-band) + 22, "−(2 + γ − log 4π)", size=15, fill="#a5b4fc",
           anchor="end", opacity=0.9)
    # the curve (min/max envelope per pixel column)
    lx = np.log10(ys)
    cx, lo, hi = envelope(lx, r, 1.0, 7.0, 1200)
    s.path(zigzag(ax, cx, lo, hi), stroke="url(#gold)", sw=1.6, extra='filter="url(#glow)"')
    # x ticks
    for k in range(1, 8):
        s.line(ax.X(k), ax.y0 + ax.h + 6, ax.X(k), ax.y0 + ax.h + 12, stroke="#475569", sw=1)
        s.rich(ax.X(k), ax.y0 + ax.h + 34, [("10", {}), (str(k), {"sup": True})], size=15,
               fill="#94a3b8", anchor="middle")
    s.text(ax.x0 + ax.w, ax.y0 + ax.h + 62, "y (log scale)", size=14, fill="#94a3b8", anchor="end")
    # left fade so the title can sit on the image
    s.rect(0, 0, W, H, fill="url(#fadeL)")
    save("hero", s)


# =====================================================================================
# 2. The explicit formula: the oscillation is the music of the zeros
# =====================================================================================
def fig_explicit(ps: rhlib.PrimeSums, zeros: list[float]) -> None:
    ys = np.exp(np.linspace(math.log(100.0), math.log(2.0e6), 1600))
    g = (ps.G(ys) - rhlib.LOG_2PI) / np.sqrt(ys)
    ef = (rhlib.explicit_formula_G(ys, zeros) - rhlib.LOG_2PI) / np.sqrt(ys)
    err = float(np.max(np.abs(g - ef)))
    assert err < 2.5e-3, err
    # hypothetical off-line zero (illustration only): rho = 0.62 + 40 i, contribution -2 Re y^rho/(rho(rho-1))
    rho = complex(0.62, 40.0)
    hyp = -2.0 * np.real(np.exp(rho * np.log(ys)) / (rho * (rho - 1.0))) / np.sqrt(ys)
    FACTS["explicit"] = {"zeros_used": len(zeros), "largest_ordinate": round(zeros[-1], 4),
                         "max_abs_difference_normalized": round(err, 5),
                         "y_range": [100, 2_000_000], "hypothetical_rho": [0.62, 40.0],
                         "hyp_growth_exponent": round(rho.real - 0.5, 2)}
    W, H = 980, 430
    s = SVG(W, H, "Prime sum versus the sum over zeros",
            f"Computed: normalized G(y) from primes (amber) and the explicit formula with the first "
            f"{len(zeros)} zeta zeros (indigo), 100 <= y <= 2e6; dashed: the term a hypothetical zero "
            f"at 0.62+40i would add (it grows like y^0.12).")
    ax = Axes(70, 30, 860, 330, (2.0, math.log10(2e6)), (-0.05, 0.05))
    for v in (-0.04, -0.02, 0, 0.02, 0.04):
        s.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), stroke=GRID, sw=1)
        s.text(ax.x0 - 8, ax.Y(v) + 4, f"{v:+.2f}" if v else "0", size=11, fill=MUTED, anchor="end")
    for k in range(2, 7):
        s.rich(ax.X(k), ax.y0 + ax.h + 20, [("10", {}), (str(k), {"sup": True})], size=12, fill=MUTED,
               anchor="middle")
    s.text(ax.x0 + ax.w, ax.y0 + ax.h + 40, "y", size=12, fill=MUTED, anchor="end", italic=True)
    band = rhlib.RH_BAND
    for v in (band, -band):
        s.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), stroke=ACCENT, sw=1, opacity=0.35, dash="3 5")
    lx = np.log10(ys)
    s.path(ax.polyline(lx, hyp), stroke=DEST, sw=1.5, dash="5 5", opacity=0.8)
    s.path(ax.polyline(lx, g), stroke=NUM, sw=2.4, opacity=0.95)
    s.path(ax.polyline(lx, ef), stroke=ACCENT, sw=1.1, opacity=0.95)
    # legend
    lx0, ly0 = ax.x0 + 12, ax.y0 + 14
    s.rect(lx0 - 8, ly0 - 12, 380, 66, fill=SURFACE, opacity=0.92, rx=8, stroke=GRID)
    s.line(lx0, ly0, lx0 + 22, ly0, stroke=NUM, sw=2.4)
    s.text(lx0 + 30, ly0 + 4, "from primes: (G(y) − log 2π)/√y", size=12, fill=TEXT)
    s.line(lx0, ly0 + 19, lx0 + 22, ly0 + 19, stroke=ACCENT, sw=1.2)
    s.text(lx0 + 30, ly0 + 23, f"from the first {len(zeros)} zeros (explicit formula)", size=12, fill=TEXT)
    s.line(lx0, ly0 + 38, lx0 + 22, ly0 + 38, stroke=DEST, sw=1.5, dash="5 5")
    s.text(lx0 + 30, ly0 + 42, "one hypothetical zero at 0.62 + 40i would add this", size=12, fill=TEXT)
    save("explicit-formula", s)


# =====================================================================================
# 3. The critical strip and reflection
# =====================================================================================
def fig_strip(zeros: list[float]) -> None:
    W, H = 760, 560
    s = SVG(W, H, "Critical strip, reflection and the half-plane theorem",
            "Schematic plane with the computed first zeta zeros on the critical line; a hypothetical "
            "off-line zero rho and its mirror image 1 - conj(rho) under the functional equation.")
    ax = Axes(90, 30, 600, 470, (-0.5, 1.6), (0.0, 52.0))
    arrow = s.arrow_marker("arr-strip", INK)
    s.rect(ax.X(0.5), ax.y0, ax.X(1.0) - ax.X(0.5), ax.h, fill=DEST, opacity=0.07)
    s.rect(ax.X(1.0), ax.y0, ax.X(1.6) - ax.X(1.0), ax.h, fill=OK, opacity=0.08)
    for x in (0.0, 1.0):
        s.line(ax.X(x), ax.y0, ax.X(x), ax.y0 + ax.h, stroke=FAINT, sw=1, dash="4 4")
    s.line(ax.X(0.5), ax.y0, ax.X(0.5), ax.y0 + ax.h, stroke=DEST, sw=2)
    s.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), stroke=INK, sw=1)
    for x, lab in ((0.0, "0"), (0.5, "½"), (1.0, "1")):
        s.text(ax.X(x), ax.Y(0) + 20, lab, size=13, fill=MUTED, anchor="middle")
    s.text(ax.x0 + ax.w, ax.Y(0) + 20, "Re s", size=12, fill=MUTED, anchor="end", italic=True)
    for t in (10, 20, 30, 40, 50):
        s.text(ax.x0 - 10, ax.Y(t) + 4, f"{t}i", size=11, fill=MUTED, anchor="end")
    shown = [g for g in zeros if g < 52]
    for g in shown:
        s.circle(ax.X(0.5), ax.Y(g), 4.5, fill=DEST, stroke=SURFACE, sw=2)
    b, t = 0.78, 26.8
    s.circle(ax.X(b), ax.Y(t), 6.5, fill=SURFACE, stroke=INK, sw=1.6)
    s.circle(ax.X(1 - b), ax.Y(t), 6.5, fill=SURFACE, stroke=INK, sw=1.6, extra='stroke-dasharray="3 2"')
    s.path(f"M{f(ax.X(1 - b) + 9)},{f(ax.Y(t) + 9)} Q{f(ax.X(0.5))},{f(ax.Y(t) + 52)} "
           f"{f(ax.X(b) - 9)},{f(ax.Y(t) + 9)}", stroke=INK, sw=1.4, extra=f'marker-end="{arrow}"')
    s.rich(ax.X(0.5), ax.Y(t) + 72, [("reflection: L(s, χ) = 0  ⇒  L(1 − s, χ", {}), ("−1", {"sup": True}),
                                     (") = 0", {})], size=12, fill=INK, anchor="middle")
    s.text(ax.X(b) + 12, ax.Y(t) + 5, "ρ ?", size=14, fill=INK, italic=True)
    # 1 - conj(rho), with a drawn overline
    lx = ax.X(1 - b) - 14
    s.text(lx, ax.Y(t) + 5, "1 − ρ", size=14, fill=INK, anchor="end", italic=True)
    s.line(lx - 9, ax.Y(t) - 9, lx - 1, ax.Y(t) - 9, stroke=INK, sw=1.2)
    s.text(ax.X(1.05), ax.y0 + 22, "Re s ≥ 1: classical", size=12, fill=OK, weight=600)
    s.text(ax.X(1.05), ax.y0 + 38, "nonvanishing (Mathlib)", size=11, fill=OK)
    s.text(ax.X(0.6), ax.y0 + 120, "Re s > ½:", size=12.5, fill=DEST, weight=700)
    s.text(ax.X(0.6), ax.y0 + 137, "half-plane", size=12, fill=DEST)
    s.text(ax.X(0.6), ax.y0 + 153, "theorem,", size=12, fill=DEST)
    s.text(ax.X(0.6), ax.y0 + 169, "every χ", size=12, fill=DEST)
    s.text(ax.X(-0.47), ax.y0 + 22, f"first {len(shown)} zeros, computed", size=12, fill=MUTED)
    s.circle(ax.X(-0.47) + 4, ax.y0 + 40, 4.5, fill=DEST, stroke=SURFACE, sw=2)
    s.text(ax.X(-0.47) + 14, ax.y0 + 44, "on Re s = ½", size=12, fill=MUTED)
    s.circle(ax.X(-0.47) + 4, ax.y0 + 62, 5.5, fill=SURFACE, stroke=INK, sw=1.4)
    s.text(ax.X(-0.47) + 14, ax.y0 + 66, "hypothetical zero", size=12, fill=MUTED)
    FACTS["strip"] = {"zeros_drawn": len(shown)}
    save("strip", s)


# =====================================================================================
# 4. The ramp and its Mellin transform
# =====================================================================================
def fig_ramp(ps: rhlib.PrimeSums) -> None:
    # numerical check of int_1^inf (y/n-1)_+ y^{-s-1} dy = n^{-s}/(s(s-1)) at a few (n, s)
    checks = []
    for n in (2, 3, 7):
        for sv in (complex(2.0, 0.0), complex(1.5, 3.0), complex(3.0, -2.0)):
            # substitute y = n e^v: integral = n^{-s} int_0^inf (e^v - 1) e^{-s v} dv
            v = np.linspace(0, 60, 600_001)
            integrand = (np.exp(v) - 1.0) * np.exp(-sv * v)
            num = n ** (-sv) * np.trapezoid(integrand, v)
            exact = n ** (-sv) / (sv * (sv - 1))
            checks.append(abs(num - exact))
    assert max(checks) < 1e-6, max(checks)
    yy = np.linspace(1.0, 120.0, 6000)
    G = ps.G(yy)
    tail = G[yy >= 20]
    FACTS["ramp"] = {"mellin_checks": len(checks), "max_abs_error": float(f"{max(checks):.2e}"),
                     "G_range_20_120": [round(float(tail.min()), 3), round(float(tail.max()), 3)],
                     "log_2pi": round(rhlib.LOG_2PI, 4)}
    W, H = 980, 380
    s = SVG(W, H, "Ramps and the centered sum",
            "Computed. Left: the weighted ramps Lambda(n)(y/n-1)_+ for prime powers n <= 13, each switching "
            "on at y = n with slope Lambda(n)/n. Right: their full sum minus y log y - (1+gamma) y, i.e. "
            "G(y), for 1 <= y <= 120; it hovers around log 2pi (dashed), the residue at s = 0.")
    ax = Axes(60, 40, 380, 270, (1.0, 14.0), (0.0, 4.5))
    s.text(60, 24, "weighted ramps Λ(n)(y/n − 1)₊", size=13, fill=INK, weight=600)
    for v in (0, 1, 2, 3, 4):
        s.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), stroke=GRID, sw=1)
        s.text(ax.x0 - 8, ax.Y(v) + 4, str(v), size=11, fill=MUTED, anchor="end")
    for k in (2, 4, 6, 8, 10, 12, 14):
        s.text(ax.X(k), ax.y0 + ax.h + 18, str(k), size=11, fill=MUTED, anchor="middle")
    s.text(ax.x0 + ax.w, ax.y0 + ax.h + 36, "y", size=12, fill=MUTED, anchor="end", italic=True)
    lam = rhlib.von_mangoldt_table(14)
    for n in range(2, 14):
        if lam[n] > 0:
            xs = [1.0, float(n), 14.0]
            ys = [0.0, 0.0, lam[n] * (14.0 / n - 1.0)]
            s.path(ax.polyline(xs, ys), stroke=ANA, sw=1.8, opacity=0.35 + 0.5 * (n in (2, 3, 5, 7, 11, 13)))
            s.text(ax.X(n), ax.Y(0) + 4 - 14, f"{n}", size=10.5, fill=TEXT, anchor="middle")
    bx = Axes(540, 40, 400, 270, (0.0, 120.0), (-2.0, 6.0))
    s.text(540, 24, "Σ Λ(n)(y/n − 1) − y log y + (1+γ)y  =  G(y)", size=13, fill=INK, weight=600)
    for v in (-2, 0, 2, 4, 6):
        s.line(bx.x0, bx.Y(v), bx.x0 + bx.w, bx.Y(v), stroke=GRID, sw=1)
        s.text(bx.x0 - 8, bx.Y(v) + 4, str(v), size=11, fill=MUTED, anchor="end")
    for k in (0, 20, 40, 60, 80, 100, 120):
        s.text(bx.X(k), bx.y0 + bx.h + 18, str(k), size=11, fill=MUTED, anchor="middle")
    s.text(bx.x0 + bx.w, bx.y0 + bx.h + 36, "y", size=12, fill=MUTED, anchor="end", italic=True)
    s.line(bx.x0, bx.Y(rhlib.LOG_2PI), bx.x0 + bx.w, bx.Y(rhlib.LOG_2PI), stroke=INK, sw=1.2, dash="5 4",
           opacity=0.7)
    s.text(bx.x0 + bx.w, bx.Y(rhlib.LOG_2PI) - 8, "log 2π", size=12, fill=MUTED, anchor="end")
    cx, lo, hi = envelope(yy, G, 0.0, 120.0, 400)
    s.path(zigzag(bx, cx, lo, hi), stroke=ANA, sw=1.6)
    save("ramp", s)


# =====================================================================================
# 5. Positive residues: the weighted zero orders cannot cancel
# =====================================================================================
def fig_residue() -> None:
    rho = complex(0.7, 14.0)
    c = -1.0 / (rho * (rho - 1.0))
    FACTS["residue"] = {"rho": [rho.real, rho.imag], "direction_deg": round(math.degrees(math.atan2(c.imag, c.real)), 2)}
    W, H = 900, 300
    s = SVG(W, H, "Positive weights keep the residue alive",
            "Schematic, exact in direction: at a common zero rho every member of a positive family contributes "
            "a positive multiple of the same complex number -1/(rho(rho-1)), so the contributions add; with "
            "signed weights two contributions could cancel.")
    a1 = s.arrow_marker("arr-res", ANA, 6)
    a2 = s.arrow_marker("arr-res2", MOTIV, 6)
    s.text(40, 34, "positive family:  contributions add", size=13.5, fill=INK, weight=600)
    ux, uy = math.cos(math.radians(-24)), math.sin(math.radians(-24))
    x, y = 60.0, 230.0
    parts = [(78.0, "½ a₁ (m(χ₁) + m(χ₁⁻¹))"), (52.0, "½ a₂ (m(χ₂) + m(χ₂⁻¹))"), (104.0, "½ a₃ (m(χ₃) + m(χ₃⁻¹))")]
    for i, (L, lab) in enumerate(parts):
        s.line(x, y, x + ux * (L - 3), y + uy * (L - 3), stroke=ANA, sw=3, opacity=0.55 + 0.2 * i,
               extra=f'marker-end="{a1}"')
        s.circle(x, y, 3.5, fill=ANA)
        s.text(x + ux * L / 2 + 8, y + uy * L / 2 + 22, lab, size=11.5, fill=TEXT)
        x, y = x + ux * L, y + uy * L
    s.text(x + 12, y - 2, "total: S(ρ) · (−1/(ρ(ρ − 1)))", size=13, fill=INK, weight=600)
    s.text(40, 284, "S(ρ) = ½ Σᵢ aᵢ (ord_ρ L(·, χᵢ) + ord_ρ L(·, χᵢ⁻¹)) > 0  whenever some member vanishes at ρ",
           size=12.5, fill=TEXT)
    s.text(600, 34, "signed weights:  could cancel", size=13.5, fill=MUTED, weight=600)
    x0, y0 = 630.0, 190.0
    s.line(x0, y0, x0 + ux * 120, y0 + uy * 120, stroke=MOTIV, sw=3, extra=f'marker-end="{a2}"')
    s.line(x0 + ux * 120, y0 + uy * 120 + 18, x0 + 4, y0 + 18, stroke=MOTIV, sw=3, dash="5 4",
           extra=f'marker-end="{a2}"')
    s.text(x0 + 140, y0 - 20, "+a", size=12, fill=MUTED)
    s.text(x0 + 140, y0 + 12, "−a", size=12, fill=MUTED)
    s.text(600, 250, "the source requires aᵢ > 0 and a", size=12, fill=MUTED)
    s.text(600, 266, "principal member only of modulus 1", size=12, fill=MUTED)
    save("residue", s)


# =====================================================================================
# 6. The spotlight: high derivatives focus on one window
# =====================================================================================
def fig_spotlight() -> None:
    sigma, delta = 1.0, 0.5
    Us = [20.0, 40.0, 80.0, 160.0]
    masses = {}
    for U in Us:
        k = math.ceil((1 + delta / 2) * sigma * U)
        masses[int(U)] = {"k": k, "mass_inside": round(rhlib.spotlight_mass_in(U, delta, k, sigma), 4)}
    vals = [masses[int(U)]["mass_inside"] for U in Us]
    assert all(b > a for a, b in zip(vals, vals[1:])) and vals[-1] > 0.99, vals
    FACTS["spotlight"] = {"sigma": sigma, "delta": delta, "windows": masses}
    W, H = 980, 380
    s = SVG(W, H, "The spotlight of high derivatives",
            "Computed: kernels u^k e^{-u}/k! (normalized to peak 1) with k = ceil(1.25 U) for U = 20, 40, "
            "80, 160 and the windows [U, 1.5 U] in u = log y; labels give the fraction of each kernel's "
            "mass inside its window.")
    ax = Axes(60, 70, 880, 236, (0.0, 260.0), (0.0, 1.0))
    s.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), stroke=GRID, sw=1)
    for k in range(0, 261, 40):
        s.text(ax.X(k), ax.y0 + ax.h + 18, str(k), size=11, fill=MUTED, anchor="middle")
    s.text(ax.x0 + ax.w, ax.y0 + ax.h + 38, "u = log y", size=12, fill=MUTED, anchor="end", italic=True)
    u = np.linspace(0.5, 260.0, 1200)
    for i, U in enumerate(Us):
        k = masses[int(U)]["k"]
        s.rect(ax.X(U), ax.y0, ax.X(1.5 * U) - ax.X(U), ax.h, fill=ANA, opacity=0.07 + 0.02 * i)
        v = rhlib.spotlight(u, k, sigma)
        v = v / v.max()
        s.path(ax.polyline(u, v), stroke=ANA, sw=2, opacity=0.45 + 0.18 * i)
        pct = masses[int(U)]["mass_inside"] * 100
        s.text(ax.X(1.25 * U), ax.Y(1.10), f"k = {k}", size=11.5, fill=TEXT, anchor="middle", weight=600)
        s.text(ax.X(1.25 * U), ax.Y(1.10) + 15, f"{pct:.1f}% inside", size=11, fill=MUTED, anchor="middle")
    save("spotlight", s)


# =====================================================================================
# 7. The square-root balance and the exponent staircase
# =====================================================================================
def fig_balance() -> None:
    rows = rhlib.budget_rows()
    worst = max(r["eps"] for r in rows if r["half"] == Fraction(1, 2))
    assert worst == Fraction(13, 8)
    eD, eL = 2, 0
    Cstar = eD + eL + 3
    steps = [("balance x/m vs m (worst budget term)", Fraction(13, 8)),
             ("geometric error E ≤ x^(C*·ε)·B with C* = e_D + e_L + 3", Fraction(Cstar)),
             ("density of the averaging set: 2/δ ≤ 2·x^ε", Fraction(1)),
             ("absorbing the constant: 26 ≤ x^(3ε/8)", Fraction(3, 8)),
             ("restoring discarded characters: 1 + 4o ≤ x^ε", Fraction(1))]
    total = sum(v for _, v in steps)
    assert total == eD + eL + 7 == 9, total
    FACTS["balance"] = {"worst_budget_eps": "13/8", "steps": [[a, str(b)] for a, b in steps],
                        "total_eps": str(total), "eD": eD, "eL": eL,
                        "budget": [{"term": r["term"], "coef": r["coef"],
                                    "exponent": ("1/2 + " if r["half"] else "") + f"{r['eps']}·ε"
                                    if r["half"] else "O(1)", "why": r["why"]} for r in rows]}
    W, H = 980, 400
    s = SVG(W, H, "Where the square root and each epsilon are paid",
            "Left: exponents 1-a of x/m and a of m when m = x^a; the larger is smallest at a = 1/2. "
            "Right: exact staircase of the losses in units of epsilon, from the finite comparison to "
            "1/2 + (e_D+e_L+7) eps = 1/2 + 9 eps for the source's choice e_D = 2, e_L = 0.")
    ax = Axes(60, 40, 330, 280, (0.0, 1.0), (0.0, 1.0))
    for v in (0, 0.5, 1.0):
        s.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), stroke=GRID, sw=1)
        s.text(ax.x0 - 8, ax.Y(v) + 4, {0: "0", 0.5: "½", 1.0: "1"}[v], size=12, fill=MUTED, anchor="end")
        s.text(ax.X(v), ax.y0 + ax.h + 18, {0: "0", 0.5: "½", 1.0: "1"}[v], size=12, fill=MUTED,
               anchor="middle")
    s.text(ax.x0 + ax.w, ax.y0 + ax.h + 38, "a  (m = xᵃ)", size=12, fill=MUTED, anchor="end")
    a = np.linspace(0, 1, 201)
    s.path(ax.polyline(a, 1 - a), stroke=EST, sw=1.4, opacity=0.6, dash="5 4")
    s.path(ax.polyline(a, a), stroke=EST, sw=1.4, opacity=0.6, dash="5 4")
    s.path(ax.polyline(a, np.maximum(a, 1 - a)), stroke=EST, sw=2.6)
    s.circle(ax.X(0.5), ax.Y(0.5), 5, fill=EST, stroke=SURFACE, sw=2)
    s.text(ax.X(0.08), ax.Y(0.94), "x/m", size=12, fill=TEXT)
    s.text(ax.X(0.92), ax.Y(0.94), "m", size=12, fill=TEXT, anchor="end")
    s.text(ax.X(0.5), ax.Y(0.5) + 24, "chain length m ≈ √x", size=12, fill=INK, anchor="middle", weight=600)
    # staircase
    bx = Axes(500, 40, 430, 280, (0, 9.6), (0, 6))
    s.text(500, 28, "losses above ½, in units of ε", size=13, fill=INK, weight=600)
    acc = Fraction(0)
    for i, (lab, v) in enumerate(steps):
        y = bx.y0 + 14 + i * 52
        x0 = bx.X(float(acc))
        x1 = bx.X(float(acc + v))
        s.rect(x0, y, max(2.0, x1 - x0 - 2), 22, fill=EST, opacity=0.18 + 0.12 * i, rx=4)
        s.text(x1 + 6, y + 15, f"+{v}", size=12, fill=TEXT, family=MONO)
        s.text(bx.x0, y + 38, lab, size=11.5, fill=MUTED)
        acc += v
    s.line(bx.X(9), bx.y0, bx.X(9), bx.y0 + 268, stroke=INK, sw=1, dash="3 3")
    s.text(bx.X(9), bx.y0 + 286, "total 9 = e_D + e_L + 7", size=12, fill=INK, anchor="middle", weight=600)
    save("balance", s)


# =====================================================================================
# 8. The cohomological window: exceptional twists and one good interval
# =====================================================================================
def fig_windows() -> None:
    starts, B, U = [8.0, 90.0], 2.0, 128.0
    y, y2 = rhlib.window1(starts, B, U)
    assert (y, y2) == (16.0, 32.0) and rhlib.avoids(y, starts, B)
    exc = rhlib.ultrametric_exceptions(3, 80, 1)
    assert exc == [1]
    FACTS["windows"] = {"example": {"Ct": 2, "eta": 1, "B": 2, "X": "2^128", "twists": ["2^16", "2^180"],
                                    "starts": starts, "interval_log2": [y, y2],
                                    "interval": ["2^16", "2^32"]},
                        "ultrametric": {"ell": 3, "Z": 80, "center": 1, "exceptional": exc,
                                        "if_mod_27": [1, 28, 55]}}
    W, H = 980, 330
    s = SVG(W, H, "One interval survives all exceptional twists",
            "Computed with the induction of UpperTheory.V.Win.window1 on the book's example: forbidden "
            "logarithmic intervals [a, B a) for a = 8, 90 with B = 2 inside [0, 128]; the recursion lowers "
            "the ceiling 128 -> 32 and returns [16, 32], i.e. [Y, Y^2] = [2^16, 2^32].")
    ax = Axes(60, 70, 860, 60, (0.0, 200.0), (0, 1))
    s.text(60, 30, "u = log₂ x   (forbidden: [a, 2a) for each exceptional twist h, a = log₂(h)/C_t)",
           size=13, fill=INK, weight=600)
    s.line(ax.x0, ax.y0 + 60, ax.x0 + ax.w, ax.y0 + 60, stroke=INK, sw=1)
    for k in range(0, 201, 20):
        s.line(ax.X(k), ax.y0 + 60, ax.X(k), ax.y0 + 66, stroke=INK, sw=1)
        s.text(ax.X(k), ax.y0 + 82, str(k), size=11, fill=MUTED, anchor="middle")
    for a in starts:
        s.rect(ax.X(a), ax.y0 + 8, ax.X(B * a) - ax.X(a), 22, fill=ARITH, opacity=0.8, rx=3)
        s.text((ax.X(a) + ax.X(B * a)) / 2, ax.y0 + 2, f"[{a:g}, {B * a:g})", size=11, fill=ARITH,
               anchor="middle")
    s.rect(ax.X(y), ax.y0 + 34, ax.X(y2) - ax.X(y), 22, fill=OK, opacity=0.85, rx=3)
    s.text((ax.X(y) + ax.X(y2)) / 2, ax.y0 + 50, "[16, 32]", size=11, fill=SURFACE, anchor="middle",
           weight=600)
    s.text(ax.X(y2) + 10, ax.y0 + 50, "→ [Y, Y²] = [2¹⁶, 2³²]", size=12, fill=OK, weight=600)
    # recursion ceilings
    for i, (ceil, note) in enumerate([(128.0, "ceiling U = 128: start 90 lies in (32, 128] → delete it"),
                                      (32.0, "ceiling U′ = 128/(2B) = 32: no start in (8, 32] → y = U′/2 = 16")]):
        yy = 190 + i * 34
        s.line(ax.X(0), yy, ax.X(ceil), yy, stroke=MUTED, sw=2)
        s.circle(ax.X(ceil), yy, 4, fill=MUTED)
        s.text(ax.X(ceil) + 10, yy + 4, note, size=12, fill=TEXT)
    s.text(60, 290, "Ultrametric separation (ℓ = 3, Z = 80, centre 1): |h − 1|₃ < 3⁻³ forces h ≡ 1 mod 81, "
           "so h = 1 only;", size=12, fill=TEXT)
    s.text(60, 308, "with ≤ instead of < one would also admit 28 and 55. Each ℓ-adic centre produces at most one "
           "exceptional twist.", size=12, fill=TEXT)
    save("windows", s)


# =====================================================================================
# 9. Behrend: a digit sphere avoids short affine relations
# =====================================================================================
def fig_behrend() -> None:
    pts, enc, checks = rhlib.behrend_example()
    assert sorted(enc) == [26, 49, 578, 624, 1153, 1176] and checks == 1440
    # the six points lie on the plane x+y+z = 3 at distance sqrt 2 from (1,1,1)
    c = np.array([1.0, 1.0, 1.0])
    e1 = np.array([1.0, -1.0, 0.0]) / math.sqrt(2)
    e2 = np.array([1.0, 1.0, -2.0]) / math.sqrt(6)
    coords = []
    for v in pts:
        w = np.array(v, dtype=float) - c
        assert abs(sum(v) - 3) == 0 and abs(float(w @ w) - 2.0) < 1e-12
        coords.append((float(w @ e1), float(w @ e2)))
    FACTS["behrend"] = {"S": 3, "d": 3, "L": 2, "norm": 5, "base": 24, "points": [list(p) for p in pts],
                        "encodings": enc, "checks": checks, "plane": "x+y+z=3", "radius_in_plane": "sqrt(2)"}
    W, H = 900, 380
    s = SVG(W, H, "A Behrend digit sphere",
            "Computed: the vectors of {0,1,2}^3 with squared norm 5 are the six permutations of (0,1,2); they "
            "lie on the circle where the sphere meets the plane x+y+z = 3. Their base-24 encodings avoid every "
            "relation j(s2-s1) = i(s3-s1) with 1 <= |i|,|j| <= 2, i != j: 1,440 checks.")
    cx0, cy0, R = 262.0, 186.0, 112.0
    sc = R / math.sqrt(2)
    s.circle(cx0, cy0, R, fill="none", stroke=ARITH, sw=1.4, opacity=0.6)
    # a secant line through two of the points: a line meets the circle at most twice
    (p, q) = (coords[0], coords[3])
    P = (cx0 + sc * p[0], cy0 - sc * p[1])
    Q = (cx0 + sc * q[0], cy0 - sc * q[1])
    dx, dy = Q[0] - P[0], Q[1] - P[1]
    s.line(P[0] - 0.35 * dx, P[1] - 0.35 * dy, Q[0] + 0.35 * dx, Q[1] + 0.35 * dy, stroke=MUTED, sw=1.2,
           dash="5 4")
    for v, e, (u, w) in zip(pts, enc, coords):
        X, Y = cx0 + sc * u, cy0 - sc * w
        s.circle(X, Y, 7.5, fill=ARITH, stroke=SURFACE, sw=2)
        dxl = 14 if u >= -1e-9 else -14
        s.text(X + dxl, Y + (-10 if w > 0 else 18), f"({v[0]},{v[1]},{v[2]}) ↦ {e}", size=12, fill=TEXT,
               anchor="start" if u >= -1e-9 else "end", family=MONO)
    s.text(cx0, cy0 + R + 40, "sphere x² + y² + z² = 5  ∩  plane x + y + z = 3", size=12, fill=MUTED,
           anchor="middle")
    s.text(470, 70, "Encode (x, y, z) ↦ 24²x + 24y + z  (base 4Ld = 24).", size=13, fill=INK, weight=600)
    s.text(470, 100, "The base is large enough that no carries occur, so", size=12.5, fill=TEXT)
    s.text(470, 118, "j(s₂ − s₁) = i(s₃ − s₁) between encodings forces the", size=12.5, fill=TEXT)
    s.text(470, 136, "same relation between the vectors: three points on", size=12.5, fill=TEXT)
    s.text(470, 154, "one line. A line meets a sphere at most twice.", size=12.5, fill=TEXT)
    s.text(470, 196, f"{checks:,} relation checks, none holds", size=13.5, fill=OK, weight=700)
    s.text(470, 216, "(120 ordered triples × 12 pairs (i, j), 1 ≤ |i|, |j| ≤ 2, i ≠ j)", size=12, fill=MUTED)
    s.text(470, 256, "Lean: BehrendReading.sphere_rel (this repository)", size=12, fill=TEXT, family=MONO)
    s.text(470, 274, "Archive: Formalism.FrobeniusOrbits.ThickExists.noRel_image", size=12, fill=TEXT, family=MONO)
    save("behrend", s)


# =====================================================================================
# 10. Schematic: the chain of theta lifts
# =====================================================================================
def fig_chain() -> None:
    W, H = 980, 250
    s = SVG(W, H, "The chain of theta lifts (schematic)",
            "Schematic: unitary groups U(X0) -> U(X1) -> ... -> U(Xm) linked by theta lifts; each lift "
            "carries a denominator D_j; the archive's RankVal puts m between sqrt(x delta1) and "
            "2 sqrt(x delta1), delta1 = x^(-eps/8).")
    arrow = s.arrow_marker("arr-ch", EST)
    xs = [60, 225, 390, 640, 815]
    subs = ["0", "1", "2", "m−1", "m"]
    for i, (x, sb) in enumerate(zip(xs, subs)):
        s.rect(x, 80, 120, 52, fill=EST, opacity=0.1 + 0.03 * i, rx=10, stroke=EST, sw=1.2)
        s.rich(x + 60, 112, [("U(X", {}), (sb, {"sub": True}), (")", {})], size=15, fill=INK, anchor="middle",
               weight=600)
    links = [(0, 1, "0"), (1, 2, "1"), (3, 4, "m−1")]
    for i, j, sb in links:
        s.line(xs[i] + 122, 106, xs[j] - 4, 106, stroke=EST, sw=2, extra=f'marker-end="{arrow}"')
        s.rich((xs[i] + 122 + xs[j]) / 2, 96, [("θ, ×D", {}), (sb, {"sub": True})], size=12.5, fill=TEXT,
               anchor="middle")
    s.text((xs[2] + 120 + xs[3]) / 2, 112, "· · ·", size=20, fill=EST, anchor="middle")
    s.text(60, 40, "π ↦ π ⊞ μⱼ[t] at each step: each lift is meant to mimic one order of multiplicity",
           size=13.5, fill=INK, weight=600)
    s.rich(60, 176, [("√(xδ", {}), ("1", {"sub": True}), (") ≤ m ≤ 2√(xδ", {}), ("1", {"sub": True}),
                     ("),   δ", {}), ("1", {"sub": True}), (" = x", {}), ("−ε/8", {"sup": True}),
                     ("   ⇒   m ≈ x", {}), ("1/2 − ε/16", {"sup": True}),
                     ("      GlobalTheory.EX.RankVal", {"family": MONO, "fill": MUTED})], size=13, fill=TEXT)
    s.rich(60, 206, [("(∏ D", {}), ("j", {"sub": True}), (") · (T", {}), ("m−1", {"sub": True}),
                     (" ⋯ T", {}), ("0", {"sub": True}), (" f)(v) ∈ S  when every D", {}), ("j", {"sub": True}),
                     ("w", {}), ("j", {"sub": True}), (", every kernel entry and f are S-integral", {}),
                     ("      Formalism.ThetaLiftIndependence.ChainInt", {"family": MONO, "fill": MUTED})],
           size=13, fill=TEXT)
    save("chain", s)


# =====================================================================================
# 11. Schematic: the Galois row by quadratic descent
# =====================================================================================
def fig_galois() -> None:
    W, H = 900, 380
    s = SVG(W, H, "The Galois row by quadratic descent (schematic)",
            "Schematic: representations r_K over infinitely many quadratic CM extensions K = E(sqrt(-p)) "
            "are patched to one rho over E whose Frobenius polynomials match the Satake parameters of pi.")
    arrow = s.arrow_marker("arr-g", ARITH, 6)
    s.rect(345, 262, 210, 56, fill=ARITH, opacity=0.13, rx=10, stroke=ARITH, sw=1.4)
    s.text(450, 286, "E  (CM field),  π on GL_a", size=14, fill=INK, anchor="middle", weight=600)
    s.text(450, 306, "one ρ : G_E → GL_a(Q̄_ℓ)", size=12.5, fill=TEXT, anchor="middle", family=MONO)
    xs = [40, 245, 450, 655]
    for i, x in enumerate(xs):
        s.rect(x, 112, 180, 54, fill=ARITH, opacity=0.07, rx=10, stroke=ARITH, sw=1)
        s.rich(x + 90, 136, [("K", {}), (str(i + 1), {"sub": True}), (" = E(√−p", {}), (str(i + 1), {"sub": True}),
                             (")", {})], size=13, fill=INK, anchor="middle")
        s.rich(x + 90, 156, [("r", {}), ("K" + str(i + 1), {"sub": True}), ("  from the good case", {})], size=12,
               fill=MUTED, anchor="middle")
        s.line(x + 90, 168, 450 + (i - 1.5) * 34, 258, stroke=ARITH, sw=1.4, opacity=0.65,
               extra=f'marker-end="{arrow}"')
    s.text(860, 144, "…", size=22, fill=ARITH, anchor="middle")
    s.rich(450, 50, [("p", {}), ("i", {"sub": True}), (" ≡ −1 mod M outside a finite bad set: √−p", {}),
                     ("i", {"sub": True}), (" ∉ E, since inertia at p", {}), ("i", {"sub": True}),
                     (" moves it", {})], size=12.5, fill=TEXT, anchor="middle")
    s.text(450, 76, "index-two patching of conjugation-invariant trace identities  ⇒  one ρ over E",
           size=12.5, fill=TEXT, anchor="middle")
    s.rich(450, 352, [("ι(charpoly ρ(σ", {}), ("−1", {"sup": True}), (")) = ∏", {}), ("α∈B_v", {"sub": True}),
                      ("(X − q", {}), ("(a−1)/2", {"sup": True}), ("α)   for all but finitely many places v", {})],
           size=13, fill=INK, anchor="middle")
    save("galois", s)


# =====================================================================================
# 12. Schematic: the choreography of quantifiers
# =====================================================================================
def fig_choreography() -> None:
    W, H = 980, 210
    s = SVG(W, H, "The order of choices (schematic)",
            "Schematic: the loss exponents are fixed first; a candidate zero beta > 1/2 is given; theta is "
            "chosen between 1/2 and beta; epsilon is chosen so that 1/2 + (e_D+e_L+7) eps <= theta; the "
            "arithmetic then supplies windows for that epsilon; the analytic criterion excludes the zero.")
    arrow = s.arrow_marker("arr-q", INK, 6)
    steps = [("fix the losses", "e_D = 2, e_L = 0", EST), ("suppose a zero", "with Re ρ = β > ½", DEST),
             ("choose θ", "½ < θ < min(β, 1)", ANA), ("choose ε", "½ + 9ε ≤ θ", EST),
             ("arithmetic supplies", "windows [Y, Y^(3/2)]", ARITH), ("the criterion", "excludes Re s > θ", ANA)]
    x, w = 20, 148
    for i, (l1, l2, col) in enumerate(steps):
        s.rect(x, 70, w, 64, fill=col, opacity=0.1, rx=10, stroke=col, sw=1.2)
        s.text(x + w / 2, 97, l1, size=12.5, fill=INK, anchor="middle", weight=600)
        s.text(x + w / 2, 117, l2, size=12, fill=TEXT, anchor="middle")
        s.text(x + w / 2, 156, f"{i + 1}", size=12, fill=MUTED, anchor="middle", weight=700)
        if i < len(steps) - 1:
            s.line(x + w + 2, 102, x + w + 12, 102, stroke=INK, sw=1.5, extra=f'marker-end="{arrow}"')
        x += w + 14
    s.text(20, 40, "Why a bound at ε = 0 is never needed: θ is chosen after the zero, and ε after θ",
           size=13.5, fill=INK, weight=600)
    s.text(20, 190, "Lean: Formalism.HC.level_of_tiedWin takes θ = ½ + ½·min(β − ½, ½); the window width is 3/2.",
           size=12, fill=MUTED, family=MONO)
    save("choreography", s)


# 0. Hero background: the curve t -> zeta(1/2 + it) through the origin at every zero
def _rdp(pts: np.ndarray, eps: float) -> np.ndarray:
    """Ramer-Douglas-Peucker simplification (iterative); returns the kept indices."""
    keep = np.zeros(len(pts), dtype=bool)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        if b <= a + 1:
            continue
        d = pts[b] - pts[a]
        n = math.hypot(d[0], d[1])
        seg = pts[a + 1:b] - pts[a]
        dist = np.hypot(seg[:, 0], seg[:, 1]) if n == 0 else np.abs(d[0] * seg[:, 1] - d[1] * seg[:, 0]) / n
        i = int(np.argmax(dist))
        if dist[i] > eps:
            keep[a + 1 + i] = True
            stack += [(a, a + 1 + i), (a + 1 + i, b)]
    return np.nonzero(keep)[0]


def fig_hero_zeta(t_max: float = 80.0, chunks: int = 28) -> None:
    dt = 0.005
    ts = np.arange(0.0, t_max + dt / 2, dt)
    zs = np.array([rhlib.zeta_em(complex(0.5, float(t))) for t in ts])
    # rs_theta is an asymptotic series, valid for t >= 10; zeta_zeros also starts at t0 = 10 (no zero lies below 14)
    i10 = int(round(10.0 / dt))
    hz = np.array([rhlib.hardy_z(float(t)) for t in ts[i10:]])
    changes = np.nonzero(hz[:-1] * hz[1:] < 0)[0] + i10 - 1
    n_grid = len(changes)
    allz = rhlib.zeta_zeros(n_grid + 3)
    zeros = [g for g in allz if g <= t_max]
    if len(zeros) != n_grid:
        raise SystemExit(f"hero_zeta: zero count mismatch: sign changes {n_grid}, zeta_zeros {len(zeros)}")
    for g, i in zip(zeros, changes):   # each bisected zero lies in its grid cell
        if not (ts[1 + i] - 1e-9 <= g <= ts[2 + i] + 1e-9):
            raise SystemExit(f"hero_zeta: zero {g} outside its grid cell")
    if min(abs(rhlib.zeta_em(complex(0.5, g))) for g in zeros) > 1e-6 or \
            max(abs(rhlib.zeta_em(complex(0.5, g))) for g in zeros) > 1e-6:
        raise SystemExit("hero_zeta: curve does not pass through 0 at the zeros")
    if abs(zeros[0] - 14.134725) >= 1e-5:
        raise SystemExit(f"hero_zeta: first zero {zeros[0]} is not 14.134725")
    # frame: equal scale, curve centred in a 1400 x 600 box
    W, H = 1400, 600
    re_, im_ = zs.real, zs.imag
    cx, cy = (re_.max() + re_.min()) / 2, (im_.max() + im_.min()) / 2
    sc = min(0.94 * W / (re_.max() - re_.min()), 0.94 * H / (im_.max() - im_.min()))
    P = np.column_stack([W / 2 + (re_ - cx) * sc, H / 2 - (im_ - cy) * sc])
    keep = _rdp(P, 0.12)
    Q = P[keep]
    K = np.array_split(np.arange(len(Q) - 1), chunks)
    s = SVG(W, H, "The curve t -> zeta(1/2 + it)",
            f"Computed curve of zeta(1/2 + it) for 0 <= t <= {t_max:g} in the complex plane; it passes through the "
            f"origin at each of the {len(zeros)} zeros on the critical line in that range.", bg=None)
    lo, hi = np.array([0x64, 0x74, 0x8b]), np.array([0x7d, 0xb4, 0xff])   # slate -> blue
    for j, idx in enumerate(K):
        if len(idx) == 0:
            continue
        u = j / max(chunks - 1, 1)
        col = "#%02x%02x%02x" % tuple(int(round(v)) for v in lo + (hi - lo) * u)
        seg = Q[idx[0]:idx[-1] + 2]
        d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in seg)
        s.path(d, stroke=col, sw=0.8, opacity=0.35 + 0.6 * u)
    ox, oy = W / 2 - cx * sc, H / 2 + cy * sc
    s.circle(ox, oy, 3.2, fill="#e2e8f0", opacity=0.95)
    save("hero-zeta", s)
    size = (OUT / "hero-zeta.svg").stat().st_size
    if size > 150_000:
        raise SystemExit(f"hero_zeta: {size} bytes exceeds 150 KB")
    FACTS["hero_zeta"] = {"t_max": t_max, "n_zeros": len(zeros), "zeros": [round(g, 6) for g in zeros],
                          "samples": int(len(ts)),
                          "method": f"zeta(1/2+it) by Euler-Maclaurin on a grid of step {dt:g}, simplified to "
                                    f"{len(Q)} points (Douglas-Peucker, 0.12 px); zeros from sign changes of "
                                    f"Hardy's Z for t >= 10, refined by bisection and checked against zeta_zeros",
                          "svg_bytes": size}


def main() -> int:
    args = sys.argv[1:]
    only = args[args.index("--only") + 1] if "--only" in args else None
    t_max = float(args[args.index("--tmax") + 1]) if "--tmax" in args else 80.0
    if only == "hero_zeta":
        fp = OUT / "facts.json"
        if fp.exists():
            FACTS.update(json.loads(fp.read_text(encoding="utf-8")))
        fig_hero_zeta(t_max)
        fp.write_text(json.dumps(FACTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"hero_zeta: T={t_max:g}, {FACTS['hero_zeta']['n_zeros']} zeros, {FACTS['hero_zeta']['svg_bytes']} bytes")
        return 0
    ps = rhlib.PrimeSums.build(10_000_000)
    zeros = rhlib.zeta_zeros(100)
    assert abs(zeros[0] - 14.134725) < 1e-5 and abs(zeros[99] - 236.524230) < 1e-5
    FACTS["zeros"] = {"count": len(zeros), "first": round(zeros[0], 6), "hundredth": round(zeros[99], 6)}
    fig_hero_zeta(t_max)
    fig_hero(ps)
    fig_explicit(ps, zeros)
    fig_strip(zeros)
    fig_ramp(ps)
    fig_residue()
    fig_spotlight()
    fig_balance()
    fig_windows()
    fig_behrend()
    fig_chain()
    fig_galois()
    fig_choreography()
    FACTS["generated_by"] = "scripts/build_figures.py"
    (OUT / "facts.json").write_text(json.dumps(FACTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"figures: {len(list(OUT.glob('*.svg')))} SVG files; facts.json with {len(FACTS)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
