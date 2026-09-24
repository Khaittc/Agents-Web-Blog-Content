# LATEX FORMULA SKILL FOR TECHNICAL CONTENT AGENTS
Version: 1.0
Status: Test version
Primary use: Technical blog / solution / engineering content
Target rendering environment: Website supporting LaTeX rendered from CKEditor content

---

# 1. PURPOSE

This Skill defines how an Agent must create, validate, explain, and insert mathematical and engineering formulas into technical articles.

The Skill is intended for content involving:

- Electrical Engineering
- Automation
- Industrial Control
- Energy Management
- Motor Systems
- Power Systems
- Instrumentation
- Industrial IoT
- Mechanical / Process calculations
- General engineering calculations

The Skill standardizes formula generation so that all formulas are:

- mathematically correct;
- syntactically valid LaTeX;
- readable on the website;
- consistent with engineering notation;
- accompanied by variable definitions and units;
- compatible with citation/review workflows;
- safe from invented equation references.

---

# 2. SOURCE RENDERING BASIS

The website has been verified to render LaTeX content using a structure based on:

```latex
\documentclass[12pt,a4paper]{article}

\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

% Formula content

\end{document}
```

The verified source also uses the `equation` environment for displayed mathematical formulas.

Therefore this Skill adopts:

```text
amsmath
+
amssymb
+
equation
+
aligned
```

as the canonical LaTeX formula standard for Agents.

---

# 3. CORE RULE

All mathematical and engineering formulas intended for publication must be generated in LaTeX.

Preferred form:

```latex
\begin{equation}
...
\end{equation}
```

For multiple aligned lines:

```latex
\begin{equation}
\begin{aligned}
...
\end{aligned}
\end{equation}
```

Do not replace publication formulas with:

- plain-text slash fractions;
- Unicode pseudo-math;
- screenshots;
- formula images;
- HTML tables;
- MathML;
- improvised spacing with HTML;
- ASCII-art equations.

---

# 4. FORMULA WORKFLOW

The Agent must follow this sequence:

```text
Technical concept
        ↓
Determine whether a formula is necessary
        ↓
Identify variables
        ↓
Identify units
        ↓
Identify assumptions / conditions
        ↓
Generate LaTeX
        ↓
Validate mathematics
        ↓
Validate dimensional consistency
        ↓
Attach source citation if required
        ↓
Create worked example if useful
        ↓
Explain interpretation
```

---

# 5. WHEN TO USE A FORMULA

Use a formula when it improves technical understanding.

Appropriate cases include:

- load factor;
- efficiency;
- electrical power;
- energy consumption;
- power factor relationships;
- percentage calculations;
- voltage/current relationships;
- engineering ratios;
- statistical calculations;
- performance metrics;
- design calculations;
- conversion equations;
- control relationships;
- physical relationships.

Do not insert formulas merely to make an article look more technical.

---

# 6. DISPLAY FORMULA STANDARD

## 6.1. Single-line formula

Use:

```latex
\begin{equation}
L = \frac{P_{\mathrm{out}}}{P_{\mathrm{rated}}} \times 100\%
\end{equation}
```

---

## 6.2. Multi-line aligned formula

Use:

```latex
\begin{equation}
\begin{aligned}
P_{\mathrm{in}}
&= \sqrt{3}\,U_{\mathrm{LL}}I_{\mathrm{L}}\cos\varphi \\
P_{\mathrm{out}}
&= \eta P_{\mathrm{in}}
\end{aligned}
\end{equation}
```

Use `aligned` only when the expressions belong logically together.

Do not create separate equation blocks merely because one relationship spans several lines.

---

# 7. FRACTIONS

Use:

```latex
\frac{a}{b}
```

Preferred:

```latex
\frac{P_{\mathrm{out}}}{P_{\mathrm{rated}}}
```

Avoid:

```text
P_out / P_rated
```

for a displayed publication formula.

