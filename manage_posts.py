import json
import os
import datetime
import argparse
import re

CONTENTS_DIR = '.'
INDEX_FILE = os.path.join(CONTENTS_DIR, 'index.json')

def load_index():
    if not os.path.exists(INDEX_FILE):
        return {}
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_index(data):
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '_', text)
    return text

def create_post(title, category='posts', tags=None, summary=''):
    index_data = load_index()
    
    filename = slugify(title)
    date_str = datetime.date.today().isoformat()
    
    # Ensure category directory exists
    category_dir = os.path.join(CONTENTS_DIR, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
        
    # Create markdown file
    filepath = os.path.join(category_dir, f"{filename}.md")
    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists.")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("")
    
    print(f"Created {filepath}")

    # Update index.json
    # Navigate to category in index_data
    # If category is nested (e.g. foo/bar), we need to traverse/create
    
    parts = category.split('/')
    current = index_data
    for part in parts:
        if part not in current:
            current[part] = {}
        current = current[part]
        
    # Add post metadata
    current[filename] = {
        "title": title,
        "date": date_str,
        "tags": tags or [],
        "summary": summary
    }
    
    save_index(index_data)
    print(f"Updated {INDEX_FILE}")

def main():
    parser = argparse.ArgumentParser(description='Manage blog posts')
    subparsers = parser.add_subparsers(dest='command')

    new_parser = subparsers.add_parser('new', help='Create a new post')
    new_parser.add_argument('title', help='Post title')
    new_parser.add_argument('--category', '-c', default='posts', help='Category (folder path)')
    new_parser.add_argument('--tags', '-t', nargs='+', help='Tags')
    new_parser.add_argument('--summary', '-s', default='', help='Summary')

    args = parser.parse_args()

    if args.command == 'new':
        create_post(args.title, args.category, args.tags, args.summary)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
