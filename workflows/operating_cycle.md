# Obsidian KB Operating Cycle

Goal: coordinate capture, triage, report ingestion, external data watch, MOC maintenance, and weekly synthesis without duplicating the real vault.

Default vault:

```text
/Users/zhukaijian/Documents/Obsidian Vault
```

## Execution Order

```text
read-only audit
-> inbox triage
-> report/data-source ingestion
-> MOC and link maintenance
-> weekly synthesis
-> next-week action list
```

## Read-Only Start

Run this before any batch operation:

```bash
python3 scripts/obsidian_kb_audit.py --vault "/Users/zhukaijian/Documents/Obsidian Vault"
```

Use the output to decide the smallest useful batch:

- missing frontmatter
- broken wikilinks
- Inbox notes ready for routing
- MOC link gaps
- weekly synthesis candidates

## Workflow Map

| Situation | Use | Result |
|---|---|---|
| raw captures need sorting | `inbox_triage.md` | move/update proposal, triage log |
| broker or financial reports arrive | `report_ingestion.md` | report index, summary, factor ideas |
| external statistics or industry sources need checking | `external_data_watch.md` | source update report, data-routing notes |
| week needs review | `weekly_synthesis.md` | weekly synthesis note, next actions |
| durable idea emerges | `obsidian-pkm-workflows` note promotion | one permanent note linked to sources |

## Safety Gates

- Do not delete user notes.
- Do not copy full paid/member/internal/copyrighted reports into Obsidian.
- Do not store raw numeric time series in Obsidian as the primary store.
- For more than 10 affected notes, produce a proposed action table first.
- For vault structure changes, explain the impact before applying them.
- For external data, distinguish fact, inference, forecast, revision, and methodology change.

## Current Baseline From 2026-06-25 Audit

- Core folders exist.
- Vault has 25 Markdown notes.
- `00_Inbox` has 1 note.
- `30_Resources` has 8 notes.
- Missing frontmatter candidates:
  - `Obsidian + Codex 工作流.md`
  - `欢迎.md`
- Broken wikilink candidates:
  - `50_MOCs/Home.md` -> `[[../00_Inbox]]`
  - `欢迎.md` -> `[[创建链接]]`

Recommended first maintenance batch:

1. Decide whether the default `欢迎.md` should be archived or kept as a seed note.
2. Decide whether the empty `Obsidian + Codex 工作流.md` should be replaced by an actual project note or archived.
3. Replace the folder-style wikilink in `50_MOCs/Home.md` with a valid note link or plain folder reference.
4. Triage the one Inbox note into an AI tools/resource note if it remains useful.

## Done Criteria

- Every changed note preserves source and creation context.
- New or changed resource notes have frontmatter.
- Report notes include access status and source confidence.
- Data-source notes include URL, frequency, unit, storage route, and caveats.
- Weekly synthesis links to source notes rather than duplicating them.