Plain `/` may still be acceptable inside explanatory prose when the expression is not being presented as a formal formula.

---

# 8. SUBSCRIPTS AND SUPERSCRIPTS

Use braces for multi-character subscripts:

```latex
P_{\mathrm{out}}
P_{\mathrm{rated}}
I_{\mathrm{rated}}
U_{\mathrm{LL}}
T_{\mathrm{avg}}
```

Use:

```latex
x^2
P^2
```

and:

```latex
x^{n+1}
```

for multi-character superscripts.

Do not write engineering symbols as:

```text
Prated
Pout
Irated
```

inside the formal equation when semantic subscripts improve readability.

---

# 9. GREEK SYMBOLS

Use LaTeX commands:

```latex
\eta
\varphi
\omega
\theta
\lambda
\Delta
\sigma
\mu
\pi
```

Examples:

```latex
\cos\varphi
```

```latex
\eta P_{\mathrm{in}}
```

Prefer LaTeX symbol commands instead of manually pasted Unicode Greek characters inside formula source.

---

# 10. OPERATORS AND FUNCTIONS

Use standard LaTeX functions:

```latex
\sin
\cos
\tan
\log
\ln
\exp
\lim
\max
\min
```

Do not fake functions as ordinary italic variable strings when a standard operator exists.

Correct:

```latex
\cos\varphi
```

Preferred over:

```latex
cos\varphi
```

---

# 11. ROOTS

Use:

```latex
\sqrt{x}
```

Example:

```latex
\sqrt{3}
```

For nth roots:

```latex
\sqrt[n]{x}
```

---

# 12. SUMMATION, INTEGRATION, LIMITS

Use standard LaTeX syntax:

```latex
\sum_{k=1}^{n}
```

```latex
\int_{a}^{b} f(x)\,dx
```

```latex
\lim_{h \to 0}
```

Use thin spacing before differential terms when appropriate:

```latex
\,dx
```

---

# 13. PERCENTAGE

The `%` character must be escaped:

```latex
100\%
```

Correct:

```latex
L = \frac{P_{\mathrm{out}}}{P_{\mathrm{rated}}}\times100\%
```

Incorrect:

```latex
L = \frac{P_{\mathrm{out}}}{P_{\mathrm{rated}}}\times100%
```

because `%` is a comment marker in LaTeX.

---

# 14. UNITS

Units must be typeset as upright text.

Use:

```latex
\mathrm{kW}
\mathrm{W}
\mathrm{V}
\mathrm{A}
\mathrm{kWh}
\mathrm{Hz}
\mathrm{rpm}
\mathrm{N\,m}
```

Example:

```latex
P = 30\,\mathrm{kW}
```

Use a thin space between numerical value and unit:

```latex
\,
```

Example:

```latex
400\,\mathrm{V}
```

Avoid:

```latex
400V
```

in a formal equation when the value and unit appear inside mathematical notation.

---

# 15. VARIABLE DEFINITIONS

Every non-trivial formula must be followed by a variable-definition section.

Recommended article form:

```text
Trong đó:

L — Hệ số tải của động cơ, %.
Pout — Công suất cơ đầu ra của động cơ, kW.
Prated — Công suất định mức của động cơ, kW.
```

The Agent must define:

- every important symbol;
- physical meaning;
- engineering unit where applicable.

Do not force a unit onto dimensionless quantities.

Examples:

```text
η — Hiệu suất, dimensionless hoặc % tùy cách biểu diễn.
cosφ — Hệ số công suất, dimensionless.
```

---

# 16. VARIABLE NAMING POLICY

Use symbols that are:

- conventional;
- concise;
- unambiguous;
- stable throughout the article.

Do not use the same symbol for two different quantities.

Example:

If:

```text
P_in = input power
```

then do not later use:

```text
P_in = rated power
```

The Agent must maintain a formula symbol registry for articles containing several formulas.

---

# 17. SYMBOL REGISTRY

