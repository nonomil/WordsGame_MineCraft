# -*- coding: utf-8 -*-
import json
import os

def load_json_file(filepath):
    """����JSON�ļ�"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def extract_words_from_file(data):
    """���ļ���������ȡ�����б�"""
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and 'words' in data:
        return data['words']
    else:
        return []

def categorize_word(word_entry):
    """���ݵ������ݾ�������"""
    word = word_entry.get('word', '').lower()
    category = word_entry.get('category', '')
    subcategory = word_entry.get('subcategory', '')
    
    # �������Ȼ��
    nature_keywords = ['animal', 'nature', 'living', 'cat', 'dog', 'bird', 'fish', 'tree', 'flower', 'sun', 'moon', 'star']
    if any(keyword in category.lower() for keyword in nature_keywords) or \
       any(keyword in word for keyword in ['cat', 'dog', 'bird', 'fish', 'tree', 'flower', 'sun', 'moon', 'star', 'lion', 'bear']):
        return 'nature_animals'
    
    # �������Ʒ��
    body_object_keywords = ['body', 'object', 'clothing', 'food', 'toy', 'head', 'hand', 'foot', 'eye', 'nose']
    if any(keyword in category.lower() for keyword in body_object_keywords) or \
       any(keyword in word for keyword in ['head', 'hand', 'foot', 'eye', 'nose', 'shirt', 'shoes', 'apple', 'ball', 'doll']):
        return 'body_objects'
    
    # ѧϰ����״��
    learning_keywords = ['learning', 'shape', 'school', 'geometric', 'circle', 'square', 'triangle']
    if any(keyword in category.lower() for keyword in learning_keywords) or \
       any(keyword in word for keyword in ['school', 'book', 'pen', 'circle', 'square', 'triangle']):
        return 'learning_shapes'
    
    # Ĭ�Ϲ���Ϊ�����ʻ�
    return 'basic_vocabulary'

def process_all_files():
    """���������ļ������·���"""
    files = [
        'kindergarten_basic_complete.json',
        'kindergarten_basic_vocabulary.json', 
        'kindergarten_body_objects.json',
        'kindergarten_learning_complete.json',
        'kindergarten_learning_shapes.json',
        'kindergarten_nature_animals.json',
        'kindergarten_nature_complete.json',
        'kindergarten_objects_complete.json'
    ]
    
    # ������Ҫ����
    categories = {
        'basic_vocabulary': [],
        'nature_animals': [],
        'learning_shapes': []
    }
    
    processed_words = set()  # ����ȥ��
    
    for filename in files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            data = load_json_file(filename)
            if data:
                words = extract_words_from_file(data)
                for word_entry in words:
                    if isinstance(word_entry, dict) and 'word' in word_entry:
                        word_key = word_entry['word'].lower()
                        if word_key not in processed_words:
                            processed_words.add(word_key)
                            
                            # ת��ΪMinecraft��ʽ
                            minecraft_entry = {
                                "word": word_entry.get('word', ''),
                                "standardized": word_entry.get('standardized', word_entry.get('word', '')),
                                "chinese": word_entry.get('chinese', ''),
                                "phonetic": word_entry.get('phonetic', ''),
                                "phrase": word_entry.get('phrase', ''),
                                "phraseTranslation": word_entry.get('phraseTranslation', ''),
                                "difficulty": word_entry.get('difficulty', 'basic'),
                                "category": word_entry.get('category', 'general'),
                                "imageURLs": word_entry.get('imageURLs', [])
                            }
                            
                            # ��������
                            target_category = categorize_word(word_entry)
                            categories[target_category].append(minecraft_entry)
    
    return categories

def save_new_files(categories):
    """�����µķ����ļ�"""
    file_mapping = {
        'basic_vocabulary': 'kindergarten_basic.json',
        'nature_animals': 'kindergarten_nature.json', 
        'learning_shapes': 'kindergarten_learning.json'
    }
    
    for category, words in categories.items():
        filename = file_mapping[category]
        print(f"Saving {len(words)} words to {filename}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal words processed: {sum(len(words) for words in categories.values())}")
    for category, words in categories.items():
        print(f"{category}: {len(words)} words")

if __name__ == "__main__":
    print("���������׶�԰�����ļ�...")
    print("��8���ļ��ϲ�Ϊ3����Ҫ����")
    print("��ʽת��ΪMinecraft�ʻ������ʽ")
    print("=" * 50)
    
    categories = process_all_files()
    save_new_files(categories)
    
    print("\n? �ļ�����������ɣ�")
    print("���ļ�:")
    print("- kindergarten_basic.json (�����ʻ�)")
    print("- kindergarten_nature.json (��Ȼ����)")
    print("- kindergarten_learning.json (ѧϰ��״)")