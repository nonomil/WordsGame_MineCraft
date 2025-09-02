// �����ʻ�����
const BASIC_VOCABULARY = [
  {
    "word": "smile",
    "standardized": "smile",
    "chinese": "΢Ц",
    "phonetic": "/sma?l/",
    "phrase": "Smile happily",
    "phraseTranslation": "���ĵ�΢Ц",
    "difficulty": "basic",
    "category": "general",
    "imageURLs": [
      {
        "filename": "smile.jpg",
        "url": "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400&q=80&auto=format&fit=crop",
        "type": "Concept Image"
      }
    ]
  },
  {
    "word": "happy",
    "standardized": "happy",
    "chinese": "���ĵ�",
    "phonetic": "/?h?pi/",
    "phrase": "Happy child",
    "phraseTranslation": "���ĵ�С����",
    "difficulty": "basic",
    "category": "general",
    "imageURLs": [
      {
        "filename": "happy.jpg",
        "url": "https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=400&q=80&auto=format&fit=crop",
        "type": "Concept Image"
      }
    ]
  },
  {
    "word": "walk",
    "standardized": "walk",
    "chinese": "��·",
    "phonetic": "/w??k/",
    "phrase": "Walk slowly",
    "phraseTranslation": "������·",
    "difficulty": "basic",
    "category": "action",
    "imageURLs": [
      {
        "filename": "walk.jpg",
        "url": "https://images.unsplash.com/photo-1516575150278-77136aed6920?w=400",
        "type": "Concept Image"
      }
    ]
  },
  {
    "word": "read",
    "standardized": "read",
    "chinese": "�Ķ�",
    "phonetic": "/ri?d/",
    "phrase": "Read a storybook",
    "phraseTranslation": "�Ķ�������",
    "difficulty": "basic",
    "category": "general",
    "imageURLs": [
      {
        "filename": "read.jpg",
        "url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400",
        "type": "Concept Image"
      }
    ]
  },
  {
    "word": "sleep",
    "standardized": "sleep",
    "chinese": "˯��",
    "phonetic": "/sli?p/",
    "phrase": "Baby is sleeping",
    "phraseTranslation": "����˯����",
    "difficulty": "basic",
    "category": "general",
    "imageURLs": [
      {
        "filename": "sleep.jpg",
        "url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80&auto=format&fit=crop",
        "type": "Concept Image"
      }
    ]
  }
];

// �����ʿ�����
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BASIC_VOCABULARY;
} else if (typeof window !== 'undefined') {
  window.BASIC_VOCABULARY = BASIC_VOCABULARY;
}