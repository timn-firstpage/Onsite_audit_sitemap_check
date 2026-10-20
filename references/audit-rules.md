# Nine-check decision rules

These decisions include the user's simplified rules from 2026-10-12. Keep findings and human next steps short and separate. Use √ and X, never Yes/No; retain N/A and Human check for inapplicable or unavailable evidence. A sample pass is not a full technical audit. Report language follows config/user preference.

## Common result rules

`√`: the agreed test passed. `X`: a confirmed checklist failure. `N/A`: genuinely inapplicable, or a dependent check after unsuccessful sitemap discovery under this user's convention. `Human check`: insufficient evidence, failed fetch, incomplete analysis or unavailable access. Every N/A/Human check includes a reason; Human check also includes a concrete next action.

For broad negative claims (no pagination/no product images), require adequate complete relevant evidence. Lastmod presence, successful product-image sampling and 11.7's empty-result pass use the explicitly relaxed gates below. A confirmed issue can be X even when other URLs remain untested; describe the remaining scope.

## 11.1 Does an XML sitemap(s) exist?

Read `/robots.txt` Sitemap declarations first. If none is valid, try `/sitemap.xml`, `/wp-sitemap.xml`, `/sitemap_index.xml`; CMS clues can justify `/sitemap-index.xml` or `/media/sitemap.xml`. Do not brute-force arbitrary paths. Recognize `.xml.gz` and XML content at extensionless/custom endpoints. Follow finite redirects within scope/budget. A valid parsed XML urlset or sitemapindex passes. HTTP 200 alone does not.

Any valid XML sitemap found => √. No valid XML discovered after accessible checks => X, wording “Sitemap not found in checked sources; please verify the actual sitemap address manually”, not absolute proof of nonexistence. Known endpoints blocked/failed with no valid alternative => Human check. If only valid TXT/RSS/Atom is found, say “XML not found; alternative supported format found”; the XML-specific checklist is not proof that Google has no usable sitemap. HTML is a discovery aid, YAML/JSON are not supported Google sitemap formats.

For an index, traverse referenced child files, deduplicate already-seen sitemap addresses, and record failures/limits. An index can establish existence while incomplete children leave later checks unresolved. Sitemap index entries are files; do not count them as page URLs. Distinguish page loc from image:loc and hreflang href.

## 11.2 Is the sitemap a dynamic sitemap?

Keep the user's preliminary screen: open the sitemap/index and children; inspect standard readable output, bot access, organized child sitemaps and visible CMS/plugin-generation clues. Accessible standard sitemap output with coherent plugin/generated/child structure is sufficient for a preliminary √; do not demand CMS admin access or a time-based update experiment. One sitemap, a fixed URL or no plugin signature alone does not fail; these are clues only. A static file can be valid.

Confirmed invalid/nonstandard payload or effective bot block => X with the actual reason. Insufficient screening evidence => Human check. State “dynamic preliminary screen passed” rather than “automatic updates verified”. Treat TXT/RSS/Atom as supported format alternatives; do not call HTML a Google-submittable sitemap. Do not add a separate audit row or expand this into a CMS architecture investigation.

## 11.3 Are <loc> tags present? (Sample up to 3)

Sample up to three distinct sitemap entries from XML already loaded (use all available entries if fewer than three). An entry is a url element in a urlset, or a sitemap element in an index. An actual sitemap <loc> element in any sampled entry => √. A comment, escaped text or image:loc alone does not count. Do not check www/non-www, redirects, canonical or final destinations for 11.3. If all sampled entries are readable and none has <loc>, mark X. If no loc is found and the sample cannot be read, use Human check; no discovered sitemap => N/A. Record selected entries internally. Findings can say “抽查 3 项，发现 loc。” with blank Instruction. This is a presence sample, not URL correctness validation.

## 11.4 Are last modified tags being used?

Find an actual sitemap `<lastmod>` element (including one in a sitemap index) => √ under the user's presence-only test. Do not require every page to have it, validate historical accuracy, or add stricter date freshness criteria. A comment or text mentioning lastmod is not an element. Complete inspected XML with none => X, explain “missing optional lastmod; improvement recommendation”, not invalid XML. Incomplete evidence with none found => Human check. No sitemap => N/A.

## 11.5 Is the sitemap unblocked, with no noindex pages listed?

Use existing SF results only, reusing the exports used for 11.7. This check has two simple parts:

1. Check SF's robots-blocked result for the sitemap file URL(s), not every listed page. Known sitemap files not blocked => this part passes. A confirmed blocked sitemap file => X. A successful HTTP fetch alone is not an SF robots result. No usable SF robots result => this part is unresolved; do not fetch/parse robots rules independently.
2. Read the available SF noindex page result once. Empty/zero/null/NaN => this part passes immediately. Only when noindex page records exist, intersect their URLs with the already loaded sitemap page URLs. Any match => X; no matches => this part passes. An existing combined non-indexable result with reason Noindex can supply this subset; an empty non-indexable result also means no noindex candidates. If candidates exist but the sitemap inventory needed for comparison is unavailable, use Human check. No usable SF result or failed read is missing evidence, not an empty result.

