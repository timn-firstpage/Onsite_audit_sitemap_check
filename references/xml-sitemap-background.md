# XML Sitemap 背景知识与审计参考

整理日期：2026-10-06

当前执行标准：本文件是早期背景材料。后续用户确认的简化规则见 [audit-rules.md](audit-rules.md)，包括 dynamic 初筛、lastmod 存在即通过、分页出现即报告、产品图片抽查通过即通过。背景中的更广泛建议不自动增加检查或改变这些判定。

用途：保存用户提供的「11. XML Sitemap」截图背景，供后续 sitemap 相关 skill 引用。本文件是参考资料，不是可执行 skill，也不把截图中的建议视为用户要求立即执行的操作。

## 原始资料要点（摘要，未经逐项认可）

- Sitemap 帮助搜索引擎发现重要页面，尤其是缺少内部链接的页面。
- 截图列出 50,000 URL、未压缩 50 MB、UTF-8 和主机一致性要求。
- 建议根目录部署、robots.txt 声明、CMS 自动维护；爬虫生成作为替代。
- 建议多语言网站使用 hreflang sitemap，并提到每日更新、changefreq、priority，以及国际版本的信号整合。

## 经核对后应采用的背景知识

### 作用与限制

Sitemap 提供页面发现线索，不保证抓取、索引或排名，也不能代替良好的内部链接。应优先包含希望被索引的 canonical URL，而不是机械地列出所有网站地址。[Google：Sitemap 概述](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)

### 文件与提交

- 单个 sitemap 最多 50,000 个 URL，未压缩大小最多 50 MB；超过任一限制应拆分，并使用 sitemap index。
- XML 使用 UTF-8、正确命名空间及实体转义；URL 使用完整绝对地址。
- 根目录是便于覆盖全站的做法，不是唯一合法位置；需考虑目录作用域及 Search Console 提交方式。
- 可在 robots.txt 声明 sitemap index，不必逐一声明它已包含的全部子 sitemap；也可通过 Search Console 提交。
- 同一 host 是普通 sitemap 的默认约束，但 Google 支持满足所有权验证等条件的跨站提交；不能把「所有域名和子域名必须相同」当作无例外规则。

来源：[Google：创建和提交 Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)、[Sitemaps.org 协议](https://www.sitemaps.org/protocol.html)

### 字段与更新

`loc` 是必需字段；`lastmod`、`changefreq` 和 `priority` 是可选字段。Google 忽略 `changefreq` 和 `priority`，缺少它们不应判为 Google SEO 错误。`lastmod` 应反映页面实际的重要修改，不能每次生成文件就统一改成当天。更新频率应跟随内容变化，不必强制每日更新；CMS 自动维护通常更可靠。

来源：[Google：创建和提交 Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)、[Sitemaps.org 协议](https://www.sitemaps.org/protocol.html)

### 多语言与 hreflang

Hreflang 适用于对应的语言或地区版本，帮助 Google 展示合适版本；不是所有网站的必需项，也不保证更快索引。HTML、HTTP header、XML sitemap 三种实现方式对 Google 等效，已有正确实现时不必额外强制添加 sitemap 版本。

在 XML 中使用 hreflang 时，核对 xhtml 命名空间、完整 URL、有效语言／地区代码、自引用及对应版本的双向关系。Alternate URL 可以跨域；不能将它与主 loc 的 host 检查混为一谈。不要将 hreflang 描述为 canonical 替代品、权重合并工具或通用重复内容修复方法。

来源：[Google：本地化页面版本与 hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)

## 未来审计 skill 可采用的检查范围

以下是结合本次聊天整理的工作建议，不是截图原文，也不是本次已执行的审计结果。

1. 发现：robots.txt → CMS／插件设置 → 常见路径 → Search Console／Bing（有权限时）；搜索结果和 HTML sitemap 只作辅助线索。
2. 文件：HTTP 状态、最终地址、XML 解析、编码、数量、解压后大小、index 与子 sitemap 可访问性。
3. URL：状态码、重定向、noindex、robots 限制、canonical、重复地址、HTTPS 与 host 一致性。
4. 覆盖：与全站 crawl 比较，找遗漏的重要 canonical 页面及 sitemap 独有 URL；后者需确认 crawl 范围后才能判断为孤立页面。
5. 国际化：仅在有多语言／地区版本时检查 hreflang；区分标注错误与其他实现方式。
6. 证据：记录发现来源、检查时间、受影响 URL、问题类型及建议；缺少平台权限时明确 Google 抓取／索引状态尚未验证。

## 原图中的说法应怎样处理

| 原始建议 | 后续使用方式 |
|---|---|
| Sitemap 帮助发现页面 | 保留，同时注明无抓取／索引保证 |
| 必须包含 changefreq 和 priority | 修正为可选；Google 忽略这两个字段 |
| 所有网站都建议 hreflang sitemap | 限定为国际化网站，并先检查现有实现 |
| Hreflang 聚合权重、解决重复内容 | 不采用该表述；分别检查 hreflang 与 canonical |
| 必须每天更新 sitemap | 改为随实际内容变化维护 |
| Sitemap 必须放根目录 | 改为推荐位置，并核对作用域 |
| 所有域名／子域名必须一致 | 保留默认主机规则，同时识别跨站提交与 hreflang 例外 |

后续创建 skill 时，可将本文件作为 references 资料引用；正式工作流应再次核对当时的官方规则与工具行为。
