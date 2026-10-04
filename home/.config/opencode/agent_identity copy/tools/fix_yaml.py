import os
import re

def repair_yaml(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the YAML frontmatter block
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        print(f"No YAML block found in {file_path}")
        return

    frontmatter = match.group(1)
    body = content[match.end():]

    # Find all 'tags:' entries and their subsequent list items
    # This regex looks for 'tags:' followed by any amount of whitespace/newlines 
    # and then lines starting with '- ' (the tag list)
    tag_pattern = re.compile(r'tags:\s*(?:\n\s*- .+\n?)+')
    all_tag_blocks = tag_pattern.findall(frontmatter)

    if not all_tag_blocks:
        print(f"No tags found in {file_path}")
    else:
        # Extract specific tags from the blocks
        extracted_tags = []
        for block in all_tag_blocks:
            found = re.findall(r'-\s*(.+)', block)
            extracted_tags.extend([t.strip() for t in found])

        unique_tags = list(dict.fromkeys(extracted_tags)) # preserve order, remove duplicates

        # Remove all existing 'tags:' entries from the frontmatter to rebuild it
        new_frontmatter = tag_pattern.sub('', frontmatter).strip()

        # Reconstruct frontmatter
        # We'll put tags at the top for clarity
        header = "---\n"
        if unique_tags:
            header += "tags:\n"
            for t in unique_tags:
                header += f"  - {t}\n"
        
        # Add back other fields (we need to ensure we don't accidentally break existing ones)
        # Let's just build it from the re-parsed new_frontmatter if possible, 
        # but simpler is to take everything that isn't tags.
        rest = new_frontmatter + "\n"
        header += rest + "---\n\n"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(header + body)
        print(f"SUCCESS: Repaired tags in {file_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        repair_yaml(sys.argv[1])
    else:
        print("Usage: python3 fix_yaml.py <file_path>")
