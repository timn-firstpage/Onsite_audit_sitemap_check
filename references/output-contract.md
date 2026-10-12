# Output contract

Filename: `{site name}_sitemap_audit_{YYYY-MM-DD}.xlsx`. User-provided site name wins; otherwise use the hostname without leading www. Replace filename-invalid characters, preserving meaningful Unicode. Date uses output.audit_date if supplied, otherwise the user's timezone/local date (Asia/Hong_Kong in the originating session), never an unrelated host date.

Create a unique directory beneath configured run_root for each delivery. Do not append version text to the required filename or overwrite another report. Keep raw evidence, findings.json, manifest.json and sf-handover.json local/ignored.

## Workbook

Exactly two sheets in this order. Do not add columns, hide a status column, or replace these headers with another onsite audit's schema.

### 1. Checklist

| Item No. | Item Name | Initial Check | Findings | Instruction |
| --- | --- | --- | --- | --- |
| 11.1 | Does an XML sitemap(s) exist? | √ | 已找到 XML sitemap。 | |

Always include 11.1–11.9 exactly once in numeric order. Item Name uses the current checklist question from audit-rules.md, translated if requested. Initial Check contains exactly `√`, `X`, `N/A` or `Human check`, never Yes/No. Findings states what was found, preferably in one short sentence. Instruction states only the next step a person needs to take, starting with a clear verb. Keep it to one short sentence or two short steps. X and Human check require a next step. For √ or N/A, leave Instruction blank when no action is needed. N/A Findings briefly explains why it does not apply. No Coverage column: retain sources, sample URLs and scope in findings.json/manifest and the evidence archive.

| Findings | Instruction |
| --- | --- |
| 抽查 3 项，发现 loc。 | |
| Sitemap 含 noindex URL。 | 从 sitemap 移除此 URL。 |
| Sitemap 被 robots 阻挡。 | 在 robots.txt 中允许抓取此 sitemap。 |
| 缺少 SF 导出。 | 提供 SF 的对应结果导出。 |

Avoid tool logs, implementation details, SEO theory and repeated findings in Instruction. Do not automatically paraphrase reviewed text in the generator; the agent writes concise text before export.

### 2. 11. Sitemap

Preserve the originally requested detail schema:

| Sitemaps | URLs Example | Instructions | Screenshots (If Applicable) |
| --- | --- | --- | --- |
| 11.7 Redirected URL in sitemap | Actual affected URL | Replace the sitemap entry with the verified final URL. | N/A or real evidence image |

Export confirmed X findings into this detail sheet, one row per X check. Sitemaps contains the check number and concise finding; Instructions contains only the human next step, without repeating the finding. Use short numbered steps only when different fixes are needed. Passes, N/A and Human check stay in Checklist. Keep these four headers even when there are no X results. Separate representative actual URLs with line breaks; keep full lists in the archive. Never invent URLs. Use N/A when there is no affected URL, such as unsuccessful discovery; retain checked sources internally.

Screenshots are optional: embed real, relevant screenshots if available, otherwise N/A. Do not create fake screenshots or force a browser session just to populate the column. Preserve screenshot evidence files beside the report when used. Keep rows tall enough for images, wrap text, freeze headers, use readable column widths and restrained status colors in Initial Check. Store all customer-supplied strings as literal text (not formulas). Complete raw evidence lives in the run archive. Review both worksheet layouts before delivery.

For sample-based passes, briefly state the sample count; for 11.2 say “preliminary screen passed”. For 11.7, an available empty/no-match/zero/null/NaN result passes without an analysis-completion gate; say “未发现 non-indexable URL。” Record sources internally. Missing all usable evidence or failed reads remain Human check. Reports with unresolved checks must not be described as an overall pass.

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
      "evidence": ["raw/sitemap.xml"],
      "screenshots": []
    }
  ]
}
```

The example shows one row; actual input requires all nine IDs exactly once and all listed keys. Map id/item_name/result to Item No./Item Name/Initial Check, finding to Findings, and action to Instruction. Keep the existing JSON key action for compatibility. Legacy coverage is optional internal metadata and is never exported. X/Human check require a nonempty action; √/N/A may use an empty string. For X rows, use the same finding/action/urls/screenshots in 11. Sitemap. Screenshot paths are local PNG/JPEG paths relative to findings.json or absolute paths. Only X screenshots are embedded; others remain archived. The validator checks structure, not evidence truth. The generator also checks embedded files and workbook integrity; see [generator operations](report-generator.md).

## Suggested local archive

`runs/<unique-run>/`: findings.json, manifest.json, sf-handover.json (or its recorded existing path), raw sitemap/robots responses, complete SF exports, optional screenshots and final workbook. Manifest records source timestamps, sitemap coverage/failures, request usage, sample selection and unresolved scope. Never commit these customer artifacts.
