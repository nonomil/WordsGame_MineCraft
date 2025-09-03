// Embedded vocabulary data for file:// protocol support
// Auto-generated file, do not edit manually

// �ʿ����ݴ洢
const VOCABULARY_DATA = {
    'words-basic': null, // �������涨��
    '1.�׶�԰--�����ʻ�': null,
    '2.�׶�԰--ѧϰ�ʻ�': null,
    '3.�׶�԰--��Ȼ�ʻ�': null,
    '4.�����ʻ�': null,
    '5.�ճ��ʻ�': null,
    '6.�׶�԰�ʻ�': null
};

// ��̬���شʿ��ļ�
async function loadVocabularyFile(filename) {
    try {
        const script = document.createElement('script');
        script.src = encodeURI(`js/vocabularies/${filename}`);
        document.head.appendChild(script);
        
        return new Promise((resolve, reject) => {
            script.onload = () => resolve();
            script.onerror = () => reject(new Error(`Failed to load ${filename}`));
        });
    } catch (error) {
        console.error(`Error loading vocabulary file ${filename}:`, error);
        throw error;
    }
}

// Load embedded vocabulary data
async function loadEmbeddedVocabulary(vocabName) {
    console.log(`Loading vocabulary: ${vocabName}`);
    
    // ���ȳ��Լ���ӳ������
    if (!window.VOCABULARY_MAPPINGS) {
        try {
            await loadVocabularyFile('mappings.js');
        } catch (error) {
            console.warn('Failed to load vocabulary mappings:', error);
        }
    }
    
    // ��̬���Ҵʿ��ļ�
    let targetFile = null;
    let targetVariable = null;
    
    if (window.VOCABULARY_MAPPINGS) {
        // ����������в���ƥ��Ĵʿ�
        for (const [category, vocabularies] of Object.entries(window.VOCABULARY_MAPPINGS)) {
            const found = vocabularies.find(vocab => vocab.original_name === vocabName);
            if (found) {
                targetFile = found.js_file;
                targetVariable = found.variable_name;
                break;
            }
        }
    }
    
    // ����ӳ�䣨���������ݣ�
    const fallbackMappings = {
        'words-basic': { file: 'basic.js', variable: 'BASIC_VOCABULARY' },
        '1.�׶�԰--�����ʻ�': { file: 'kindergarten_1_basic.js', variable: 'VOCAB_1__________' },
        '2.�׶�԰--ѧϰ�ʻ�': { file: 'kindergarten_2_study.js', variable: 'VOCAB_2__________' },
        '3.�׶�԰--��Ȼ�ʻ�': { file: 'kindergarten_3_nature.js', variable: 'VOCAB_3__________' },
        '4.�����ʻ�': { file: 'kindergarten_4_communication.js', variable: 'VOCAB_4_____' },
        '5.�ճ��ʻ�': { file: 'kindergarten_5_daily.js', variable: 'VOCAB_5_____' },
        '6.�׶�԰�ʻ�': { file: 'kindergarten_6_general.js', variable: 'VOCAB_6______' },
        'kindergarten_vocabulary': { file: 'kindergarten_6_general.js', variable: 'VOCAB_6______' },
        'minecraft_basic': { file: 'minecraft_basic.js', variable: 'VOCAB_1_MINECRAFT____BASIC' },
        'minecraft_intermediate': { file: 'minecraft_intermediate.js', variable: 'VOCAB_2_MINECRAFT____BASIC' },
        'minecraft_advanced': { file: 'minecraft_advanced.js', variable: 'VOCAB_3_MINECRAFT____ADVANCED' },
        'common_vocabulary': { file: 'common_vocabulary.js', variable: 'VOCAB_1____COMMON' },
        'minecraft_image_links': { file: 'minecraft_words_full.js', variable: 'MINECRAFT_3_____' }
    };
    
    if (!targetFile && fallbackMappings[vocabName]) {
        targetFile = fallbackMappings[vocabName].file;
        targetVariable = fallbackMappings[vocabName].variable;
    }
    
    // ����Ƿ��ж�Ӧ�Ĵʿ�����
    if (VOCABULARY_DATA.hasOwnProperty(vocabName) && VOCABULARY_DATA[vocabName]) {
        console.log(`Using cached vocabulary data: ${vocabName}`);
        return VOCABULARY_DATA[vocabName];
    }
    
    // ���Դ��µĴʿ��ļ��м���
    if (targetFile && targetVariable) {
        try {
            await loadVocabularyFile(targetFile);
            if (window[targetVariable]) {
                VOCABULARY_DATA[vocabName] = window[targetVariable];
                console.log(`Successfully loaded vocabulary from file: ${vocabName}`);
                return VOCABULARY_DATA[vocabName];
            }
        } catch (error) {
            console.warn(`Failed to load vocabulary file for ${vocabName}:`, error);
        }
    }
    
    throw new Error(`�ʿ��ļ�δ�ҵ�: ${vocabName}����ȷ�� vocabularies Ŀ¼�´��ڶ�Ӧ JS �ļ������� mappings.js / fallbackMappings ���á�`);
}

// �����ʻ�����
VOCABULARY_DATA['words-basic'] = [
  {
    "word": "smile",
    "standardized": "smile",
    "chinese": "΢Ц",
    "phonetic": "/smile/",
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
    "word": "hello",
    "standardized": "hello",
    "chinese": "���",
    "phonetic": "/h??lo?/",
    "phrase": "Hello there",
    "phraseTranslation": "���ѽ",
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
  }
];

console.log('Vocabulary data loaded successfully');
