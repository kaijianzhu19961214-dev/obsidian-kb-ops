# Inbox Triage Workflow

Goal: turn raw captures in `00_Inbox` into linked, usable notes.

Scope: classify and lightly normalize new notes. Do not rewrite large source content, delete notes, or move many files without a reviewed plan.

Default vault:

```text
/Users/zhukaijian/Documents/Obsidian Vault
```

## Inputs

- `00_Inbox/*.md`
- recent web clipper captures
- user-provided URLs, PDFs, or local file paths
- existing MOCs under `50_MOCs/`

## Classification

| Class | Destination | Required Action |
|---|---|---|
| fleeting idea | `00_Inbox/` or `40_Permanent/` candidate | extract one durable claim or leave as seed |
| article/web clip | `30_Resources/` | preserve source, author, date, URL, short summary |
| financial report | `30_Resources/` | use `report_ingestion.md`, avoid copyrighted full text |
| external data source | `30_Resources/` | use `external_data_watch.md`, route raw data outside Obsidian |
| project note | `10_Projects/` | add status, decisions, next actions |
| daily log | `60_Daily/` | merge into date note when appropriate |

## Steps

1. List new notes in `00_Inbox`.
2. Classify each note:
   - fleeting idea
   - article/web clip
   - financial report
   - external data source
   - project note
   - daily log
3. Extract title, source, date, author/institution, URL, and key claims.
4. Summarize in Chinese:
   - conclusion
   - evidence
   - action items
   - open questions
5. Route the note:
   - keep in `00_Inbox` if incomplete
   - move/suggest to `30_Resources` if useful reference
   - move/suggest to `10_Projects` if it is active work
   - create a `40_Permanent` candidate only when there is one reusable idea
   - update MOC if it is durable
6. Add links and tags conservatively.
7. Write a short triage log to `60_Daily/YYYY-MM-DD - inbox-triage.md` when there is meaningful work.

## Frontmatter Patch Rules

- Always preserve `created`, `source`, `author`, and original capture URL.
- Set `updated` to the current date after changing the note.
- Prefer existing tag families such as `type/*`, `status/*`, `quant`, `research-report`, `external-data`.
- If confidence is low, mark `confidence: low` and add a `## To Confirm` section.

## MOC Rules

- Link a note from a MOC only when it should be rediscovered later.
- Use `[[note title]]` links rather than duplicating the note's content.
- For quant topics, prefer a Quant Research MOC if it exists; otherwise record the missing MOC as an action item.

## Output

```text
处理数量：
已归档：
仍在 Inbox：
新增链接：
Permanent 候选：
待确认：
```

## Safety Gate

For more than 10 affected notes, stop after classification and output a proposed move table first.
