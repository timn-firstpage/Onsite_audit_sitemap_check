# Nine-check decision rules

These decisions reflect the user's final instructions from 2026-10-06. Keep the flow simple. A heuristic pass is not a claim of verified CMS internals, complete image coverage or Google indexing. Report language follows config/user preference.

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

## 11.3 Are <loc> tags used and www/non-www versions accurate? (Compulsory)

Check XML loc elements contain absolute URLs. Index loc points to a sitemap; urlset loc points to a page. Compare page URLs with observed final destinations and the site's intended www/non-www version using existing SF response/redirect evidence. Missing/invalid loc, wrong hostname variant or redirected page loc => X with examples. Do not add extensive canonical comparison here; known canonicalised URLs are handled in 11.7. Intentional subdomains/locales are not automatically wrong. Unknown response coverage => Human check unless an issue is already confirmed.

## 11.4 Are last modified tags being used?

Find an actual sitemap `<lastmod>` element (including one in a sitemap index) => √ under the user's presence-only test. Do not require every page to have it, validate historical accuracy, or add stricter date freshness criteria. A comment or text mentioning lastmod is not an element. Complete inspected XML with none => X, explain “missing optional lastmod; improvement recommendation”, not invalid XML. Incomplete evidence with none found => Human check. No sitemap => N/A.

## 11.5 Are robots-blocked and noindex pages excluded?

Match sitemap page URLs against effective Googlebot robots.txt permissions and SF meta robots / HTTP X-Robots-Tag noindex evidence. Use rule precedence/user-agent selection, not raw substring matching of Disallow. `nofollow` alone is not noindex. Robots blocking is a crawl restriction, not proven deindexing.

Any confirmed blocked/noindex page in sitemap => X and identify it. Complete relevant checks with none => √. Missing directives/permissions/rows => Human check, not pass. A readable robots.txt absent by confirmed 404 means no robots-file blocking, but does not waive the noindex check. Sitemap file's own noindex header is not evidence that listed pages are noindex.

## 11.6 Are paginated URLs avoided?

Compare SF Pagination > Paginated 2+ Pages Address values with sitemap page loc values. Supplement with observed pagination patterns such as `/page/2/`, `?page=2`, `&page=2`, `?p=2`. Open/inspect candidates to establish actual pagination; p can mean a post ID. Exclude First Page from automatic failure. Empty SF Pagination alone does not prove absence because identification relies on next/prev annotations.

Any confirmed page 2+ in sitemap => X under this user's checklist; otherwise √ when relevant inventory/pattern screening is complete. Missing coverage => Human check. Recommend excluding unnecessary pagination from sitemap while preserving crawlable pagination links. Describe this as the local audit preference, not a Google prohibition; do not recommend blanket noindex or canonical-to-page-1.

## 11.7 Have non-indexable URLs been removed?

Use the available SF “Non-Indexable URLs in Sitemap” result. Under the user's revised simple rule, no matching URL records, an empty result, zero, null or NaN => √: “No non-indexable URLs found in the supplied sitemap results.” One or more listed non-indexable URL records => X. Do not require a separate crawl-completion, Crawl Analysis or full-coverage verification before accepting an empty result, and do not turn that empty/NaN result into Human check. If using a broader SF non-indexable URL export, match its URLs against the sitemap page URL inventory; no matches => √, matches => X.

This rule concerns absence of records in available evidence, not an inability to access any evidence. No SF result/export or usable comparison data at all, or a failed tool read => Human check. No discovered sitemap => N/A. Preserve known contradictory URL evidence as X rather than overriding it with an empty filter. State the actual source/coverage in Checklist Coverage; a simplified pass does not establish Google index status or verified full-crawl completion. Only X enters the second worksheet.

Report 3xx/4xx/5xx, noindex and canonical-to-other-URL reasons. Distinguish transient 403/429/timeouts/tool failures from confirmed durable site defects and suggest verification when needed. Do not delete important pages merely because they are broken: recommend repair or replacement/removal according to intended indexing. Missing canonical alone is not non-indexable. SF indexability is not actual Google index status. Checks 11.5/11.7 may overlap; keep both results without duplicating long evidence lists.

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