For complex articles, maintain internally:

```yaml
symbols:
  - symbol: L
    meaning: Motor load factor
    unit: "%"
  - symbol: P_in
    meaning: Electrical input power
    unit: "kW"
  - symbol: P_out
    meaning: Mechanical output power
    unit: "kW"
  - symbol: P_rated
    meaning: Rated mechanical output power
    unit: "kW"
  - symbol: eta
    latex: "\\eta"
    meaning: Motor efficiency
    unit: "dimensionless"
```

The symbol registry is internal unless requested.

---

# 18. ENGINEERING NOTATION

Prefer engineering notation consistent with the field.

Examples:

Three-phase active power:

```latex
\begin{equation}
P
=
\sqrt{3}\,
U_{\mathrm{LL}}\,
I_{\mathrm{L}}\,
\cos\varphi
\end{equation}
```

Mechanical output from efficiency:

```latex
\begin{equation}
P_{\mathrm{out}}
=
\eta P_{\mathrm{in}}
\end{equation}
```

Motor load factor:

```latex
\begin{equation}
L
=
\frac{P_{\mathrm{out}}}
{P_{\mathrm{rated}}}
\times100\%
\end{equation}
```

These are examples of syntax and structure.

The Agent must still verify the technical applicability of any formula before using it.

---

# 19. FORMULA CONTEXT

A formula must not appear without context.

Required structure:

```text
Purpose / explanation
        ↓
Formula
        ↓
Variable definitions
        ↓
Units
        ↓
Assumptions / conditions
        ↓
Citation if required
        ↓
Worked example if useful
        ↓
Interpretation
```

Avoid:

```text
Heading
Formula
Next heading
```

with no explanation.

---

# 20. ASSUMPTIONS AND CONDITIONS

The Agent must state assumptions when they materially affect interpretation.

Examples:

- steady-state operation;
- balanced three-phase system;
- sinusoidal supply;
- measured RMS values;
- constant efficiency assumption;
- same unit basis;
- rated data from nameplate;
- estimated versus measured values.

Do not hide assumptions inside the formula.

For Blog content, assumptions should normally be explained in prose immediately after the formula.

---

# 21. DIMENSIONAL CONSISTENCY

The Agent must check dimensional consistency.

Example:

```text
E = P × t
```

If:

```text
P = kW
t = h
```

then:

```text
E = kWh
```

The Agent must detect errors such as:

```text
kW + A
```

or mixing:

```text
W
```

with:

```text
kW
```

without conversion.

---

# 22. UNIT CONVERSION

If different unit scales are used, convert explicitly.

Example:

```latex
\begin{equation}
P_{\mathrm{kW}}
=
\frac{P_{\mathrm{W}}}{1000}
\end{equation}
```

Do not silently mix:

```text
750 W
```

with:

```text
2.2 kW
```

inside one calculation.

---

# 23. DECIMAL VERSUS PERCENT FORM

The Agent must distinguish:

```text
η = 0.90
```

from:

```text
η = 90%
```

Do not substitute one for the other without conversion.

Example:

```latex
\eta = 0.90
```

and:

```latex
\eta_{\%} = 90\%
```

are different representations of the same efficiency value.

---

# 24. FORMULA NUMBERING IN THE ARTICLE

Formula numbering in the article is separate from source citation numbering.

If the rendering system automatically numbers:

```latex
\begin{equation}
...
\end{equation}
```

then `(1)`, `(2)`, `(3)` belong to the current article.

These numbers do not indicate source equations.

Never assume:

```text
Article equation (1)
=
Source [3, eq. (1)]
```

The two numbering systems are independent.

---

# 25. WHEN TO NUMBER FORMULAS

Do not number formulas merely because LaTeX can do so.

Numbering is useful when:

- the article contains multiple equations;
- later text refers back to an equation;
- a worked example reuses an earlier formula;
- the article is strongly calculation-oriented.

