# MineCraftѧ������Ϸ - �ʻ��ļ�����˵��

## �ļ��ṹ

����Ŀ�Ĵʻ��ļ��Ѻϲ�����Ϊ����4����ҪJSON�ļ���

### ? ��Ŀ¼��Ҫ�ļ�
- `minecraft_vocabulary.json` - ������Minecraft��Ϸ�ʻ� (1181���ʻ�)
- `daily_vocabulary.json` - �ճ�����ʻ� (138���ʻ�)
- `communication_vocabulary.json` - ������ͨ�ʻ� (Լ150���ʻ�)
- `image_resources.json` - ͼƬ��Դ���� (1174����Դ)

### ? ԭʼ����Ŀ¼�����ݣ�

### ? minecraft_vocabulary/ - Minecraft��Ϸ�ʻ�
����Minecraft��Ϸ�е�רҵ�ʻ㣬���Ѷȷּ���
- `minecraft_basic.json` - �����ʻ�
- `minecraft_intermediate.json` - �м��ʻ�  
- `minecraft_advanced.json` - �߼��ʻ�

### ? daily_vocabulary/ - �ճ�����ʻ�
�����ճ�������׶�԰�׶εĻ����ʻ㣺
- `common_vocabulary.json` - ͨ���ճ��ʻ�
- `kindergarten_vocabulary.json` - �׶�԰�ʻ�
- `kindergarten_vocabulary.md` - �׶�԰�ʻ�˵���ĵ�

### ? communication_vocabulary/ - ������ͨ�ʻ�
������Ϸ�г��õĽ����͹�ͨ�ʻ㣺
- `minecraft_communication_vocab.json` - �����ʻ�����
- `minecraft_communication_vocab.md` - �����ʻ�˵���ĵ�

### ?? image_resources/ - ͼƬ��Դ�ļ�
�������дʻ���ص�ͼƬ���Ӻ���Դ��
- `minecraft_image_links.json` - ����ͼƬ��������
- `minecraft_image_links_A_F.json` - A-F��ĸ��ͷ��ͼƬ����
- `minecraft_image_links_G_M.json` - G-M��ĸ��ͷ��ͼƬ����
- `minecraft_image_links_N_S.json` - N-S��ĸ��ͷ��ͼƬ����
- `minecraft_image_links_T_Z.json` - T-Z��ĸ��ͷ��ͼƬ����
- `minecraft_vocabulary_with_images_and_chinese.txt` - ��ͼƬ�����ĵĴʻ��ı�

### ? tools/ - ���߽ű�
�������ڴ��������ʻ����ݵ�Python�ű���
- `organize_vocabulary.py` - �ʻ�����ű�
- `process_words.py` - �ʻ㴦��ű�
- `process_words_enhanced.py` - ��ǿ��ʻ㴦��ű�

## ʹ��˵��

### ? �Ƽ�ѧϰ·��
1. **ѧϰ�����ʻ�**���� `daily_vocabulary.json` ��ʼ�������ճ�����ʻ�
2. **ѧϰ��Ϸ�ʻ�**��ʹ�� `minecraft_vocabulary.json`����difficulty�ֶΣ�basic �� intermediate �� advanced��˳��ѧϰ
3. **��ϰ����**��ʹ�� `communication_vocabulary.json` �еĴʻ������Ϸ�ڽ���
4. **�鿴ͼƬ**���� `image_resources.json` ���ҵ���Ӧ��ͼƬ��Դ

### ? ���ݴ���
- ʹ�� `tools/` Ŀ¼�еĽű����дʻ����ݵĴ���ͷ���
- �ϲ��ű���`merge_minecraft_vocab.py`, `merge_daily_vocab.py`, `merge_image_resources.py`

## �ļ���ʽ˵��

����JSON�ļ�����ѭͳһ�����ݽṹ��
```json
{
  "word": "����",
  "standardized": "��׼������",
  "chinese": "���ķ���",
  "phonetic": "����",
  "phrase": "����",
  "phraseTranslation": "���䷭��",
  "difficulty": "�Ѷȼ���",
  "category": "����",
  "imageURLs": ["ͼƬ��������"]
}
```

�������ʱ�䣺2025��1��