# Onsite Sitemap Audit

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

## 已确认的判断标准

| 检查 | 第一版规则 |
| --- | --- |
| 11.1 XML sitemap 存在 | 找到有效 XML 为 √；未找到报告 X 并请人工确认；已知端点无法读取为 Human check |
| 11.2 Dynamic | 保留可访问性、标准格式、CMS/plugin/子 sitemap 线索的初筛；不要求后台或动态更新实测 |
| 11.3 loc / www | 检查 loc、完整 URL 和最终 www/non-www 地址，避免复杂 canonical 比较 |
| 11.4 lastmod | 找到实际 lastmod 元素就 √；没有为 X（可选字段优化项） |
| 11.5 robots / noindex | sitemap 内有确认被阻挡或 noindex 的页面为 X |
| 11.6 Pagination | 确认第 2 页及以后 URL 出现在 sitemap 就 X；SF 比对加实际 URL 格式补查 |
| 11.7 Non-indexable | 完整 SF sitemap 分析中 0 个问题为 √；有问题为 X；未检查/缺数据为 Human check |
| 11.8 产品图片 | 抽查成功就 √；确认完全没有为 X；抽查失败但未确认全无为 Human check；非电商 N/A |
| 11.9 GSC | 有权限检查提交和处理状态；无权限或数据不足为 Human check |

详细边界：[audit rules](references/audit-rules.md)。Dynamic 与图片的通过只表示初筛／抽查通过；pagination 是本地 checklist 标准，不声称 Google 禁止分页。HTML 不属于 Google 可提交 sitemap 格式，固定地址或单一文件也不证明静态生成。

## Excel 输出

文件名：**`{site name}_sitemap_audit_{date}.xlsx`**，date 为 `YYYY-MM-DD`。

一个 worksheet：**11. Sitemap**。保留用户指定四列，不额外增加 Result 列；状态放在 Instructions 开头。

| Sitemaps | URLs Example | Instructions | Screenshots (If Applicable) |
| --- | --- | --- | --- |
| 检查编号及问题 | 实际 sitemap／受影响页面 URL | √ / X / N/A / Human check，加结论和必要操作 | 适用时插入真实截图，否则 N/A |

九项均输出。未找到 sitemap 时，依赖它的项目按约定填 N/A 并解释原因；已知文件无法读取、分析没跑完或 GSC 无权限用 Human check。不能将未检查的空白／NaN 当作通过。

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
