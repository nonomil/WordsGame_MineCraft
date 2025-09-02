// �����ʻ�����
const COMMUNICATION_VOCABULARY = [
  {
    "word": "mine",
    "standardized": "mine",
    "chinese": "�ھ�",
    "phonetic": "",
    "phrase": "Let's mine some diamonds!",
    "phraseTranslation": "����ȥ����ʯ�ɣ�",
    "difficulty": "basic",
    "category": "basic_actions",
    "imageURLs": [
      {
        "filename": "Mining-Pixel-Icons-1.png",
        "url": "https://craftpix.net/wp-content/uploads/2024/10/Mining-Pixel-Icons-1.png",
        "type": "Default"
      }
    ]
  },
  {
    "word": "dig",
    "standardized": "dig",
    "chinese": "��",
    "phonetic": "",
    "phrase": "Dig down carefully!",
    "phraseTranslation": "С�������ڣ�",
    "difficulty": "basic",
    "category": "basic_actions",
    "imageURLs": [
      {
        "filename": "",
        "url": "",
        "type": "Default"
      }
    ]
  },
  {
    "word": "build",
    "standardized": "build",
    "chinese": "����",
    "phonetic": "",
    "phrase": "I'm building a castle",
    "phraseTranslation": "���ڽ��Ǳ�",
    "difficulty": "basic",
    "category": "basic_actions",
    "imageURLs": [
      {
        "filename": "hammer.png",
        "url": "https://img.icons8.com/color/48/hammer.png",
        "type": "Default"
      }
    ]
  },
  {
    "word": "craft",
    "standardized": "craft",
    "chinese": "�ϳ�",
    "phonetic": "",
    "phrase": "Can you craft some tools?",
    "phraseTranslation": "���ܺϳ�һЩ������",
    "difficulty": "basic",
    "category": "basic_actions",
    "imageURLs": [
      {
        "filename": "gear.png",
        "url": "https://img.icons8.com/color/48/gear.png",
        "type": "Default"
      }
    ]
  },
  {
    "word": "hello",
    "standardized": "hello",
    "chinese": "���",
    "phonetic": "/h??lo?/",
    "phrase": "Hello there!",
    "phraseTranslation": "���ѽ��",
    "difficulty": "basic",
    "category": "greeting",
    "imageURLs": [
      {
        "filename": "hello.jpg",
        "url": "https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?w=400&q=80&auto=format&fit=crop",
        "type": "Concept Image"
      }
    ]
  },
  {
    "word": "thank you",
    "standardized": "thank you",
    "chinese": "лл",
    "phonetic": "/��??k ju?/",
    "phrase": "Thank you very much!",
    "phraseTranslation": "�ǳ���л��",
    "difficulty": "basic",
    "category": "greeting",
    "imageURLs": [
      {
        "filename": "thank-you.jpg",
        "url": "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400&q=80&auto=format&fit=crop",
        "type": "Concept Image"
      }
    ]
  }
];

// �����ʿ�����
if (typeof module !== 'undefined' && module.exports) {
  module.exports = COMMUNICATION_VOCABULARY;
} else if (typeof window !== 'undefined') {
  window.COMMUNICATION_VOCABULARY = COMMUNICATION_VOCABULARY;
}