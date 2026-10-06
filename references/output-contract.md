# Output contract

Filename: `{site name}_sitemap_audit_{YYYY-MM-DD}.xlsx`. User-provided site name wins; otherwise use the hostname without leading www. Replace filename-invalid characters, preserving meaningful Unicode. Date uses output.audit_date if supplied, otherwise the user's timezone/local date (Asia/Hong_Kong in the originating session), never an unrelated host date.

Create a unique directory beneath configured run_root for each delivery. Do not append version text to the required filename or overwrite another report. Keep raw evidence, findings.json, manifest.json and sf-handover.json local/ignored.

## Workbook

Exactly one sheet, `11. Sitemap`, and these four columns in order:

| Sitemaps | URLs Example | Instructions | Screenshots (If Applicable) |
| --- | --- | --- | --- |
| 11.1 Does an XML sitemap(s) exist? | Actual sitemap URL or N/A | √ — Valid XML sitemap found. | N/A or real evidence image |

One row for each of checks 11.1–11.9, including passes and unresolved items. Use the check question from audit-rules.md in Sitemaps. Instructions starts with `√`, `X`, `N/A` or `Human check`, followed by a concise finding and necessary action. No additional status/severity columns or extra sheets. Multiple representative actual URLs may be separated by line breaks. Never put example.com or invented URLs in a customer report. NA values need a reason in Instructions.

Screenshots are optional: embed real, relevant screenshots if available, otherwise N/A. Do not create fake screenshots or force a browser session just to populate the column. Preserve screenshot evidence files beside the report when used. Keep rows tall enough for images, wrap text, freeze headers, use readable column widths and restrained status colors. Store all customer-supplied strings as literal text (not formulas). Keep concise evidence references/coverage in Instructions or cell notes without adding columns; complete raw evidence lives in the run archive.

For sample-based image passes, explicitly say “sample passed” and sample count. For 11.2 say “preliminary screen passed”. Empty SF filters pass only with completed relevant analysis. Reports with unresolved checks must not be described as an overall pass.

## Agent-reviewed findings.json

```json
{
  "site_name": "Example",
  "site_url": "https://example.com/",
  "audit_date": "2026-10-06",
  "checks": [
    {
      "id": "11.1",
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

The example shows one row only; actual input must contain all nine IDs exactly once. Every row requires the listed keys. X and Human check require an action. Human check finding explains the missing/failed evidence; N/A finding explains applicability/dependency. Screenshot paths refer to real local files relative to findings.json. Result labels are fixed; prose follows report language. The validator checks shape and required values only, not evidence truth, XML, image validity or workbook layout.

## Suggested local archive

`runs/<unique-run>/`: findings.json, manifest.json, sf-handover.json (or its recorded existing path), raw sitemap/robots responses, complete SF exports, optional screenshots and final workbook. Manifest records source timestamps, sitemap coverage/failures, request usage, sample selection and unresolved scope. Never commit these customer artifacts.
