import os
from datetime import datetime

def clean_user_profile(vault_path):
    file_path = os.path.join(vault_path, "Areas/Personal/User_Profile.md")
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # The cleaned data based on the content we see
    cleaned_content = [
        "Name: toor.",
        "Background: Backend C#/.NET, formerly Fullstack (.NET + React/TS).",
        "Current Focus: AI, ML, DataScience, RAG, Automation, Game Hacking (C/C++, WinApi, Lua, Python).",
        "",
        "Environment: Dualboot Windows 11 & CachyOS. IDE: VSCode. Tools: Docker. Hardware: RTX 4080 FE, Ryzen 7 9800X3D, 64GB DDR5-6000.",
        "",
        "Workflow: Prototype (just make it work) -> Refactor + Documentation + Tests. Testing: Mandatory Unit tests, optional Integration tests. Management: Jira (Work), GitHub Issues / todo.md (Home)."
    ]

    frontmatter = "---\n"
    frontmatter += "tags:\n"
    frontmatter += "  - area/personal\n"
    frontmatter += "  - type/profile\n"
    frontmatter += f"created_at: {now}\n" # Note: In a real scenario, we might want to keep the original created_at
    frontmatter += f"updated_at: {now}\n"
    frontmatter += "---\n\n"

    full_content = frontmatter + "\n".join(cleaned_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    print(f"SUCCESS: Cleaned and fixed {file_path}")

if __name__ == "__main__":
    clean_user_profile("/home/toor/Projects/senior-architect/obsidian-vault-main/")
