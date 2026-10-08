# Fixed Excel generator

`scripts/build_report.py` formats agent-reviewed `findings.json`. It does not discover sitemaps, read `.seospider`, classify SEO findings, contact GSC or change results. Shared onsite configuration and evidence collection retain their existing ownership.

## Runtime preparation

Use Python 3.9+ with the repository's [requirements.txt](../requirements.txt). In the actual machine/container running the skill, use the same interpreter for dependency installation, preflight and execution:

```text
python -m pip install -r requirements.txt
python -c "import openpyxl, PIL; print('Excel runtime ready')"
```

Run commands from the skill directory, or resolve absolute script/requirements paths from the installed skill location. Do not hardcode the author's Windows user directory. When the host supplies a managed Python environment, use its approved runtime/dependency mechanism instead of installing into its bundled environment. A Python virtual environment is suitable for standalone/team installs.

Before collecting audit evidence, confirm imports and that the configured run root can create/delete a small probe file. Reuse the shared preflight when it already verifies that same output directory; do not duplicate probes for each check. Dependency installation is environment setup, not something to repeat on every run.

## Export once

```text
python scripts/build_report.py --input path/to/run/findings.json --output-dir path/to/run
```

The calling agent resolves `output.audit_date` or the configured/user timezone date into `audit_date` before export. The generator requires that explicit ISO date and does not infer a host timezone. It uses site_name verbatim except replacing filename-invalid characters and trimming leading/trailing dots/spaces. Empty/unreasonably long names fail clearly.

The generator validates all nine records, sorts 11.1–11.9, writes `Checklist` and `11. Sitemap`, and exports one detail row for each X. Other statuses stay in Checklist. Zero X leaves a headers-only issue sheet. Missing screenshots are represented by N/A when the screenshot list is empty; a supplied but missing/corrupt X screenshot is an error, never silently dropped. PNG/JPEG screenshots are embedded proportionally and vertically stacked. Long summaries or too many screenshots that exceed a readable Excel row are rejected with the row number; shorten the report summary/examples and retain complete evidence separately.

All customer strings are literal text, including strings starting with `=`, `+`, `-` or `@`. No formulas, network fetching or macros are generated. Headers, cell values, worksheet order and embedded screenshot counts are checked by reopening the workbook before publication and after writing. The file is created exclusively: an existing report is never overwritten. Handled write/verification failure removes only this invocation's partial report. A process kill or power loss can still leave an incomplete file; inspect that run and export into a fresh run directory. Automatic integrity checks do not replace a visual review in Excel/a spreadsheet renderer.

Success prints `Created and verified: <absolute path>` and exits 0. Failure prints `ERROR: <reason>` to stderr and exits 1; command usage errors exit 2. No automatic retries, crawl restart or alternative report generation are triggered. Keep findings.json/raw evidence available even if Excel cannot be generated.

| Error | Recovery |
| --- | --- |
| Missing dependency/runtime | Install requirements in the actual executing environment, then retry export only. |
| Missing/duplicate check, invalid result/date, missing required action | Correct reviewed findings.json from available evidence; never invent a pass to satisfy validation. |
| Missing/corrupt X screenshot | Supply the correct local PNG/JPEG, or explicitly set screenshots to [] if optional evidence is unavailable; retain the audit conclusion. |
| Cell length, unsupported XML character, excessive row height | Produce a concise human-readable summary; preserve full raw evidence. Do not silently truncate content. |
| Existing filename, permission error, full disk | Use a new writable run directory or resolve storage, then retry export only. |
| Output verification failed | Preserve findings, record the error and investigate the generator; do not deliver the suspect workbook. |

## Team / Multica

Import/refresh the repository skill and ensure the executing agent has Python, these dependencies and readable run files. A GitHub skill import alone does not guarantee dependency installation, SF/GSC availability or access to files on another teammate's computer. Mount/copy the authorized crawl/exports and screenshots to that runtime. Keep relative screenshot paths with findings.json. Use a separate writable run directory per run to prevent collisions; share no customer evidence through Git. This report generator requires no Codex-specific spreadsheet tool. Shared SF setup still requires `sf-shared-config` and its available runtime integration.

## Validation

```text
python -m unittest discover -s tests -v
```

Tests cover exact schemas, ordering, mixed/all-non-X results, literal strings/Unicode, malformed input, screenshots, no overwrite, simulated write failure and CLI errors. Test artifacts use ignored `runs/` directories. Tests verify report mechanics; they cannot establish the correctness of a real site's SEO evidence. Changes to the output schema or dependencies require rerunning tests and visually checking both sheets of a representative workbook.
