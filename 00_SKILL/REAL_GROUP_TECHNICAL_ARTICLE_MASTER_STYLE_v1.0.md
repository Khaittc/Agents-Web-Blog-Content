# REAL GROUP TECHNICAL ARTICLE — MASTER STYLE
Version: 1.0
Status: Baseline derived from the published motor-underload article
Target editor: CKEditor 3.6.6.2
Primary targets: Blog / Solution technical articles
Website: real-group.org

---

# 1. PURPOSE

This Master Style is the canonical presentation standard for technical articles created by Agents for Real Group.

It controls:

- HTML structure used inside CKEditor;
- typography;
- spacing;
- heading hierarchy;
- paragraph styling;
- lists;
- tables;
- LaTeX formula presentation;
- Technical Note / Limitation / Warning callouts;
- figures and captions;
- citation appearance;
- reference-list appearance;
- responsive behavior;
- visual consistency between future articles.

This Master Style does **not** replace:

- `BLOG_CONTENT_STRUCTURE_STANDARD`
- `IEEE_CITATION_REFERENCE_SKILL`
- `LATEX_FORMULA_SKILL`

Those standards control content structure, citations/references, and mathematical correctness.

This file controls the **presentation layer**.

---

# 2. RULE PRECEDENCE

Agents must use the following separation of responsibilities:

```text
BLOG CONTENT STRUCTURE STANDARD
        ↓
What sections/content are required?

IEEE CITATION & REFERENCE SKILL
        ↓
How are sources cited and referenced?

LATEX FORMULA SKILL
        ↓
How are formulas constructed and validated?

REAL GROUP TECHNICAL ARTICLE MASTER STYLE
        ↓
How is the final article rendered in CKEditor HTML?
```

If another Skill proposes visual styling that conflicts with this Master Style:

```text
MASTER STYLE controls presentation.
```

It must not override the technical/citation rules of the specialist Skills.

---

# 3. OUTPUT PACKAGE

Agents should separate publication metadata from CKEditor content.

## 3.1. Review package

The review artifact may contain:

1. Tiêu đề
2. Meta Title
3. Keyword Tag
4. Description Tag
5. Featured Image
6. Mô tả
7. Nội dung bài viết
8. Content image specifications
9. Tài liệu tham khảo
10. Citation / Formula review information when requested

## 3.2. CKEditor HTML

The CKEditor HTML must contain **only the public article content**.

Start with:

```html
<div style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:1.7;color:#243447;">
```

End with:

```html
</div>
```

Do not place internal review reports, Agent instructions, source registries, locator verification statuses, or implementation notes in the public article.

HTML comments may be used during draft/review, but unresolved implementation comments must be removed or resolved before publication.

---

# 4. MASTER DESIGN PRINCIPLES

## 4.1. Engineering-first presentation

The visual hierarchy must support:

```text
READ
→ UNDERSTAND
→ VERIFY
→ APPLY
```

Do not add decoration merely to make the page look more complex.

## 4.2. Use whitespace before boxes

Default hierarchy should come from:

- heading size;
- spacing;
- paragraph grouping;
- tables where appropriate;
- meaningful figures.

Do not turn every formula, example, paragraph, or data block into a card.

## 4.3. Semantic color only

Background colors are reserved for semantic elements:

- Technical Note;
- Limitation / Caution;
- Warning / Safety;
- table header.

Normal prose, formulas, variable definitions, calculations, citations, and references must not receive decorative fills.

---

# 5. COLOR TOKENS

Use only the following default palette unless a future site-wide design update explicitly replaces it.

```text
Body text                  #243447
Primary heading blue       #28658c
Secondary heading blue     #184f73

Table header background    #eaf2f7
Table header border        #ccd8e0
Table body border          #d7e0e7

Technical Note background  #eef5fa
Technical Note border      #2f6f9f
Technical Note label       #1f5273

Caution background         #fff7e8
Caution border             #d59020
Caution label              #8a5a0a

Warning background         #fff1f0
Warning border             #b8443c
Warning label              #8e302b

Caption / secondary text   #526577
Horizontal rule            #d4dde4
```

Do not introduce arbitrary new colors per article.

---

# 6. ROOT ARTICLE CONTAINER

Canonical root:

```html
<div style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:1.7;color:#243447;">
    ...
</div>
```

