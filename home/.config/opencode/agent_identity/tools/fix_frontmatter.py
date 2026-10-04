import os
import re
from datetime import datetime

def fix_user_profile(vault_path):
    file_path = os.path.join(vault_path, "Areas/Personal/User_Profile.md")
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Извлекаем все теги из всех блоков tags:
    tags = re.findall(r'tags:\s*\n((?:\s*- .+\n)+)', content)
    all_tags = []
    if tags:
        for block in tags:
            found_tags = re.findall(r'-\s*(.+)', block)
            all_tags.extend([t.strip() for t in found_tags])
    
    # Убираем дубликаты
    unique_tags = list(dict.fromkeys(all_tags))

    # 2. Формируем новый правильный Frontmatter (сохраняем остальные поля)
    # Ищем все строки между --- и ---
    parts = re.split(r'^---\s*$', content, flags=re.MULTILINE)
    if len(parts) < 3:
        print("Error: Could not find YAML block.")
        return

    # parts[0] is before first ---
    # parts[1] is the frontmatter
    # parts[2] is the content after second ---

    # Парсим существующие поля (кроме tags)
    fields = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            key = k.strip()
            val = v.strip()
            if key != 'tags': # Мы пересобираем теги сами
                fields[key] = val

    # Собираем новый frontmatter
    new_frontmatter = "---\n"
    if unique_tags:
        new_frontmatter += "tags:\n"
        for t in unique_tags:
            new_frontmatter += f"  - {t}\n"
    
    # Сортируем поля для порядка (created_at, updated_at...)
    for k in sorted(fields.keys()):
        new_frontmatter += f"{k}: {fields[k]}\n"
    new_frontmatter += "---\n\n"

    final_content = new_frontmatter + parts[2].strip()

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"SUCCESS: Fixed {file_path}")

if __name__ == "__main__":
    fix_user_profile("/home/toor/Projects/senior-architect/obsidian-vault-main/")