Any confirmed issue in either part => X, even if the other part is unresolved. Both parts pass => √. Otherwise Human check; no discovered sitemap => N/A. Do not perform separate meta/header requests or require extra analysis-completion checks. Keep the result concise: “Sitemap 未被阻挡，未发现 noindex 页面。” An X instruction can say “允许抓取此 sitemap。” or “从 sitemap 移除此 noindex URL。” Sitemap file noindex is not page noindex.

## 11.6 Are paginated URLs avoided?

Compare SF Pagination > Paginated 2+ Pages Address values with sitemap page loc values. Supplement with observed pagination patterns such as `/page/2/`, `?page=2`, `&page=2`, `?p=2`. Open/inspect candidates to establish actual pagination; p can mean a post ID. Exclude First Page from automatic failure. Empty SF Pagination alone does not prove absence because identification relies on next/prev annotations.

Any confirmed page 2+ in sitemap => X under this user's checklist; otherwise √ when relevant inventory/pattern screening is complete. Missing coverage => Human check. Recommend excluding unnecessary pagination from sitemap while preserving crawlable pagination links. Describe this as the local audit preference, not a Google prohibition; do not recommend blanket noindex or canonical-to-page-1.

## 11.7 Have non-indexable URLs been removed?

For X, copy every affected original Address from the SF result into findings.json urls and list them in the detail sheet, one URL per row. The dedicated Non-Indexable URLs in Sitemap result is already scoped: do not discard its rows through a second sitemap/live-response/redirect check. For a broader non-indexable export, intersect original Addresses with the sitemap inventory once, then retain all matches. Preserve redirected, non-200, noindex and noncanonical URLs alike. Do not replace original Addresses with redirect targets, filter to status 200, show only a count or take a representative sample. The redirect target can be mentioned in the human instruction when known, but the affected original stays in URLs Example. An X without any affected URL must be corrected before export; do not deliver N/A as its URL. Keep original SF export and row counts internally so the agent can reconcile the exported URL list with the source. For large results retrieve the complete export, not only a tool preview; if unavailable, disclose the missing records rather than claim the list is complete.

Use the available SF “Non-Indexable URLs in Sitemap” result. Under the user's revised simple rule, no matching URL records, an empty result, zero, null or NaN => √: “No non-indexable URLs found in the supplied sitemap results.” One or more listed non-indexable URL records => X. Do not require a separate crawl-completion, Crawl Analysis or full-coverage verification before accepting an empty result, and do not turn that empty/NaN result into Human check. If using a broader SF non-indexable URL export, match its URLs against the sitemap page URL inventory; no matches => √, matches => X.

This rule concerns absence of records in available evidence, not an inability to access any evidence. No SF result/export or usable comparison data at all, or a failed tool read => Human check. No discovered sitemap => N/A. Preserve known contradictory URL evidence as X rather than overriding it with an empty filter. Store source/scope in the run archive, not a Coverage column. Only X enters the second worksheet.

Report existing SF non-indexable reasons, including response status, noindex and canonical-to-other-URL, without rechecking them independently. 11.5 uses the noindex subset; 11.7 uses all non-indexable records. Load exports once, create each needed URL intersection once, and reuse noindex matches in both checks. A noindex match makes both checks X; retain each required detail row but keep the wording short and reference the same evidence. Redirect/canonical-only records can make 11.7 X while 11.5 passes. An empty noindex subset alone does not prove the broader 11.7 result is empty. Instructions concern the sitemap entry, not deleting the actual website page.

## 11.8 If e-commerce: are appropriate product images included?

Judge actual site evidence: product catalogue/detail/collection pages with sales/shopping intent. A stray product word or unused plugin path is insufficient. Non-e-commerce => N/A; uncertain applicability => Human check.

Inspect a small representative sample of actual product sitemap entries (default up to 3 product details across visible templates/collections). Inspect image sitemap children/independent declared image sitemaps too. Match product page loc to image:image/image:loc; a generic img mention is insufficient.

- Sample succeeds (at least one sampled product entry has an appropriate image URL) => √ per user instruction. Record sample URLs/count and say sample passed; do not demand full inventory coverage.
- Confirmed zero product image entries across the complete relevant sitemap inventory => X.
- Sample fails but total absence is not established, or required files cannot be read => Human check.

Collection image absence alone does not fail when product-image sampling passes. This is a local optimisation check, not a universal Google indexing requirement.

## 11.9 Submitted to Google Search Console and error-free?

If actual connected tools and permissions can inspect the correct property, check the submitted sitemap/index and its processing status: submitted + successful processing => √; confirmed submission missing or processing errors => X. Without sufficient access/status => Human check with instructions to inspect Search Console > Sitemaps, submitted URL, status and last read. Do not submit anything automatically. Success does not mean every page is indexed. No discovered sitemap => N/A under the agreed dependency convention, with 11.1 manual action retained.

## Primary references

- [Google sitemap formats, submission, lastmod and canonical guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Image sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)
- [Pagination](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- [SF sitemap audit](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-audit-xml-sitemaps/)
- [SF pagination/filter definitions](https://www.screamingfrog.co.uk/seo-spider/user-guide/tabs/#pagination)

Standards explain findings; they do not silently override the user's explicit first-pass scoring.