Rules:

- no fixed width;
- no root background;
- no root border;
- no root padding;
- no fixed height;
- no Grid;
- no Flexbox dependency;
- no absolute/fixed positioning.

The website layout controls article width.

---

# 7. TYPOGRAPHY

## 7.1. Body

```text
Font family : Arial, Helvetica, sans-serif
Font size   : 16px
Line height : 1.7
Color       : #243447
```

## 7.2. Lead paragraph

The first public content paragraph may use:

```html
<p style="font-size:17px;margin:0 0 16px 0;">
```

Use only for the opening paragraph.

Do not enlarge every introductory paragraph.

## 7.3. Bold

Use `<strong>` only to emphasize:

- technical terms;
- key decision points;
- variables in HTML definitions;
- important distinctions.

Do not bold entire paragraphs.

## 7.4. Italic

Use `<em>` for:

- source-data captions;
- restrained explanatory emphasis.

Do not use italic as a substitute for headings.

---

# 8. HEADING SYSTEM

## 8.1. H2

Canonical:

```html
<h2 style="font-size:24px;line-height:1.35;color:#28658c;margin:34px 0 14px 0;">
    1. Section title
</h2>
```

Rules:

- H2 represents a primary article section.
- Number primary technical sections when the article structure benefits from numbering.
- Keep numbering sequential.
- Do not skip H2 levels.

## 8.2. H3

Canonical:

```html
<h3 style="font-size:19px;color:#184f73;margin:24px 0 10px 0;">
    4.1. Subsection title
</h3>
```

Rules:

- Use H3 only below an H2.
- Use for technical sub-methods, alternatives, steps, or analysis dimensions.
- Do not use H3 only for visual emphasis.

## 8.3. H4

Avoid by default.

Use only when a section genuinely requires a third structural depth.

Do not create deep heading hierarchies for short Blog articles.

---

# 9. PARAGRAPH SPACING SYSTEM

Use a small controlled set of paragraph spacing variants.

## 9.1. Standard paragraph

```html
<p style="margin:0 0 14px 0;">
```

Default for normal prose.

## 9.2. Section-ending paragraph

```html
<p style="margin:0 0 18px 0;">
```

Use before a new subsection/structural transition when a little more separation is useful.

## 9.3. Formula-introduction paragraph

```html
<p style="margin:0 0 10px 0;">
```

Use immediately before a LaTeX formula.

## 9.4. Variable label

```html
<p style="margin:0 0 8px 0;"><strong>Trong đó:</strong></p>
```

Do not invent many slightly different margin values.

---

# 10. LISTS

## 10.1. Standard unordered list

```html
<ul style="margin:0 0 18px 22px;padding:0;">
    <li>...</li>
</ul>
```

For variable-definition lists immediately after a formula:

```html
<ul style="margin:0 0 14px 22px;padding:0;">
```

## 10.2. Ordered procedure

```html
<ol style="margin:0 0 20px 24px;padding:0;">
    <li style="margin-bottom:8px;">...</li>
    <li>...</li>
</ol>
```

Use ordered lists for:

- measurement procedures;
- troubleshooting sequences;
- workflows;
- execution order.

Do not use ordered lists when items have no sequence.

---

# 11. LATEX FORMULA PRESENTATION

Formula correctness is controlled by `LATEX_FORMULA_SKILL`.

This section controls visual placement only.

## 11.1. Canonical formula wrapper

Use exactly this baseline:

```html
<div style="margin:6px 0 10px 0;text-align:center;overflow-x:auto;">
\begin{equation}
...
\end{equation}
</div>
```

This formula wrapper was validated in the motor-underload article.

## 11.2. HARD RULE — NO FORMULA CARD

The formula wrapper must NOT contain:

```text
background
border
border-left
box-shadow
padding
font-family:Consolas
font-family:Courier
```

Do not make formulas look like source-code blocks or information cards.

## 11.3. HARD RULE — NO WHITE-SPACE STYLE

Do not set:

```css
white-space: pre;
white-space: pre-wrap;
white-space: nowrap;
```

on the formula wrapper.

The validated baseline intentionally omits the `white-space` property to avoid unnecessary vertical whitespace around rendered formulas.

## 11.4. Formula alignment

Default:

