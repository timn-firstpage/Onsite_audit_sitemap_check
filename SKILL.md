---
name: onsite-audit-sitemap
description: Audit website sitemaps using Screaming Frog evidence and bounded sitemap checks, applying the agreed nine-check onsite checklist and producing a two-sheet Excel report. Reuse the shared onsite SF configuration workflow.
---

# Onsite Sitemap Audit

Produce `{site name}_sitemap_audit_{YYYY-MM-DD}.xlsx` for a supplied site using the nine checks in [audit rules](references/audit-rules.md). This is a simple first-pass audit with explicit user-selected heuristics. Do not silently replace those heuristics with a stricter SEO assessment.

## Inputs and preparation

- Obtain site URL/name, existing crawl/exports, and integrated onsite config if available. Use [config.template.json](config.template.json) only as a standalone fallback. Read [shared configuration](references/shared-config.md) for ownership and SF handover.
- If checks.sitemap is explicitly false, do not run the audit; report that this flow is disabled. Respect checks.live_checks and the integrated cumulative budgets throughout.
- Reuse suitable existing crawl evidence. If new SF preparation is needed and permitted, route to installed `sf-shared-config`; read its actual SKILL.md. It owns profile selection/loading, user sitemap confirmation, manual Start and Downloads handover. Never call an operation that starts a crawl merely to load configuration. Do not overwrite site-specific sitemap settings or change an active crawl.
- User confirmation of sitemap configuration is a prerequisite for new SF runs. An unavailable sitemap does not prevent independent discovery or delivery. Config file existence and an empty result are not proof of completed analysis; nevertheless, 11.7 explicitly accepts an available empty/no-match/NaN result as a simplified pass without an extra analysis-completion gate.
- Discover actual SF/GSC tool capabilities. Do not invent an MCP integration, assume a connector is connected, or deserialize an arbitrary .seospider binary. Use supported loading or readable exports.

## Audit

1. Read [audit rules](references/audit-rules.md) and [output contract](references/output-contract.md). These contain the accepted decisions and override broader background recommendations.
2. Find XML sitemaps from robots.txt first, then the finite CMS paths in the rules. Read index children, record source sitemap per page URL and preserve raw XML/response evidence. A successful HTTP response with homepage/error HTML is not a valid XML sitemap.
3. Run supported checks against existing SF results and bounded read-only sitemap/static evidence. Use SF for full URL status/directive/non-indexability checking; do not build an independent whole-site crawler. Read only required exports, retaining complete files instead of relying on tool previews.
4. Apply the agreed simple gates: dynamic is preliminary screening; lastmod presence passes; pagination inclusion fails the local checklist; product-image sample success passes; 11.7 passes when the available sitemap non-indexable result has no URL records (including empty/zero/null/NaN), and fails when records exist. Do not add analysis-completion prerequisites to 11.7. Label heuristic/sample scope honestly without imposing additional pass conditions.
5. Use `√`, `X`, `N/A`, `Human check`. Confirmed findings survive partial coverage; unknown data never becomes a pass. When no sitemap is discovered, 11.1 is X with manual-check action and dependent checks are N/A with the discovery limitation. If a known sitemap cannot be read, affected checks are Human check rather than N/A.
6. Record all nine decisions in findings.json using the output contract. Run `python scripts/validate_findings.py <findings.json>`. This validates the record structure, not the truth of the audit.
7. Use the available spreadsheet skill/runtime to author the two-sheet workbook with the exact headers below, embed real screenshots where useful, and verify readable layout. Always deliver supported findings and explicit gaps; do not wait indefinitely for missing exports, GSC access or a manual crawl. Resume from the same evidence when provided.

## Delivery boundaries

- Exactly two worksheets, in order: `Checklist` with `Item No.`, `Item Name`, `Initial Check`, `Findings`, `Coverage`; then `11. Sitemap` with `Sitemaps`, `URLs Example`, `Instructions`, `Screenshots (If Applicable)`. Checklist contains all nine checks; Initial Check owns the result. The second sheet contains confirmed X finding details. Keep Human check reasons/actions in Checklist, and preserve second-sheet headers even with no issues. Follow the output contract; do not substitute another audit's column names.
- Preserve the filename, date/timezone and language rules in the output contract. Save reports/raw evidence in a unique run directory, never overwrite a prior run and never commit customer evidence.
- No website/configuration repair, GSC submission, automatic crawling, recurring monitoring, or external messaging is authorized by invoking this audit.
- Optional context: [background summary](references/xml-sitemap-background.md) preserves the supplied screenshot and official SEO distinctions. It is not an additional mandatory checklist.
