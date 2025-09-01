// �ʿ������غ���

// ����Ԥ��ʿ�
async function loadVocabulary() {
    const selectedVocab = document.getElementById('vocabSelect').value;
    
    try {
        const vocabUrl = `${CONFIG.VOCAB_PATH}${selectedVocab}.json`;
        console.log('Loading vocabulary from:', vocabUrl);
        const response = await fetch(vocabUrl);
        if (!response.ok) {
            throw new Error(`�ʿ��ļ�δ�ҵ�: ${vocabUrl} (״̬: ${response.status})`);
        }
        
        const data = await response.json();
        validateVocabularyJSON(data);
        
        currentVocabulary = data;
        currentWordIndex = 0;
        
        // ������׶�԰ģʽ����ʼ������
        if (getSettings().kindergartenMode && (selectedVocab.includes('�׶�԰') || selectedVocab === 'kindergarten_vocabulary')) {
            initializeKindergartenMode();
        }
        
        showNotification(`�ɹ����� ${currentVocabulary.length} �����ʣ�`);
        updateWordDisplay();
        updateStats();
        enableControls();
        
    } catch (error) {
        showNotification('���شʿ�ʧ��: ' + error.message, 'error');
        console.error('Error loading vocabulary:', error);
    }
}

// �����Զ���ʿ�
function loadCustomVocabulary() {
    const fileInput = document.getElementById('customVocabFile');
    const file = fileInput.files[0];
    
    if (!file) {
        showNotification('����ѡ��һ��JSON�ļ�', 'error');
        return;
    }
    
    if (!file.name.toLowerCase().endsWith('.json')) {
        showNotification('��ѡ��JSON��ʽ���ļ�', 'error');
        return;
    }
    
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const jsonData = JSON.parse(e.target.result);
            validateVocabularyJSON(jsonData);
            
            currentVocabulary = jsonData;
            currentWordIndex = 0;
            
            // ����Ƿ������׶�԰ģʽ
            if (getSettings().kindergartenMode) {
                initializeKindergartenMode();
            }
            
            showNotification(`�ɹ������Զ���ʿ⣺${currentVocabulary.length} �����ʣ�`);
            updateWordDisplay();
            updateStats();
            enableControls();
            
        } catch (error) {
            showNotification('�����Զ���ʿ�ʧ��: ' + error.message, 'error');
            console.error('Error loading custom vocabulary:', error);
        }
    };
    
    reader.onerror = function() {
        showNotification('�ļ���ȡʧ��', 'error');
    };
    
    reader.readAsText(file, 'UTF-8');
}

