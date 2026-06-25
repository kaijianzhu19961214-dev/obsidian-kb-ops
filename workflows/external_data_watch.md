# External Data Watch Workflow

Goal: monitor government, association, exchange, and industry data that can support quant research and research reports.

Scope: track updates and interpretation. Obsidian stores metadata, release notes, caveats, and research conclusions; raw time series belong in MinIO, PostgreSQL, ClickHouse, DuckDB, or Parquet.

Default watchlist note:

```text
/Users/zhukaijian/Documents/Obsidian Vault/30_Resources/外部统计与产业数据源清单.md
```

## Data Routing

- Raw files: MinIO.
- Tables/time series: PostgreSQL, ClickHouse, or DuckDB.
- Metadata and interpretation: Obsidian.
- Research conclusions and experiments: Obsidian + Quant project.

## Watch Items

- inventory
- production
- demand forecast
- import/export
- shipping and logistics
- capacity utilization
- price index
- macro/industry statistics

## Watch Status

| Status | Meaning | Action |
|---|---|---|
| no_update | no new release | record checked date only if useful |
| new_release | new period or file released | capture metadata and summary |
| revision | historical values changed | flag high priority and record revision rule |
| methodology_change | definition, sample, field, or frequency changed | create/update source note |
| needs_manual_review | website changed, source ambiguous, chart-only data | do not invent values |

## Steps

1. Read the watchlist note and identify active sources.
2. Prefer official or primary sources before secondary reposts.
3. For each source, capture:
   - source name
   - category
   - release date
   - period covered
   - URL
   - file name or object URI
   - fields, units, and frequency
   - preliminary/revised/final/forecast status
4. Route raw files and structured data outside Obsidian.
5. Write a weekly watch report under `60_Daily/YYYY-Www-external-data-watch.md`.
6. Promote durable methodology notes into `30_Resources/` source notes.
7. Link factor hypotheses to quant research notes or project backlog.

## Output

```text
本期更新：
数据源：
口径变化：
对量化研究的影响：
可构造特征：
待抓取/待结构化：
需要人工确认：
```

## Quality Gate

- Do not treat forecast data as realized data.
- Do not digitize chart values unless an explicit digitization step was performed.
- Mark secondary-only findings as low confidence.
- Any methodology change should be surfaced in the weekly synthesis.
