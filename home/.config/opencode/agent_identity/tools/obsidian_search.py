import os
import sys
import re

def obsidian_search(query, vault_path):
    results = []
    keywords = set(re.findall(r'\w+', query.lower()))
    keywords = {kw for kw in keywords if len(kw) > 2}

    if not os.path.exists(vault_path):
        return f"Error: Vault path {vault_path} does not exist."

    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        content_lower = content.lower()

                        # Считаем совпадения ключевых слов
                        match_count = sum(1 for kw in keywords if kw in content_lower)

                        if match_count > 0:
                            # Находим контекст вокруг первого найденного вхождения (примерно)
                            # Для простоты вернем первые 500 символов или фрагмент с совпадением
                            match_index = -1
                            for kw in keywords:
                                idx = content_lower.find(kw)
                                if idx != -1 and (match_index == -1 or idx < match_index):
                                    match_index = idx
                            
                            if match_index != -1:
                                start = max(0, match_index - 100)
                                end = min(len(content), match_index + 400)
                                snippet = content[start:end].replace('\n', ' ')
                            else:
                                snippet = content[:500].replace('\n', ' ')

                            results.append({
                                "path": file_path,
                                "score": match_count,
                                "snippet": snippet.strip()
                            })
                except Exception as e:
                    # Пропускаем битые файлы
                    continue

    # Сортировка по количеству совпадений
    results.sort(key=lambda x: x['score'], reverse=True)
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python obsidian_search.py <vault_path> '<query>'")
        sys.exit(1)

    v_path = sys.argv[1]
    q = sys.argv[2]
    
    matches = obsidian_search(q, v_path)
    
    if isinstance(matches, str):
        print(matches)
    elif not matches:
        print("No matching notes found.")
    else:
        for m in matches:
            print(f"FILE: {m['path']}")
            print(f"SNIPPET: {m['snippet']}")
            print("---")

