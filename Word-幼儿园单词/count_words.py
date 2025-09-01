# -*- coding: utf-8 -*-
import json
import os

def count_words_in_file(filepath):
    """ͳ�Ƶ����ļ��еĵ�������"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            word_count = 0
            for entry in data:
                if isinstance(entry, dict) and 'english' in entry:
                    word_count += 1
            return word_count, len(data)
        else:
            return 0, 0
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0, 0

def analyze_folders():
    """����data��data2�ļ����е�����JSON�ļ�"""
    folders = ['data', 'data2']
    total_words = 0
    total_entries = 0
    file_stats = []
    
    print("=" * 80)
    print("�׶�԰�����ļ�ͳ�Ʒ���")
    print("=" * 80)
    
    for folder in folders:
        if not os.path.exists(folder):
            print(f"�ļ��� {folder} ������")
            continue
            
        print(f"\n? �����ļ���: {folder}")
        print("-" * 50)
        
        folder_words = 0
        folder_entries = 0
        
        for filename in sorted(os.listdir(folder)):
            if filename.endswith('.json'):
                filepath = os.path.join(folder, filename)
                word_count, entry_count = count_words_in_file(filepath)
                
                file_stats.append({
                    'folder': folder,
                    'filename': filename,
                    'words': word_count,
                    'entries': entry_count
                })
                
                folder_words += word_count
                folder_entries += entry_count
                
                print(f"{filename:<25} | ����: {word_count:>4} | ��Ŀ: {entry_count:>4}")
        
        print(f"\n{folder} �ļ���С��: {folder_words} ������, {folder_entries} ����Ŀ")
        total_words += folder_words
        total_entries += folder_entries
    
    print("\n" + "=" * 80)
    print(f"? �ܼ�ͳ��")
    print("=" * 80)
    print(f"�ܵ�����: {total_words}")
    print(f"����Ŀ��: {total_entries}")
    print(f"�����ļ���: {len(file_stats)}")
    
    # ���ļ���С������ʾ
    print("\n? ��������������:")
    print("-" * 50)
    sorted_files = sorted(file_stats, key=lambda x: x['words'], reverse=True)
    for file_info in sorted_files:
        if file_info['words'] > 0:
            print(f"{file_info['folder']}/{file_info['filename']:<25} | {file_info['words']:>4} ������")
    
    return total_words, total_entries, file_stats

if __name__ == "__main__":
    total_words, total_entries, file_stats = analyze_folders()
    
    # ����ͳ�ƽ��
    stats_result = {
        'total_words': total_words,
        'total_entries': total_entries,
        'file_count': len(file_stats),
        'files': file_stats
    }
    
    with open('word_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(stats_result, f, ensure_ascii=False, indent=2)
    
    print(f"\n? ͳ�ƽ���ѱ��浽 word_statistics.json")
    print(f"\n? ��������: ��������ֻ��629�����ʣ���ԭʼ�ļ���{total_words}�����ʣ�")
    print("   ˵�������߼����ܹ����ϸ񣬺ܶ൥�ʱ�����Ϊ'general'���")
    print("   �����Ż������߼��԰������൥�����")