// ������ǰ�ʿ�
function exportCurrentVocab() {
    if (currentVocabulary.length === 0) {
        showNotification('û�дʿ�ɵ���', 'error');
        return;
    }
    
    const dataStr = JSON.stringify(currentVocabulary, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `vocabulary_${getCurrentDateString()}.json`;
    a.click();
    
    URL.revokeObjectURL(url);
    showNotification('�ʿ��ѵ���');
}

// �������ʻ�
function shuffleWords() {
    if (currentVocabulary.length === 0) {
        showNotification('���ȼ��شʿ�', 'error');
        return;
    }
    
    currentVocabulary = shuffleArray(currentVocabulary);
    currentWordIndex = 0;
    
    // ���³�ʼ���׶�԰ģʽ
    if (getSettings().kindergartenMode) {
        initializeKindergartenMode();
    }
    
    updateWordDisplay();
    showNotification('�ʻ����������');
}

// ���ÿ��ư�ť
function enableControls() {
    const nextBtn = document.querySelector('.control-btn.next');
    const prevBtn = document.querySelector('.control-btn.prev');
    const exportBtn = document.getElementById('exportBtn');
    
    if (nextBtn) nextBtn.disabled = false;
    if (prevBtn) prevBtn.disabled = currentWordIndex === 0;
    if (exportBtn) exportBtn.disabled = false;
}

// ��ȡ��ǰ����
function getCurrentWord() {
    if (currentVocabulary.length === 0 || currentWordIndex >= currentVocabulary.length) {
        return null;
    }
    return currentVocabulary[currentWordIndex];
}

// ��ȡ�ʿ�ͳ����Ϣ
function getVocabularyStats() {
    if (currentVocabulary.length === 0) {
        return {
            total: 0,
            categories: {},
            difficulties: {}
        };
    }
    
    const stats = {
        total: currentVocabulary.length,
        categories: {},
        difficulties: {}
    };
    
    currentVocabulary.forEach(word => {
        // ͳ�Ʒ���
        const category = word.category || 'δ����';
        stats.categories[category] = (stats.categories[category] || 0) + 1;
        
        // ͳ���Ѷ�
        const difficulty = word.difficulty || 'δ֪';
        stats.difficulties[difficulty] = (stats.difficulties[difficulty] || 0) + 1;
    });
    
    return stats;
}

// ������ɸѡ�ʻ�
function filterByCategory(category) {
    if (!category || category === 'all') {
        return currentVocabulary;
    }
    
    return currentVocabulary.filter(word => 
        (word.category || 'δ����') === category
    );
}

// ���Ѷ�ɸѡ�ʻ�
function filterByDifficulty(difficulty) {
    if (!difficulty || difficulty === 'all') {
        return currentVocabulary;
    }
    
    return currentVocabulary.filter(word => 
        (word.difficulty || 'δ֪') === difficulty
    );
}

// �����ʻ�
function searchVocabulary(query) {
    if (!query) {
        return currentVocabulary;
    }
    
    const lowerQuery = query.toLowerCase();
    return currentVocabulary.filter(word => 
        word.word.toLowerCase().includes(lowerQuery) ||
        word.chinese.toLowerCase().includes(lowerQuery) ||
        (word.standardized && word.standardized.toLowerCase().includes(lowerQuery))
    );
}

// ��ȡ���ƴʻ㣨��������ѡ����ѡ�
function getSimilarWords(targetWord, count = 3) {
    const otherWords = currentVocabulary.filter(word => 
        word.chinese !== targetWord.chinese
    );
    
    if (otherWords.length === 0) {
        return [];
    }
    
    // ����ѡ��ͬ���Ĵʻ�
    const sameCategory = otherWords.filter(word => 
        word.category === targetWord.category
    );
    
    const sameDifficulty = otherWords.filter(word => 
        word.difficulty === targetWord.difficulty
    );
    
    // ��Ϻ�ѡ�ʻ�
    let candidates = [];
    
    // ���ͬ���ʻ�
    if (sameCategory.length > 0) {
        candidates.push(...getRandomElements(sameCategory, Math.min(count, sameCategory.length)));
    }
    
    // ������������ͬ�Ѷȴʻ�
    if (candidates.length < count && sameDifficulty.length > 0) {
        const needed = count - candidates.length;
        const additional = sameDifficulty.filter(word => 
            !candidates.some(c => c.chinese === word.chinese)
        );
        candidates.push(...getRandomElements(additional, Math.min(needed, additional.length)));
    }
    
    // ����������������������ʻ�
    if (candidates.length < count) {
        const needed = count - candidates.length;
        const remaining = otherWords.filter(word => 
            !candidates.some(c => c.chinese === word.chinese)
        );
        candidates.push(...getRandomElements(remaining, Math.min(needed, remaining.length)));
    }
    
    return candidates.slice(0, count);
}

// ���ʻ�������
function validateWordData(word) {
    const required = ['word', 'chinese'];
    const missing = required.filter(field => !word[field]);
    
    if (missing.length > 0) {
        console.warn(`�ʻ����ݲ�������ȱ���ֶ�: ${missing.join(', ')}`, word);
        return false;
    }
    
    return true;
}

// �޸��ʻ�����
function fixWordData(word) {
    const fixed = { ...word };
    
    // ȷ���б�׼������
    if (!fixed.standardized) {
        fixed.standardized = fixed.word;
    }
    
    // ȷ���з���
    if (!fixed.category) {
        fixed.category = 'δ����';
    }
    
    // ȷ�����Ѷ�
    if (!fixed.difficulty) {
        fixed.difficulty = 'basic';
    }
    
    return fixed;
}