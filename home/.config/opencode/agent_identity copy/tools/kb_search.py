import json
import sys
import os
import re

def smart_search(query, base_dir='kb'):
    results = []
    keywords = set(re.findall(r'\w+', query.lower()))
    # Исключаем слишком короткие слова (предлоги и т.д.)
    keywords = {kw for kw in keywords if len(kw) > 2}

    if not os.path.exists(base_dir):
        return []

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.jsonl'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if not line: continue
                            data = json.loads(line)
                            content = data.get('content', '')
                            content_lower = content.lower()
                            
                            # Проверка на совпадение ключевых слов
                            match_count = sum(1 for kw in keywords if kw in content_lower)
                            
                            if match_count > 0:
                                # Добавляем метаданные о том, где нашли
                                data['found_in'] = file_path
                                results.append((match_count, data))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}", file=sys.stderr)

    # Сортируем результаты по количеству совпадений (сначала самые релевантные)
    results.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in results]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    q = sys.argv[1]
    matches = smart_search(q)
    for m in matches:
        # Выводим в упрощенном виде для удобного парсинга агентом
        print(f"SOURCE: {m.get('found_in', 'unknown')}")
        print(f"CONTENT: {m['content']}")
        print("---")