```text
center
```

Do not left-align formulas unless a future design requirement explicitly calls for it.

## 11.5. Multi-line formulas

Still use the same HTML wrapper.

LaTeX handles internal alignment:

```latex
\begin{equation}
\begin{aligned}
...
\end{aligned}
\end{equation}
```

Do not change the HTML style because the equation contains multiple lines.

## 11.6. Citation placement

Citation stays in the prose before/after the formula according to the IEEE Skill.

Do not style citations inside the formula.

---

# 12. VARIABLE DEFINITIONS AFTER FORMULAS

Preferred pattern:

```html
<p style="margin:0 0 8px 0;"><strong>Trong đó:</strong></p>

<ul style="margin:0 0 14px 22px;padding:0;">
    <li><strong>P<sub>in</sub></strong>: ...</li>
    <li><strong>U<sub>LL</sub></strong>: ...</li>
</ul>
```

Rules:

- no colored box;
- no border;
- no monospace block;
- no separate background;
- keep definitions directly adjacent to the formula.

---

# 13. WORKED EXAMPLES

Worked examples are technical content, not code blocks.

Preferred flow:

```text
Intro sentence
↓
Input data table or bullet list
↓
Formula-introduction sentence
↓
LaTeX formula
↓
Result interpretation
```

## 13.1. Input values

Prefer normal HTML bullets:

```html
<ul style="margin:0 0 16px 22px;padding:0;">
    <li><strong>U<sub>LL</sub></strong> = 469,7 V.</li>
    <li><strong>I<sub>L</sub></strong> = 37 A.</li>
</ul>
```

or a table when there are many measured values.

Do not present normal engineering input values inside a gray monospace/code card.

## 13.2. Calculations

Use the canonical formula wrapper.

Do not add a special gray box around the calculation.

---

# 14. TABLE STYLE

## 14.1. Wrapper

```html
<div style="overflow-x:auto;margin:14px 0 20px 0;">
    ...
</div>
```

Horizontal scrolling is required when necessary on smaller screens.

## 14.2. Table

```html
<table style="width:100%;border-collapse:collapse;min-width:760px;">
```

`min-width` may be adjusted based on column count:

```text
2–3 moderate columns : 650–760px
4 columns            : around 800px
```

Do not set a fixed pixel width for the table.

## 14.3. Header row

```html
<tr style="background:#eaf2f7;">
```

Header cells:

```html
<th style="border:1px solid #ccd8e0;padding:10px;text-align:left;color:#184f73;">
```

## 14.4. Body cells

```html
<td style="border:1px solid #d7e0e7;padding:10px;">
```

## 14.5. Table rules

- text-align left by default;
- numeric alignment may be adjusted when it improves readability;
- no zebra colors by default;
- no strong background fills in body rows;
- no decorative shadows;
- avoid very long paragraphs inside cells;
- unit information should be explicit.

---

# 15. TABLE SOURCE CAPTION

When a table uses sourced data, a compact source caption may appear immediately below it.

Canonical:

```html
<p style="margin:-8px 0 16px 0;font-size:14px;color:#526577;">
    <em>Source data: [1, p. 4].</em>
</p>
```

Citation details must comply with the IEEE Skill.

If a detailed locator is not verified:

```text
Source data: [1].
```

Do not invent page/table locators for the caption.

---

# 16. TECHNICAL NOTE

Use for:

- important engineering interpretation;
- non-obvious limitation;
- clarification that prevents common misunderstanding.

Canonical:

```html
<div style="background:#eef5fa;border-left:4px solid #2f6f9f;padding:14px 16px;margin:20px 0;">
    <strong style="color:#1f5273;">Technical Note:</strong><br>
    ...
</div>
```

Rules:

- use sparingly;
- usually no more than a few meaningful callouts per article;
- do not use Technical Note merely to highlight normal prose.

---

# 17. LIMITATION / CAUTION

Use for:

- calculation limitation;
- method limitation;
- condition where misinterpretation is likely;
- non-safety caution.

Canonical:

```html
<div style="background:#fff7e8;border-left:4px solid #d59020;padding:14px 16px;margin:20px 0;">
    <strong style="color:#8a5a0a;">Giới hạn của phép tính:</strong><br>
    ...
</div>
```

Alternative label may be:

