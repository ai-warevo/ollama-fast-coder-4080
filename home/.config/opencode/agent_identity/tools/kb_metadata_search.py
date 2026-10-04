import os
import re
import sys
import argparse

def search_by_tag(vault_path, target_tag):
    """Ищет все файлы в Vault, которые содержат определенный тег в frontmatter."""
    found_files = []
    # Регулярное выражение для поиска блока тегов внутри YAML
    # Ищем строку '- tag' внутри блока tags:
    tag_pattern = re.compile(r'tags:\s*\n(?:\s*- .+\n?)+')

    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Проверяем наличие тега в контенте (простой и быстрый способ)
                        if f"- {target_tag}" in content or f"  - {target_tag}" in content:
                            found_files.append(os.path.relpath(full_path, vault_path))
                except Exception:
                    continue
    return found_files

def search_by_folder(vault_path, folder_name):
    """Ищет все файлы по частичному совпадению пути папки."""
    found_files = []
    for root, dirs, files in os.walk(vault_path):
        if folder_name in root:
            for file in files:
                if file.endswith(".md"):
                    found_files.append(os.path.relpath(os.path.join(root, file), vault_path))
    return found_files

def main():
    parser = argparse.ArgumentParser(description="Search Obsidian Vault by Metadata")
    parser.add_argument("--vault", required=True, help="Path to the Obsidian vault")
    parser.add_argument("--tag", help="Tag to search for (e.g., 'area/ai')")
    parser.add_argument("--folder", help="Folder name or fragment to search within")

    args = parser.parse_args()

    if not os.path.exists(args.vault):
        print(f"Error: Vault path {args.vault} does not exist.")
        sys.exit(1)

    results = []
    if args.tag:
        results = search_by_tag(args.vault, args.tag)
    elif args.folder:
        results = search_by_folder(args.vault, args.folder)
    else:
        print("Please provide either --tag or --folder")
        sys.exit(1)

    if results:
        print("\n".join(results))
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
