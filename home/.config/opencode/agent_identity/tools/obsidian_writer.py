import os
import sys
from datetime import datetime

def write_obsidian_note(vault_path, relative_path, content, tags=None, mode='create'):
    full_path = os.path.join(vault_path, relative_path)
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    frontmatter = "---\n"
    if tags:
        tag_lines = "\n".join([f"  - {t}" for t in tags])
        frontmatter += f"tags:\n{tag_lines}\n"
    frontmatter += f"created_at: {now}\n"
    frontmatter += f"updated_at: {now}\n"
    frontmatter += "---\n\n"

    full_content = frontmatter + content

    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"SUCCESS: Created/Overwritten {relative_path}")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)

if __name__ == "__main__":
    # python3 obsidian_writer.py <vault> <rel_path> <content> <tags_csv> <mode>
    v_base = sys.argv[1]
    r_path = sys.argv[2]
    body = sys.argv[3]
    raw_tags = sys.argv[4] if len(sys.argv) > 4 else ""
    tag_list = [t.strip() for t in raw_tags.split(',')] if raw_tags else []
    op_mode = sys.argv[5] if len(sys.argv) > 5 else 'create'

    write_obsidian_note(v_base, r_path, body, tag_list, op_mode)