```text
Lưu ý:
Caution:
Giới hạn:
```

provided the semantic meaning remains caution/limitation.

Do not use amber styling for ordinary notes.

---

# 18. WARNING / SAFETY

Reserved for actual safety/risk information.

Canonical:

```html
<div style="background:#fff1f0;border-left:4px solid #b8443c;padding:14px 16px;margin:22px 0;">
    <strong style="color:#8e302b;">Warning — An toàn khi đo:</strong><br>
    ...
</div>
```

Use only when:

- electrical safety is relevant;
- equipment damage risk exists;
- unsafe operation may result;
- the user could misapply the procedure in a hazardous way.

Do not use red warning styling for general recommendations.

---

# 19. CONTENT IMAGES

A technical Blog may use:

```text
0–3 content images
```

The number is determined by technical value, not page length.

## 19.1. Canonical image wrapper

```html
<div style="margin:24px 0;text-align:center;">
    <img src="IMAGE_URL"
         alt="Descriptive ALT text"
         style="max-width:100%;height:auto;" />
    <p style="margin:8px 0 0 0;font-size:14px;color:#526577;">
        Figure caption.
    </p>
</div>
```

Rules:

- no decorative border by default;
- no background card by default;
- no fixed image width in article HTML;
- `max-width:100%`;
- `height:auto`;
- ALT required;
- caption recommended for technical figures.

## 19.2. Draft placeholders

Drafts may contain:

```html
<!-- IMAGE_1: description -->
```

Before publication, every placeholder must be:

- replaced by the final image; or
- removed.

Do not publish unresolved image placeholders.

---

# 20. FEATURED IMAGE

Featured Image belongs to article metadata, not the CKEditor body.

Canonical size:

```text
808 × 500 px
```

Metadata must include:

```text
Filename
Size
ALT
Purpose
Image Prompt
```

Do not insert the Featured Image again in the body unless the website design explicitly requires it.

---

# 21. CITATION APPEARANCE

Citation logic is controlled by `IEEE_CITATION_REFERENCE_SKILL`.

Visual rules:

- citation stays inline with prose;
- same body font;
- same body color;
- do not bold citation numbers;
- do not add colored badges;
- do not place citations in separate boxes;
- no internal hyperlinks in Master Style v1.0 unless separately validated.

Examples:

```text
... ở vùng tải thấp [1].
```

```text
... theo quan hệ trong [1, eq. (1)].
```

Detailed locators are allowed only when verified by the IEEE Skill.

---

# 22. REFERENCE SECTION

## 22.1. Separator

Before References:

```html
<hr style="border:0;border-top:1px solid #d4dde4;margin:32px 0 24px 0;">
```

## 22.2. References heading

```html
<h2 style="font-size:24px;line-height:1.35;color:#28658c;margin:0 0 14px 0;">
    Tài liệu tham khảo
</h2>
```

## 22.3. Reference paragraph

Use hanging-indent style:

```html
<p style="margin:0 0 12px 0;padding-left:30px;text-indent:-30px;">
    [1] ...
</p>
```

## 22.4. Reference links

Canonical:

```html
<a href="SOURCE_URL"
   target="_blank"
   rel="noopener noreferrer"
   style="color:#28658c;text-decoration:none;">SOURCE_URL</a>
```

Do not add buttons/cards around reference links.

The bibliographic format itself is controlled by the IEEE Skill.

---

# 23. HORIZONTAL RULES

Use `<hr>` only for a major transition such as:

```text
Main article
→ References
```

Do not place horizontal rules between every H2 section.

Whitespace and headings provide normal separation.

---

# 24. HTML TAG ALLOWLIST

Preferred content tags:

```text
div
p
h2
h3
h4
strong
em
span
ul
ol
li
table
thead
tbody
tr
th
td
a
img
br
hr
```

LaTeX is stored as text inside the validated formula wrapper.

Avoid unnecessary nested `<div>` structures.

---

# 25. FORBIDDEN PRESENTATION PATTERNS

Agents must not introduce the following unless a future Master Style explicitly approves them.

## 25.1. Formula box styling

Forbidden:

```text
formula background fill
formula border
formula shadow
formula padding card
formula monospace wrapper
white-space property on formula wrapper
```

## 25.2. Decorative card proliferation

