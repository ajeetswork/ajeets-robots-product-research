# Printify Variant Audit – August 2026

Source: Printify API (Shop "Ajeets", ID 27965389) + Notion "Ajeet's Robots Variant Review Lab" (`3b9c1db3-c3be-81b1-8fc5-f73c6d67b1f2`)

Date: 2026-08-23

## High-burden variants – color confusion risk

These products have large color × size matrices with documented customer-confusion risk.

### 1. Ajeet Robot mens tee

- **Printify ID:** 6a51683a667e100da0023852
- **Visible:** No
- **Variants:** 19 colors × 10 sizes = 190 variants
- **Price:** $23.02 – $30.22
- **Risk:** Medium customer-confusion
- **Issues:**
  - 19 color options – Heather Grey / Athletic Heather / Sport Grey confusion
  - Missing marketing description (only care instructions present – flagged in `ajeets-robots-catalog/current-catalog-baseline.md`)
  - Inconsistent title: `Ajeet Robot mens tee` (should be `Ajeets Robots - Men's Tee`)
  - Pricing drift across colors – audit all 190 combinations

### 2. Ajeets Robots - Kids Cotton Tee

- **Printify ID:** 6a51687e667e100da0023895
- **Visible:** Yes
- **Variants:** 12 colors × 11 sizes = 132 variants
- **Price:** $14.99 – $22.99
- **Risk:** High customer-confusion
- **Issues:**
  - 12 similar color names – high confusion risk
  - Kids sizing varies by brand – ensure size chart is prominent
  - Pricing varies $14.99–$22.99 – confirm tier logic

### 3. Ajeets Robots - Men's Soft Shell Jacket

- **Printify ID:** 6a5167f5667e100da0023814
- **Visible:** Yes
- **Variants:** 6 colors × 9 sizes = 54 variants
- **Price:** $77.65 – $88.60
- **Risk:** High customer-confusion
- **Issues:**
  - Navy / Royal / Charcoal look similar in mockups – verify hex codes against provider swatches
  - XS–5XL size range must render correctly on Wix product page

## Print quality defects

### Wireless Earbuds case – text truncation

- **Printify ID:** 6a5d76570e7b07617a09f3cf
- **Price:** $41.99
- **Link:** https://ajeets.printify.me/product/30184150
- **Defect:** Print area template truncates "Ajeets Robots" → "Ajeets Rob"
- **Source:** Notion Issue Tracker – "Ajeets Robots - Wireless Earbuds" page in Variant Review Lab (`3c4c1db3-c3be-8176-99a3-c46003cec887`)
- **Pre-change checklist:** Confirm print area template fits full text before any listing update

## Variant burden summary

| Product | Total Variants | Review Burden | Confusion Risk |
|---------|---------------|---------------|----------------|
| Ajeet Robot mens tee | 190 | High | Medium |
| Kids Cotton Tee | 132 | High | High |
| Men's Soft Shell Jacket | 54 | High | High |
| Wireless Earbuds | 1 | Low | Low |
| Sweatshirt Blanket | 2 | Low | — |

## Recommendations

1. Add color swatch callouts with hex codes to high-burden listings (mens tee, kids tee, soft shell jacket)
2. Prominently display size charts – especially for kids apparel
3. Fix Wireless Earbuds print template before promoting the product
4. Backfill missing marketing description on "Ajeet Robot mens tee" before unhiding
5. Apply catalog-wide naming standard – see `ajeets-robots-brand-system/product-naming-conventions.md`

## Related

- Catalog snapshot: `ajeets-robots-catalog/catalog-snapshot-2026-08-23.md`
- QA checklists: `ajeets-robots-store-qa/variant-review-checklists.md`
- Naming conventions: `ajeets-robots-brand-system/product-naming-conventions.md`
- Customer complaints: `ajeets-robots-store-qa/customer-complaints-resolution-guide.md`
