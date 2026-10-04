import os
import shutil
from datetime import datetime

VAULT_PATH = "/home/toor/Projects/senior-architect/obsidian-vault-main/"
CURRENT_SCRIPTS_DIR = "./scripts"  # Relative to current working directory

AGENT_DIR = os.path.join(VAULT_PATH, ".agent")
PROTOCOL_DIR = os.path.join(AGENT_DIR, "protocol")
TOOLS_DIR = os.path.join(AGENT_DIR, "tools")

# The original location of the protocol
OLD_PROTOCOL_PATH = os.path.join(VAULT_PATH, "Areas/AI/Agent_Protocol.md")

def migrate():
    print("--- Starting Agent Infrastructure Migration ---")

    # 1. Create Directory Structure
    for folder in [PROTOCOL_DIR, TOOLS_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created directory: {folder}")
        else:
            print(f"Directory already exists: {folder}")

    # 2. Move Protocol
    if os.path.exists(OLD_PROTOCOL_PATH):
        new_protocol_path = os.path.join(PROTOCOL_DIR, "Agent_Protocol.md")
        shutil.move(OLD_PROTOCOL_PATH, new_protocol_path)
        print(f"Moved protocol from {OLD_PROTOCOL_PATH} to {new_protocol_path}")
    else:
        print(f"Warning: Original protocol not found at {OLD_PROTOCOL_PATH}")

    # 3. Copy Tools (Scripts)
    if os.path.exists(CURRENT_SCRIPTS_DIR):
        print(f"Copying tools from {CURRENT_SCRIPTS_DIR} to {TOOLS_DIR}...")
        for item in os.listdir(CURRENT_SCRIPTS_DIR):
            s = os.path.join(CURRENT_SCRIPTS_DIR, item)
            d = os.path.join(TOOLS_DIR, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)
                print(f"  - Copied: {item}")
    else:
        print(f"Error: Source scripts directory {CURRENT_SCRIPTS_DIR} not found.")

    # 4. Create setup_agent.md
    setup_content = f"""# 🚀 Agent Setup Guide

This file contains the instructions to initialize this agent in a new environment (e.g., after a system reinstall or on a different PC).

## Prerequisites
1.  **Obsidian Vault**: Ensure you have cloned/copied the entire vault directory.
2.  **Python**: Install Python 3.9 or higher.
3.  **Dependencies**:
    Run the following command to install necessary libraries:
    ```bash
    pip install requests qdrant-client fastembed sentence-transformers
    ```

## How to Start
To "activate" the agent, open a new session in your coding environment (like OpenCode) and give it this exact instruction:

> **"Read the protocol in `.agent/protocol/Agent_Protocol.md` and start working with my Obsidian Vault using the tools located in `.agent/tools/`. Follow the PARA and Zettelkasten principles."**

## Directory Structure
- `.agent/protocol/`: Contains `Agent_Protocol.md` (System Instructions).
- `.agent/tools/`: Contains Python scripts for searching, writing, and managing the vault.
- `(Obsidian Vault Root)`: This is your long-term memory.

---
*Generated on {datetime.now().strftime('%d.%m.%Y %H:%M')}. Use this as a bootstrap manual.*
"""
    setup_path = os.path.join(AGENT_DIR, "setup_agent.md")
    with open(setup_path, 'w', encoding='utf-8') as f:
        f.write(setup_content)
    print(f"Created setup guide: {setup_path}")

    print("\n--- Migration Completed Successfully! ---")

if __name__ == "__main__":
    migrate()