Do not put each of these in separate colored cards:

```text
formula
variables
worked example
normal paragraph
citation
reference
```

## 25.3. Arbitrary colors

Do not choose new colors per article.

## 25.4. Complex CSS

Do not use:

```text
display:grid
display:flex
position:absolute
position:fixed
animations
CSS variables
external style sheets
```

inside CKEditor article content.

## 25.5. JavaScript

Never generate:

```text
<script>
onclick=
onload=
onmouseover=
```

for article formatting.

---

# 26. RESPONSIVE RULES

The article must remain usable on mobile.

Required:

- root has no fixed width;
- images use `max-width:100%;height:auto`;
- wide tables are placed in `overflow-x:auto` wrappers;
- formulas use `overflow-x:auto`;
- no fixed-height containers;
- no absolute positioning.

Do not shrink technical tables until content becomes unreadable; horizontal scrolling is preferable.

---

# 27. PUBLIC CONTENT VS REVIEW CONTENT

The public article must not expose Agent implementation information.

Do not publish text such as:

```text
IEEE Skill: v1.2
LaTeX Skill: v1.0
LOCATOR_VERIFIED
Formula Audit: PASS
Citation Audit: PASS
STYLE REVIEW VARIANT
Agent reasoning
Implementation Review
```

These may exist in review artifacts or comments only.

Likewise, do not publish explanations such as:

```text
The article equation number is different from the source equation locator...
```

unless that distinction is itself materially relevant to the reader's technical understanding.

---

# 28. LANGUAGE STYLE AT THE PRESENTATION LAYER

Master Style does not force full Vietnamese translation of established engineering terms.

When technical English terms are useful:

```text
motor
part-load
full-load
power factor
VFD
operating profile
rated value
measured value
estimated value
```

they may appear naturally.

Presentation rules:

- avoid unnecessary quotation marks around common technical terms;
- use the same term consistently throughout one article;
- do not randomly switch between synonyms that refer to the same engineering quantity.

Terminology policy belongs primarily to the content standard, but inconsistent terminology is also a style failure.

---

# 29. BASELINE HTML COMPONENT LIBRARY

## 29.1. Root

```html
<div style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:1.7;color:#243447;">
```

## 29.2. Lead

```html
<p style="font-size:17px;margin:0 0 16px 0;">
    ...
</p>
```

## 29.3. Paragraph

```html
<p style="margin:0 0 14px 0;">
    ...
</p>
```

## 29.4. H2

```html
<h2 style="font-size:24px;line-height:1.35;color:#28658c;margin:34px 0 14px 0;">
    ...
</h2>
```

## 29.5. H3

```html
<h3 style="font-size:19px;color:#184f73;margin:24px 0 10px 0;">
    ...
</h3>
```

## 29.6. Formula

```html
<div style="margin:6px 0 10px 0;text-align:center;overflow-x:auto;">
\begin{equation}
...
\end{equation}
</div>
```

## 29.7. Table

```html
<div style="overflow-x:auto;margin:14px 0 20px 0;">
<table style="width:100%;border-collapse:collapse;min-width:760px;">
    <thead>
        <tr style="background:#eaf2f7;">
            <th style="border:1px solid #ccd8e0;padding:10px;text-align:left;color:#184f73;">...</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #d7e0e7;padding:10px;">...</td>
        </tr>
    </tbody>
</table>
</div>
```

## 29.8. Technical Note

```html
<div style="background:#eef5fa;border-left:4px solid #2f6f9f;padding:14px 16px;margin:20px 0;">
    <strong style="color:#1f5273;">Technical Note:</strong><br>
    ...
</div>
```

## 29.9. Caution

```html
<div style="background:#fff7e8;border-left:4px solid #d59020;padding:14px 16px;margin:20px 0;">
    <strong style="color:#8a5a0a;">Lưu ý:</strong><br>
    ...
</div>
```

## 29.10. Warning

```html
<div style="background:#fff1f0;border-left:4px solid #b8443c;padding:14px 16px;margin:22px 0;">
    <strong style="color:#8e302b;">Warning:</strong><br>
    ...
</div>
```

## 29.11. Figure

```html
<div style="margin:24px 0;text-align:center;">
    <img src="IMAGE_URL" alt="ALT_TEXT" style="max-width:100%;height:auto;" />
    <p style="margin:8px 0 0 0;font-size:14px;color:#526577;">
        Caption
    </p>
</div>
```

