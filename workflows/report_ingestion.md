# Financial Report Ingestion Workflow

Goal: capture financial reports as research memory without copying copyrighted full text.

Scope: create or update report index notes, report summaries, data clues, and factor hypotheses. Full report text stays outside Obsidian unless copyright clearly permits it and the user explicitly asks.

## Input Modes

| Mode | Example | Allowed Output |
|---|---|---|
| local user file | `/path/to/report.pdf` | metadata, summary, local path, data clues |
| official public page | broker or institution page | metadata, URL, short excerpts, summary |
| public PDF URL | direct PDF link | metadata, PDF URL, summary within copyright limits |
| secondary index | repost/index page | metadata with `source_confidence: secondary`, verify later |
| paid/member/internal | user has access but content is restricted | metadata and private reference only; no full text |

## Fields

- title
- author
- institution
- date
- source URL
- local PDF path or MinIO URI
- public/paid/internal status
- source confidence: `official`, `public-index`, `pdf-direct`, `secondary`, `local-user-file`
- theme
- factor ideas
- data requirements
- validation method
- implementation risk

## Summary Shape

```text
核心结论：
证据与方法：
因子/策略启发：
需要的数据：
可复现实验：
风险与限制：
后续行动：
```

## Routing

| Content | Destination |
|---|---|
| report metadata and concise summary | Obsidian `30_Resources/` |
| local PDF or raw attachment | local archive or MinIO reference |
| extracted tables/time series | PostgreSQL, ClickHouse, DuckDB, or Parquet candidate |
| factor hypothesis | Obsidian note plus Quant project backlog |
| experiment result | structured experiment metadata plus Obsidian narrative |

## Steps

1. Search existing vault notes by title, institution, author, and URL.
2. Deduplicate by normalized title + report date + institution.
3. Capture metadata before summarizing.
4. Separate:
   - report facts
   - analyst claims
   - Codex/user inference
   - validation plan
5. If the report is a collection, update an index note first and summarize only selected high-value reports.
6. Add candidate links to relevant MOCs, especially quant, factor research, macro, industry, or data-source indexes.
7. Record unresolved access/copyright issues in `## 待确认`.

## Copyright Boundary

Do not paste full paid/member/internal reports into Obsidian. Store metadata, summaries, short compliant excerpts, and links or local references.

## Quality Gate

- Every report note must include date, institution, source, access status, and source confidence.
- Every factor idea must include a minimal validation plan: universe, horizon, required data, expected direction, and failure risk.
- If source confidence is not `official` or `pdf-direct`, mark the note as `status: seed` or add `confidence: low`.