If the website renderer numbers all `equation` environments automatically, keep the numbering consistent and do not manually duplicate equation numbers in prose unless necessary.

---

# 26. INLINE FORMULAS

For short mathematical expressions inside prose, use inline LaTeX only if the website rendering workflow supports it reliably.

Examples conceptually:

```latex
\( P_{\mathrm{out}} \)
```

```latex
\( \eta = 0.9 \)
```

If inline rendering has not been validated on the website, prefer prose plus displayed formulas rather than inventing an unsupported inline format.

This Skill treats displayed formulas as the primary verified format.

---

# 27. CITATION INTEGRATION

Formula citation is controlled by the IEEE Citation & Reference Skill.

Citation must remain outside the LaTeX formula.

Correct:

```text
Hệ số tải có thể được xác định theo quan hệ sau [1].

[LaTeX formula]
```

Do not place:

```text
[1]
```

inside the equation environment.

Incorrect:

```latex
\begin{equation}
L = ... [1]
\end{equation}
```

---

# 28. SOURCE FORMULA POLICY

## 28.1. Formula directly from a source

If the formula is taken directly from a source:

```text
Citation required.
```

Example prose:

```text
Hệ số tải được xác định theo quan hệ sau [1].
```

---

## 28.2. Formula adapted from a source

If the Agent algebraically transforms or adapts a sourced relationship:

- cite the supporting source;
- explain the transformation when material;
- do not imply the transformed expression is printed exactly that way in the source unless verified.

---

## 28.3. Formula derived within the article

If the formula is purely an algebraic derivation from already defined values:

- no artificial source citation is required for the algebra itself;
- externally sourced constants, assumptions, thresholds, or input data still require citation.

---

# 29. IEEE LOCATOR INTEGRATION

If the IEEE Citation Skill confirms:

```text
LOCATOR_VERIFIED
```

the prose may use:

```text
[1, eq. (4)]
```

Example:

```text
Quan hệ này được trình bày trong [1, eq. (4)].
```

If the source equation number is not directly verified:

```text
use [1]
```

The Formula Agent must never invent:

```text
eq. (1)
eq. (2)
```

for the source.

Article equation numbers and source equation locators are independent.

---

# 30. WORKED EXAMPLES

A worked example must be clearly classified as one of:

```text
REAL DATA
SOURCE DATA
ILLUSTRATIVE ASSUMPTION
```

---

## 30.1. Real data

Use only when provided or verified.

Example label:

```text
Ví dụ từ dữ liệu đo thực tế:
```

---

## 30.2. Source data

Use citation.

Example:

```text
Sử dụng dữ liệu trong [2], ...
```

---

## 30.3. Illustrative assumption

Clearly label:

```text
Ví dụ minh họa:
```

or:

```text
Giả sử:
```

The Agent must not present invented values as measured plant data.

---

# 31. NUMERICAL DATA POLICY

The Agent must never invent a measured value, manufacturer value, efficiency value, threshold, or standard limit and present it as factual.

If a number is created only to demonstrate a formula:

```text
label it as illustrative / assumed
```

Example:

```text
Giả sử động cơ có công suất định mức 75 kW...
```

This is acceptable.

Do not write:

```text
Động cơ trong nhà máy có công suất 75 kW...
```

unless that is supported by real/source data.

---

# 32. SIGNIFICANT FIGURES

Do not report calculated results with unjustified precision.

Example:

Input:

```text
75 kW
30 kW
```

Do not automatically output:

```text
40.000000%
```

Prefer:

```text
40%
```

unless the calculation context requires more precision.

---

# 33. ROUNDING

Round only after completing the calculation unless the method requires intermediate rounding.

State rounding when it materially affects the result.

Do not introduce false precision.

---

# 34. EQUATION LABELS

Do not use custom `\label{}` and `\ref{}` unless the website rendering pipeline has been explicitly verified to support them.

Default Skill behavior:

```text
Do not generate \label or \ref.
```

