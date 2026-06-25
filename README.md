# Obsidian KB Operations

This project stores Codex workflows, templates, and scripts for operating the personal Obsidian knowledge base.

Real notes live in:

```text
/Users/zhukaijian/Documents/Obsidian Vault
```

This repository should not duplicate the whole vault. Keep it focused on repeatable operations:

- inbox triage
- web clipper review
- financial report ingestion
- external statistics and industry data watch
- weekly synthesis
- MOC maintenance
- vault hygiene

## Operating Cycle

Use this repo as the control plane and keep the real notes in the vault.

```text
capture -> inbox triage -> resource/report/data-source notes -> MOC links -> weekly synthesis
```

Default cadence:

| Cadence | Workflow | Output |
|---|---|---|
| Before changes | `workflows/operating_cycle.md` | Scope, safety gate, and execution order |
| Daily | `workflows/inbox_triage.md` | Inbox review log and routing decisions |
| On demand | `workflows/report_ingestion.md` | Copyright-safe report index or summary |
| Weekly | `workflows/external_data_watch.md` | External data watch report |
| Weekly | `workflows/weekly_synthesis.md` | Weekly synthesis note and next actions |

Start with a read-only audit before changing the vault:

```bash
python3 scripts/obsidian_kb_audit.py --vault "/Users/zhukaijian/Documents/Obsidian Vault"
```

Then execute the relevant workflow in a small batch. Bulk moves, template rewrites, and MOC restructuring should be proposed first and applied only after the first batch looks correct.

## Common Prompts

```text
用 $obsidian-pkm-workflows 整理今天的 Inbox，并输出处理日志。
```

```text
用 $financial-report-ingestion 检索公开研报，生成摘要、元数据和因子启发，不录入版权全文。
```

```text
用 $external-data-watch 检查外部统计与产业数据源清单，生成本周更新摘要。
```

```text
用 $obsidian-knowledge-base 更新 Quant Research MOC，把最近新增笔记挂到合适位置。
```

```text
先运行 scripts/obsidian_kb_audit.py，只读巡检 vault，列出 Inbox、孤立笔记、缺 frontmatter、断链和本周复盘候选。
```

## Project Layout

```text
workflows/   repeatable operating procedures
templates/   note templates and output shapes
scripts/     local utilities, added only when needed
AGENTS.md    Codex rules for this project
```
