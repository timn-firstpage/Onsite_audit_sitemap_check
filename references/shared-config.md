# Shared onsite configuration contract

Use the existing [sf-shared-config repository](https://github.com/timn-firstpage/On-_site_SF_shared_config) and its installed SKILL.md. The sitemap package does not fork profiles or change global SF settings. A sibling checkout is a usable source when accessible; discover the executing host's actual path rather than hardcoding the author's machine.

## Reuse and preparation

For a supplied `.seospider`, follow the shared [saved-crawl entry contract](https://github.com/timn-firstpage/On-_site_SF_shared_config/blob/main/references/saved-crawl-entry.md), reading its local copy when available. source.mode=saved_crawl and source.crawl_file are agent-owned inputs; relative paths resolve against the supplied config directory. Explicit supplied input wins over stale session IDs. Reuse matching exports or open once, share source fingerprint/crawl/export records across onsite flows, and preserve active/unsaved sessions and original inputs. No generic profile or new-crawl sitemap confirmation is required. No reader/import rejection gets manual saved-crawl Open + exact exports, not config Load + Start. Check output/runtime access before expensive retrieval.

Saved crawl may lack XML/GSC evidence: reuse archives, then permitted bounded static reads, then report only material gaps. File readiness is not proof of complete audit evidence. These preflight steps do not tighten 11.7's agreed empty-result pass. Label historical versus current live evidence.

1. Reuse site-matched, suitably dated exports/crawl with sufficient fields; historical settings need not all be reverified.
2. Missing SF evidence + source.allow_new_crawl=true: route to the shared skill. Full-site default is bundled onsite-main-js; targeted-content is only for necessary selected-URL follow-up. Explicit invalid profile overrides need correction, not silent fallback.
3. The shared skill delivers a verified profile copy to the SF host's real Downloads before manual Load; the user confirms profile/mode, site/sitemap, manually Starts and supervises, completes required Crawl Analysis and saves/exports to Downloads.
4. Never overwrite an active crawl or reload a generic config after site-specific sitemap edits. Never use sf_crawl(config_path) as a standalone loader. Unsupported/failed native loading follows the shared skill's immediate manual fallback.
5. Reuse sf-handover.json across onsite flows. Record its actual path in this run's manifest. Handover confirms provenance, not completeness or site health; validate the actual exports.
6. allow_new_crawl=false means use existing evidence and deliver gaps; it does not prevent permitted bounded static sitemap/robots retrieval. Do not bypass it with a custom crawler. Shared skill missing: provide its install/manual route and retain usable evidence.

## Config ownership

Reuse integrated site/source/mcp/budget/cache/output values. Execute only checks.sitemap; ignore other flows' enabled checks. Use the standalone template only when no integrated config exists. Resolve relative file paths against the provided config's directory; run_root must resolve to writable task storage, not an installed skill folder.

| Config | Owner / interpretation |
| --- | --- |
| site | Agent validates start_url, name, allowed_hosts; an empty allowed_hosts uses the start URL host and explicit approved scope, not arbitrary discovered domains |
| source | Evidence selection and shared skill routing; profile paths are optional overrides, null uses the shared bundled defaults when needed |
| mcp | Agent discovers actual tool/schema and allowed paths; config does not create a connection |
| checks.live_checks | False forbids new website HTTP reads; archived evidence remains usable |
| budget | Agent enforces cumulative MCP/live-request/redirect/timeout/poll/preview/paid-call limits across an integrated run; do not reset per check or turn these into SF full-crawl page limits |
| cache | Reuse same-crawl exports only when source/filter/fields match; do not assume stale live evidence is current |
| output | Agent resolves report language, date/timezone, unique run directory and archives |
| sitemap | Local bounded discovery and product-image sample size; does not overwrite the shared SF profile |

The config is agent-executed instructions, not an automatic runtime or a replacement for MCP permissions. max_paid_api_calls=0 excludes optional paid calls. Batch local evidence processing; no repeated unchanged polling. At most two safe transient read retries within cumulative budget; respect Retry-After, then record Human check. Cross-host sitemap declarations may be legitimate, but check approved scope before fetching; retain unverified references and gaps.

Bound sitemap discovery by sitemap.max_sitemap_files (default 100) and the remaining shared live-request budget, with sitemap.requests_per_second as the direct-read throttle. These are file/request limits, not URL counts or full SF crawl limits. Reaching a limit leaves the remaining inventory unresolved; it never proves absence. Apply response-size/decompression safeguards when reading untrusted compressed XML; do not resolve external XML entities. Record oversized/unreadable content as an evidence gap.

## Minimum evidence handover

- Site, crawl ID/time, completed/partial status and analysis status, with user-confirmed versus tool-verified provenance.
- Loaded/read sitemap inventory and child-file failures; page loc inventory with source sitemap.
- SF page URL/status/redirect, Indexability and reason, canonical when available, robots permission, meta robots and X-Robots-Tag.
- Pagination > Paginated 2+ Pages export and known site pagination patterns.
- Raw sitemap XML for loc/lastmod/image checks; optional GSC status evidence.

Full raw/rendered page HTML is not required for every URL. Main profile does not store full HTML: retrieve bounded static XML directly when permitted, use existing SF metadata, and request only material missing evidence. Complete data is required only for claims depending on it. Retain useful checks and export Human check gaps rather than withholding the workbook.
