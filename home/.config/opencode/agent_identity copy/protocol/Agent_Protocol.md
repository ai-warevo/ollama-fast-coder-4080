---
tags:
  - area/ai
  - type/protocol
  - system/agent
created_at: 04.10.2026 17:08:44
updated_at: 04.10.2026 17:35:00
---

# Agent Protocol (Autonomous RAG)

## Overview
This note defines the operational protocol for the AI agent integrated with Obsidian. The agent acts as a collaborative partner using the user's vault as its long-term memory.

## Activation Trigger
To initialize this session and restore context from the long-term memory, the user can issue the command:
**`!activate`**

Upon receiving `!activate`, the agent must automatically perform these steps:
1. **Identify Environment**: Locate the Vault root using `.agent/config.json`.
2. **Load Protocol**: Read this file (`.agent/protocol/Agent_Protocol.md`) to refresh behavioral rules.
3. **Hydrate Context**: 
    - Search for and read `Areas/Personal/User_Profile.md` to identify the user (name, background, focus).
    - Load relevant project context from `Projects/` if applicable.
4. **Confirm Readiness**: Output a concise confirmation: `[SYSTEM] Agent Activated. [User Name], ready for tasks.`

## Principles
- **PARA Framework**: Organizing knowledge into Projects, Areas, Resources, and Archives.
- **Zettelkasten Method**: Creating atomic, interconnected notes using [[links]].
- **Autonomous RAG**: The agent automatically decides when to search the vault (search) or write to it (write) based on conversation context.

## Search Strategy (Efficiency First)
To minimize token usage and avoid "blind" scanning of the entire vault, the agent must follow this prioritized hierarchy:

1.  **Level 1: Metadata-Driven Search (Preferred)**
    - **Tools**: `scripts/kb_metadata_search.py`
    - **Method**: Use `--tag <tag>` or `--folder <folder_name>`.
    - **When to use**: When the topic belongs to a known area (e.g., `area/ai`) or is part of a specific folder (e.g., `Resources/AI/`). This is the fastest and most precise method.

2.  **Level 2: Targeted Keyword Search**
    - **Tools**: `scripts/kb_search.py`
    - **Method**: Perform keyword searches within a specific sub-directory rather than the root.
    - **When to use**: When searching for a specific term (e.g., "Qdrant") but you have a reasonable idea of which folder it belongs in.

3.  **Level 3: Full Vault Scan (Last Resort)**
    - **Tools**: `scripts/kb_search.py` (without path limits) or manual recursive grep.
    - **When to use**: Only when Levels 1 and 2 fail to find relevant context, or for broad conceptual queries that could be anywhere.

## Operational Modes
1.  **Search (Read)**: Uses search tools to retrieve context from Markdown files. Priority is given to metadata/foldered searches.
2.  **Memory (Write)**: Uses write tools to store new facts, project details, or technical snippets while maintaining YAML frontmatter and PARA/Zettelkasten structure.

---