Use the normal `equation` environment and article prose.

---

# 35. DISALLOWED LATEX FEATURES BY DEFAULT

Unless separately validated on the website, do not use:

```latex
\includegraphics
\input
\include
\write
\newcommand
\renewcommand
\def
\usepackage{...}
```

inside formula output.

Do not create custom macros.

Only use syntax supported by:

```text
amsmath
amssymb
```

unless another package has been explicitly approved.

---

# 36. SECURITY / CONTENT SAFETY

Do not generate LaTeX commands intended to:

- read files;
- write files;
- execute shell commands;
- include external files;
- redefine document behavior;
- modify renderer configuration.

The formula output must contain mathematical content only.

---

# 37. CANONICAL OUTPUT FOR A FORMULA

For each important formula, the Agent should internally produce:

```yaml
formula_id: EQ-001
title: ""
purpose: ""
latex: |
  \begin{equation}
  ...
  \end{equation}
variables:
  - symbol: ""
    meaning: ""
    unit: ""
assumptions: []
source_references: []
source_locator_status: ""
example_type: NONE | REAL_DATA | SOURCE_DATA | ILLUSTRATIVE_ASSUMPTION
validation_status: PASS | REVIEW_REQUIRED | FAIL
```

Only the human-readable formula and explanation need to appear in the published article.

---

# 38. EXAMPLE — MOTOR LOAD FACTOR

## Explanation

Hệ số tải biểu thị tỷ lệ giữa công suất cơ đầu ra tại điều kiện vận hành và công suất cơ định mức.

## LaTeX

```latex
\begin{equation}
L
=
\frac{P_{\mathrm{out}}}
{P_{\mathrm{rated}}}
\times100\%
\end{equation}
```

## Variables

```text
L — Hệ số tải, %.
Pout — Công suất cơ đầu ra, kW.
Prated — Công suất cơ định mức, kW.
```

## Validation

```text
Pout and Prated must use the same power unit.
Prated > 0.
```

---

# 39. EXAMPLE — THREE-PHASE ACTIVE POWER

## LaTeX

```latex
\begin{equation}
P_{\mathrm{in}}
=
\sqrt{3}\,
U_{\mathrm{LL}}\,
I_{\mathrm{L}}\,
\cos\varphi
\end{equation}
```

## Variables

```text
Pin — Công suất tác dụng đầu vào.
ULL — Điện áp dây-dây.
IL — Dòng điện dây.
cosφ — Hệ số công suất.
```

The Agent must state the applicable assumptions before presenting this as a general relationship in a technical article.

---

# 40. EXAMPLE — OUTPUT POWER USING EFFICIENCY

```latex
\begin{equation}
P_{\mathrm{out}}
=
\eta P_{\mathrm{in}}
\end{equation}
```

Variables:

```text
Pout — Mechanical output power.
Pin — Electrical input power.
η — Efficiency in decimal form.
```

If efficiency is given as a percentage:

```text
90% → 0.90
```

before applying the equation.

---

# 41. EXAMPLE — ENERGY

```latex
\begin{equation}
E = P t
\end{equation}
```

If:

```text
P = kW
t = h
```

then:

```text
E = kWh
```

---

# 42. FORMULA REVIEW GATE

Before a formula is accepted, the Agent must verify:

```text
1. Is the formula technically necessary?
2. Is the mathematics correct?
3. Is the LaTeX syntax valid?
4. Are braces balanced?
5. Are variables consistent?
6. Are all variables defined?
7. Are units defined where applicable?
8. Are dimensions consistent?
9. Are percentage/decimal forms handled correctly?
10. Are assumptions stated?
11. Are sourced formulas cited?
12. Are source equation locators verified before use?
13. Are numerical values real, sourced, or explicitly illustrative?
14. Is numerical precision reasonable?
15. Does the formula use only approved LaTeX features?
```

If any critical item fails:

