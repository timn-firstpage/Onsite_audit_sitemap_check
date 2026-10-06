# Onsite Sitemap Audit

<p align="center"><img src="assets/onsite-audit-cover.png" alt="Onsite audit cover showing HTTPS security, website inspection, crawl connections, hostname redirects, and an audit report" width="640"></p>

用于 onsite audit 第 **11. Sitemap** 项的 Codex skill。沿用现有 [SF Shared Config](https://github.com/timn-firstpage/On-_site_SF_shared_config)，按已确认的九项检查输出 Excel。

仓库：[timn-firstpage/Onsite_audit_sitemap_check](https://github.com/timn-firstpage/Onsite_audit_sitemap_check)。Skill 名称：`onsite-audit-sitemap`，入口：[SKILL.md](SKILL.md)。

## 使用

将本仓库根目录安装或链接为 Codex skills 目录下的 `onsite-audit-sitemap`。SF 准备流程依赖另行安装的 `sf-shared-config`；已有可用 crawl/export 时无需重新配置。生成 Excel 使用当前环境可用的 spreadsheet skill/runtime。

示例：

> 使用 $onsite-audit-sitemap，检查 https://example.com。沿用我的 onsite global config 和已完成的 SF 导出，按约定输出 sitemap audit Excel。

提供网站、site name（可选）、global config 和现有 crawl/导出位置即可。独立运行可复制 [config.template.json](config.template.json) 到本地 run 目录再填写。模板不含凭据，读取模板不会自动连接 MCP、安装依赖或启动 crawl。

## 简单流程

1. 复用现有证据；确有需要且允许新 crawl 时，交给共享配置 skill。
2. 用户在 SF 确认 sitemap、手动 Start，完成分析后保存/导出；本 skill 不自动启动或重启。
3. 从 robots.txt 和常见 CMS 路径发现 sitemap，读取 index 及子文件。
4. 使用 SF 结果、XML 和适量抽查完成九项判断。
5. 校验 findings.json，生成并检查 Excel；资料不足仍交付 Human check 和具体下一步。

## 11.1–11.9 逐项检查逻辑

此 skill 只执行 sitemap 检查；SF 配置、crawl 和运行环境沿用 onsite global config。新 crawl 前由用户在 SF 确认 sitemap；已有适用结果直接复用。**未发现 sitemap 时，依赖它的项目记 N/A 并说明原因；已知文件无法读取或证据不足时记 Human check。**

| Item | 怎么检查 | 结果判断 |
| --- | --- | --- |
| **11.1 XML sitemap 是否存在？** | 先读取 `/robots.txt` 的 Sitemap 声明，再检查 `/sitemap.xml`、`/wp-sitemap.xml`、`/sitemap_index.xml` 等有限 CMS 常见地址。确认实际 XML 内容，主索引继续读取子 sitemap。 | **√**：找到有效 XML。**X**：完成可用来源检查仍未找到，列出检查范围并请人工确认地址。**Human check**：已知端点被阻挡、超时或无法判断。仅找到 TXT／RSS／Atom 时说明存在替代格式；不能声称完全没有 Google 可用 sitemap。 |
| **11.2 是否为 dynamic sitemap？** | 保留初筛：打开 sitemap 及子文件，检查标准可读格式、bot 访问情况、CMS／plugin 生成线索与子 sitemap 结构。不要求后台确认或动态更新实测。 | **√**：可访问、格式正常且初筛线索支持，注明“初筛通过”。**X**：确认格式无效／非标准内容，或被 bot 规则阻挡。**Human check**：线索或读取证据不足。只有一个文件或固定 URL 不单独判 X。**N/A**：未发现 sitemap。 |
| **11.3 是否使用 loc，www／非 www 是否正确？（必查）** | 检查 XML `<loc>` 及完整 URL。普通 sitemap 的 loc 是页面，index 的 loc 是子 sitemap；用已有 SF 响应／重定向结果确认页面最终地址和 www／非 www 版本，不扩大为复杂 canonical 比较。 | **√**：loc 正确，已检查 URL 与最终版本一致。**X**：缺失／无效 loc、错误 www 版本或页面 loc 指向重定向地址。**Human check**：必要响应证据不完整。**N/A**：未发现 sitemap。合法独立子域名不自动判错。 |
| **11.4 是否使用 lastmod？** | 在实际 XML 中查找 `<lastmod>` 元素，index 中的元素也计入；不要求全量覆盖或日期真实性验证，注释中提到 lastmod 不计入。 | **√**：找到实际元素即通过。**X**：相关 XML 已完整检查且没有，标注为可选字段优化建议。**Human check**：只检查部分文件且尚未发现。**N/A**：未发现 sitemap。 |
| **11.5 robots 阻挡／noindex 页面是否已排除？** | 将 sitemap 页面 URL 与有效 Googlebot robots 规则、SF meta robots 和 HTTP `X-Robots-Tag` 的 noindex 结果比对。按实际规则优先级判断；nofollow 本身不算 noindex。 | **√**：完成相关检查，没有发现阻挡／noindex URL。**X**：确认有此类 URL 留在 sitemap，列出地址和原因。**Human check**：权限、指令或数据缺失。**N/A**：未发现 sitemap。Sitemap 文件自身的 noindex 不代表里面的页面也 noindex。 |
| **11.6 是否避免分页 URL？** | 将 SF **Pagination → Paginated 2+ Pages** 的 Address 与 sitemap URL 比对；再按实际 `/page/2/`、`?page=2`、`?p=2` 等格式补查，确认候选确实是分页。 | **√**：完成比对／格式检查，没有第 2 页及以后的分页。**X**：确认分页出现在 sitemap，按本 checklist 报告。**Human check**：覆盖不足。**N/A**：未发现 sitemap。First Page 不自动判错，p 参数不一定代表分页。 |
| **11.7 是否排除 non-indexable URL？** | 确认 sitemap 已加载、相关 crawl／Crawl Analysis 完成，再读取 **Non-Indexable URLs in Sitemap**，结合状态码、noindex、canonicalised 等原因。 | **√**：已完成相关分析，结果为 0。**X**：确认存在非索引 URL，按原因建议修复、替换或移除。**Human check**：分析未运行、缺列／导出、无法解释的空白／NaN，或临时访问异常尚未核实。**N/A**：未发现 sitemap。 |
| **11.8 电商 sitemap 是否包含产品图片？** | 先按真实产品／销售功能判断是否电商。抽查代表性产品条目，默认最多 3 个；检查 `<image:image>`／`<image:loc>`，同时考虑独立 image sitemap。记录抽查 URL 和数量。 | **√**：抽查成功，至少一个抽查产品含适当图片 URL，注明“抽查通过”。**X**：确认完整相关 sitemap 中完全没有产品图片条目。**Human check**：抽查未通过，但未确认全无，或适用性／文件读取不明。**N/A**：非电商或未发现 sitemap。 |
| **11.9 是否提交 GSC 且无处理错误？** | 有实际 GSC 连接及权限时，检查正确 property 的 sitemap 提交记录、处理状态及最后读取时间。无权限时提供人工检查步骤，不自动提交。 | **√**：已提交且处理成功。**X**：确认未提交或有处理错误。**Human check**：未连接、无权限或状态证据不足，请到 GSC → Sitemaps 检查。**N/A**：未发现 sitemap。处理成功不等于所有页面已索引。 |

详细边界：[audit rules](references/audit-rules.md)。Dynamic 与图片的通过只表示初筛／抽查通过；pagination 是本地 checklist 标准，不声称 Google 禁止分页。HTML 不属于 Google 可提交 sitemap 格式，固定地址或单一文件也不证明静态生成。

## Excel 输出

文件名：**`{site name}_sitemap_audit_{date}.xlsx`**，date 为 `YYYY-MM-DD`。

两个 worksheet，按以下顺序输出。

**1. Checklist — 九项检查总表**

| Item No. | Item Name | Initial Check | Findings | Coverage |
| --- | --- | --- | --- | --- |
| 11.1–11.9 | 对应 checking list 的完整检查名称 | √ / X / N/A / Human check | 简洁结论、问题或缺口，以及必要的下一步 | 已检查来源、范围、数量、抽样及未覆盖部分 |

**2. 11. Sitemap — 具体问题与处理建议**

| Sitemaps | URLs Example | Instructions | Screenshots (If Applicable) |
| --- | --- | --- | --- |
| 检查编号及具体问题 | 实际 sitemap／受影响页面 URL | 具体问题说明及修正建议 | 适用时插入真实截图，否则 N/A |

Checklist 始终输出九项；Initial Check 是本次初审结果，不要求额外做一次复审。Findings 放结论和操作，Coverage 放证据范围，不重复长篇描述。11. Sitemap 放已确认的 X 问题详情；Human check、通过和 N/A 保留在 Checklist，无问题时第二页仍保留表头。

未找到 sitemap 时，依赖它的项目按约定填 N/A 并解释原因；已知文件无法读取、分析没跑完或 GSC 无权限用 Human check。不能将未检查的空白／NaN 当作通过。文件名和检查判定规则不变。

完整字段、命名、截图和归档约定见 [output contract](references/output-contract.md)。

## Global config 接入

共用 `site/source/mcp/budget/cache/output`，本 skill 只读取 `checks.sitemap` 和自身 `sitemap` 参数。沿用用户提供的累计预算与已有 SF handover，不复制两份 SF profile，不修改其他 onsite 项目配置。缺少设置时使用 standalone 模板的默认值。

`source.allow_new_crawl` 只允许请求用户手动运行；`checks.live_checks` 控制额外静态读取。已有数据优先、配置复制到真实 Downloads、手动加载 fallback 等均由共享 skill 负责。详见 [shared config contract](references/shared-config.md)。

## 文档与验证

- [九项审计规则](references/audit-rules.md)
- [输出 schema](references/output-contract.md)
- [共享配置与证据交接](references/shared-config.md)
- [原始截图背景摘要与官方说明](references/xml-sitemap-background.md)：背景参考，用户最终简化规则优先

本包为 agent 执行的工作流，附一个仅使用 Python 标准库的结构校验器：

```text
python scripts/validate_findings.py path/to/findings.json
python -m unittest discover -s tests
```

校验器不自动抓取、不判断 SEO、不生成 Excel。实际报告由 agent 使用可用 spreadsheet 工具生成；没有独立运行的全自动审计程序。Skill 结构、JSON 校验器及本地规则回归已验证；真实 SF/GSC 网站审计仍需实际数据，不能由静态验证代替。

运行证据、客户 URL 列表、Excel、凭据和本机配置均保存在忽略的 run 目录。仓库不包含客户报告，不修改网站，不自动提交 GSC。