## 29.12. References separator

```html
<hr style="border:0;border-top:1px solid #d4dde4;margin:32px 0 24px 0;">
```

## 29.13. Reference entry

```html
<p style="margin:0 0 12px 0;padding-left:30px;text-indent:-30px;">
    [1] ...
</p>
```

---

# 30. ARTICLE STYLE AUDIT

Before returning final CKEditor HTML, the Agent must run the following audit.

## Typography

- [ ] Root uses Arial/Helvetica.
- [ ] Body font is 16px.
- [ ] Body line-height is 1.7.
- [ ] Body color is #243447.
- [ ] H2 matches Master Style.
- [ ] H3 matches Master Style.
- [ ] No arbitrary heading colors/sizes.

## Spacing

- [ ] Normal paragraphs use the approved margin system.
- [ ] H2/H3 spacing is consistent.
- [ ] No unnecessary `<br>` spacing hacks.
- [ ] No empty paragraphs used to create vertical space.

## Formulas

- [ ] Formula wrapper is `margin:6px 0 10px 0;text-align:center;overflow-x:auto`.
- [ ] Formula has no fill.
- [ ] Formula has no border.
- [ ] Formula has no padding card.
- [ ] Formula wrapper contains no `white-space` property.
- [ ] Formula is not displayed as source code.

## Tables

- [ ] Table wrapper uses horizontal overflow.
- [ ] Table uses `width:100%`.
- [ ] Table uses `border-collapse:collapse`.
- [ ] Header style matches Master Style.
- [ ] Body border style matches Master Style.
- [ ] No decorative body-row fill by default.

## Callouts

- [ ] Blue box is used only for Technical Note.
- [ ] Amber box is used only for caution/limitation.
- [ ] Red box is used only for actual warning/safety.
- [ ] Normal paragraphs are not converted into callouts.

## Images

- [ ] Content image count is 0–3.
- [ ] Every final image has ALT.
- [ ] Image is responsive.
- [ ] Technical figure has caption when appropriate.
- [ ] No unresolved `IMAGE_n` placeholders remain at publication.

## Citations

- [ ] Citation is inline, not boxed.
- [ ] Citation style follows IEEE Skill.
- [ ] Detailed locator is used only if verified.
- [ ] Citation is not visually restyled.

## References

- [ ] References are separated by one `<hr>`.
- [ ] Reference heading uses H2 style.
- [ ] Entries use hanging indent.
- [ ] Links use approved color and safe target attributes.
- [ ] Reference formatting follows IEEE Skill.

## Public-output hygiene

- [ ] No Skill version labels visible.
- [ ] No Agent review notes visible.
- [ ] No audit status visible.
- [ ] No source-registry metadata visible.
- [ ] No implementation comments visible unless intentionally retained for draft only.

---

# 31. MASTER STYLE CHANGE CONTROL

Agents must not modify Master Style values ad hoc.

If a future article appears to require a new style:

```text
Do not invent it inside that article.
```

Instead:

```text
Article test
→ Human review
→ Approve new component/style
→ Update MASTER STYLE version
→ Apply to future articles
```

Example:

```text
v1.0 → baseline from motor-underload article
v1.1 → only after a reviewed style change
```

This prevents visual drift between articles.

---

# 32. ACCEPTED BASELINE

The motor-underload article is the first visual baseline for this Master Style.

Key accepted patterns include:

```text
Root typography
H2/H3 hierarchy
Paragraph rhythm
Responsive tables
Blue Technical Note
Amber calculation limitation
Red safety Warning
IEEE References
Formula wrapper with:
    margin:6px 0 10px 0
    text-align:center
    overflow-x:auto
    no fill
    no border
    no white-space property
```

Future Agents must reproduce these patterns unless the Master Style version is explicitly updated.

---

# 33. FINAL PRINCIPLE

The article should look like a professional engineering publication on a corporate technical website, not:

- a code editor;
- a dashboard;
- a collection of colored cards;
- an academic paper pasted without adaptation;
- a marketing landing page.

The target presentation is:

```text
Clean
Technical
Readable
Reviewable
Consistent
Responsive
Source-aware
```