```text
FORMULA_REVIEW_REQUIRED
```

---

# 43. FORMULA AUDIT FAILURE CONDITIONS

The formula must fail review if any of the following occurs:

- invalid LaTeX;
- undefined important variable;
- inconsistent variable meaning;
- incompatible units;
- invented measured data;
- invented technical threshold;
- invented source equation number;
- citation placed inside the formula;
- unsupported LaTeX package dependency;
- malformed fraction;
- unescaped `%`;
- false precision;
- formula contradicts the article explanation;
- formula applicability conditions are omitted when material.

---

# 44. AGENT OUTPUT CONTRACT

When requested to create a technical article containing formulas, the Agent should output:

```text
ARTICLE PROSE

FORMULA
- LaTeX equation

VARIABLE DEFINITIONS

ASSUMPTIONS / CONDITIONS

SOURCE CITATION
- when required

WORKED EXAMPLE
- when useful

INTERPRETATION
```

When requested for review/debug output, also provide:

```text
FORMULA ID
SYMBOL REGISTRY
UNIT CHECK
SOURCE STATUS
LOCATOR STATUS
FORMULA AUDIT RESULT
```

---

# 45. INTEGRATION WITH BLOG CONTENT STANDARD

The Blog Agent should invoke this Skill when:

- a formula is required;
- a formula already exists and must be checked;
- a calculation example is added;
- numerical engineering relationships are introduced;
- variables or units must be standardized.

The Blog structure itself remains controlled by:

```text
BLOG CONTENT STRUCTURE STANDARD
```

This Skill controls only formula-related content.

---

# 46. INTEGRATION WITH IEEE CITATION SKILL

Use:

```text
LATEX FORMULA SKILL
```

for:

- mathematical syntax;
- symbols;
- units;
- formula explanation;
- formula validation;
- worked examples.

Use:

```text
IEEE CITATION & REFERENCE SKILL
```

for:

- `[n]`;
- verified `[n, eq. (x)]`;
- source identification;
- reference formatting;
- citation audit.

Do not duplicate IEEE reference logic inside the Formula Skill.

---

# 47. AGENT FINAL CHECKLIST

Before returning formula-complete content:

- [ ] Formula is written in LaTeX.
- [ ] Display formula uses `equation`.
- [ ] Multi-line formula uses `aligned` inside `equation` when appropriate.
- [ ] Fractions use `\frac`.
- [ ] Greek symbols use LaTeX commands.
- [ ] `%` is escaped as `\%`.
- [ ] Units are upright using `\mathrm{}` when inside math.
- [ ] Important variables are defined.
- [ ] Units are stated.
- [ ] Variable symbols are consistent across the article.
- [ ] Dimensional consistency has been checked.
- [ ] Assumptions/conditions are stated when material.
- [ ] Source-derived formulas have citations.
- [ ] Source equation locator is used only when verified by the IEEE Skill.
- [ ] Citation is not embedded inside LaTeX.
- [ ] Numerical example is identified as real, sourced, or illustrative.
- [ ] No measured data has been invented.
- [ ] No threshold has been invented.
- [ ] Precision and rounding are reasonable.
- [ ] No unsupported custom package or macro is used.
- [ ] Formula audit passes.

---

# 48. IMPLEMENTATION PRINCIPLE

Correct Agent behavior:

```text
Engineering statement
        ↓
Need mathematical relationship?
        ↓
YES
        ↓
Create canonical LaTeX
        ↓
Define symbols and units
        ↓
Validate engineering meaning
        ↓
Check dimensional consistency
        ↓
Call IEEE Citation Skill if sourced
        ↓
Insert into article
```

Incorrect behavior:

```text
Need formula
        ↓
Generate visually plausible equation
        ↓
Invent variable meanings
        ↓
Invent source equation number
        ↓
Publish
```

The goal is not merely to render mathematics.

The goal is to produce **reviewable, technically consistent, source-aware engineering formulas**.
