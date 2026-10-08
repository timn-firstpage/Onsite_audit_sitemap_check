# Output contract

Filename: `{site name}_sitemap_audit_{YYYY-MM-DD}.xlsx`. User-provided site name wins; otherwise use the hostname without leading www. Replace filename-invalid characters, preserving meaningful Unicode. Date uses output.audit_date if supplied, otherwise the user's timezone/local date (Asia/Hong_Kong in the originating session), never an unrelated host date.

Create a unique directory beneath configured run_root for each delivery. Do not append version text to the required filename or overwrite another report. Keep raw evidence, findings.json, manifest.json and sf-handover.json local/ignored.

## Workbook

Exactly two sheets in this order. Do not add columns, hide a status column, or replace these headers with another onsite audit's schema.

### 1. Checklist

| Item No. | Item Name | Initial Check | Findings | Coverage |
| --- | --- | --- | --- | --- |
| 11.1 | Does an XML sitemap(s) exist? | √ | Valid XML sitemap found. | robots.txt declaration; XML parsed |

Always include 11.1–11.9 exactly once in numeric order. Item Name is the corresponding complete checklist question from audit-rules.md, translated if requested. Initial Check contains exactly `√`, `X`, `N/A` or `Human check`; it is this run's assessment, not a requirement for a second review stage. Findings combines the concise conclusion and necessary action; Human check explains the missing/failed evidence and next action, N/A explains inapplicability/dependency. Coverage owns checked sources, counts, sampling and remaining scope. Avoid repeating this inventory in Findings.

### 2. 11. Sitemap

Preserve the originally requested detail schema:

| Sitemaps | URLs Example | Instructions | Screenshots (If Applicable) |
| --- | --- | --- | --- |
| 11.7 Redirected URL in sitemap | Actual affected URL | Explain the redirect and replace with the verified final URL. | N/A or real evidence image |

Export confirmed X findings into this detail sheet. The fixed generator creates one row per X check. Sitemaps contains the check number and concise finding; Instructions contains the finding and concrete action. When a check has multiple causes/fixes, distinguish them with numbered lines in finding/action and associate each with its representative URL; keep full URL lists in the evidence archive. Passes, N/A and unresolved Human check details belong to Checklist only. Keep these four headers even when there are no confirmed issues. Multiple representative actual URLs may be separated by line breaks. Never put example.com or invented URLs in a customer report; use N/A when no affected URL exists (such as unsuccessful discovery), explaining the checked sources in Checklist Coverage.

Screenshots are optional: embed real, relevant screenshots if available, otherwise N/A. Do not create fake screenshots or force a browser session just to populate the column. Preserve screenshot evidence files beside the report when used. Keep rows tall enough for images, wrap text, freeze headers, use readable column widths and restrained status colors in Initial Check. Store all customer-supplied strings as literal text (not formulas). Complete raw evidence lives in the run archive. Review both worksheet layouts before delivery.

For sample-based image passes, explicitly say “sample passed” and sample count. For 11.2 say “preliminary screen passed”. For 11.7, an available empty/no-match/zero/null/NaN result passes without a separate analysis-completion gate; say no non-indexable URLs were found in the supplied sitemap results and record the actual source in Coverage. Missing all usable evidence or a failed read remains Human check. Reports with unresolved checks must not be described as an overall pass.

## Agent-reviewed findings.json

```json
{
  "site_name": "Example",
  "site_url": "https://example.com/",
  "audit_date": "2026-10-06",
  "checks": [
    {
      "id": "11.1",
      "item_name": "Does an XML sitemap(s) exist?",
      "result": "√",
      "urls": ["https://example.com/sitemap.xml"],
      "finding": "Valid XML sitemap found.",
      "action": "",
      "coverage": "robots.txt declaration; XML parsed",
      "evidence": ["raw/sitemap.xml"],
      "screenshots": []
    }
  ]
}
```

The example shows one row only; actual input must contain all nine IDs exactly once. Every row requires the listed keys. Map id/item_name/result to Item No./Item Name/Initial Check; finding plus action to Findings; coverage to Coverage. For X rows, use the same reviewed finding/action/urls/screenshots to populate 11. Sitemap. X and Human check require an action. Human check finding explains the missing/failed evidence; N/A finding explains applicability/dependency. Screenshot paths refer to real local PNG/JPEG files relative to findings.json; absolute local paths also work, but relative paths travel better with an archived run. Only X screenshots are embedded; other screenshots remain archived evidence. Result labels are fixed; prose follows report language. The validator checks shape and required values only, not evidence truth, XML, image validity or workbook layout. The generator additionally checks embedded screenshot files and workbook integrity; see [generator operations](report-generator.md). Older records without item_name must be completed from the known checklist before export.

## Suggested local archive

`runs/<unique-run>/`: findings.json, manifest.json, sf-handover.json (or its recorded existing path), raw sitemap/robots responses, complete SF exports, optional screenshots and final workbook. Manifest records source timestamps, sitemap coverage/failures, request usage, sample selection and unresolved scope. Never commit these customer artifacts.
