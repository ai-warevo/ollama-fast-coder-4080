import json
import sys
import os
from datetime import datetime

def add_to_kb(category, content):
    # Путь к файлу базы знаний внутри папки категории
    target_dir = f"kb/{category}"
    file_path = os.path.join(target_dir, "knowledge.jsonl")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    new_entry = {
        "id": int(datetime.now().timestamp()), # Временный ID на основе времени
        "content": content,
        "metadata": {
            "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category
        }
    }

    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(new_entry, ensure_ascii=False) + "\n")
        print(f"SUCCESS: Added to {file_path}")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Ожидаем: python kb_writer.py <category> "<content>"
    if len(sys.argv) < 3:
        print("Usage: python kb_writer.py <category> '<content>'")
        sys.exit(1)
    
    cat = sys.argv[1]
    cont = sys.argv[2]
    add_to_kb(cat, cont)
