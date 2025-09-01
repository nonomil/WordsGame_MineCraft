// ���ߺ���

// ��ʾ֪ͨ
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = 'notification show';
    
    if (type === 'error') {
        notification.style.background = '#dc3545';
    } else {
        notification.style.background = '#28a745';
    }
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// �����������
function shuffleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
}

// ��ȡ���Ԫ��
function getRandomElements(array, count) {
    const shuffled = shuffleArray(array);
    return shuffled.slice(0, count);
}

// ת��Minecraft Wiki�ļ�ҳ������Ϊֱ��ͼƬ����
async function convertToDirectImageUrl(filePageUrl, filename) {
    // ����Ѿ���ֱ��ͼƬ���ӣ�ֱ�ӷ���
    if (filePageUrl.includes('/images/') || filePageUrl.includes('format=original')) {
        return filePageUrl;
    }
    
    // ��黺��
    if (imageUrlCache.has(filePageUrl)) {
        return imageUrlCache.get(filePageUrl);
    }
    
    // ������ļ�ҳ�����ӣ�ͨ��API��ȡ��ʵͼƬ����
    if (filePageUrl.includes('/w/File:')) {
        try {
            // ��ȡ�ļ���
            const fileName = filename || filePageUrl.split('/File:')[1];
            if (fileName) {
                // ʹ��MediaWiki API��ȡͼƬ��Ϣ
                const apiUrl = `https://minecraft.wiki/api.php?action=query&titles=File:${encodeURIComponent(fileName)}&prop=imageinfo&iiprop=url&format=json&origin=*`;
                const response = await fetch(apiUrl);
                const data = await response.json();
                
                const pages = data.query?.pages;
                if (pages) {
                    const pageId = Object.keys(pages)[0];
                    const imageUrl = pages[pageId]?.imageinfo?.[0]?.url;
                    if (imageUrl) {
                        // ������
                        imageUrlCache.set(filePageUrl, imageUrl);
                        return imageUrl;
                    }
                }
            }
        } catch (error) {
            console.warn('Failed to fetch image URL:', error);
        }
    }
    
    // ����޷�ת��������ԭ����
    return filePageUrl;
}

// ʹ�� UTF-8 ���ַ������� Base64 ���룬��������
function toBase64Utf8(str) {
    const bytes = new TextEncoder().encode(str);
    let binary = '';
    for (let i = 0; i < bytes.length; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
}

// ����ռλ��ͼƬ�����������ַ���
function createPlaceholderImage(text = 'ͼƬ�޷�����') {
    const svg = `
        <svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="200" height="200" fill="#f0f0f0"/>
            <text x="100" y="100" font-family="Arial" font-size="14" fill="#999" text-anchor="middle" dominant-baseline="middle">${text}</text>
        </svg>
    `;
    return `data:image/svg+xml;base64,${toBase64Utf8(svg)}`;
}

// ��������
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ��������
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// ��ʽ��ʱ��
function formatTime(milliseconds) {
    const seconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    
    if (hours > 0) {
        return `${hours}Сʱ${minutes % 60}����`;
    } else if (minutes > 0) {
        return `${minutes}����`;
    } else {
        return `${seconds}��`;
    }
}

// ��ȡ��ǰ�����ַ���
function getCurrentDateString() {
    return new Date().toISOString().slice(0, 10);
}

// �������
function deepClone(obj) {
    if (obj === null || typeof obj !== 'object') {
        return obj;
    }
    
    if (obj instanceof Date) {
        return new Date(obj.getTime());
    }
    
    if (obj instanceof Array) {
        return obj.map(item => deepClone(item));
    }
    
    if (typeof obj === 'object') {
        const clonedObj = {};
        for (const key in obj) {
            if (obj.hasOwnProperty(key)) {
                clonedObj[key] = deepClone(obj[key]);
            }
        }
        return clonedObj;
    }
}

// ����Ƿ�Ϊ�ƶ��豸
function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

// ��ȡ�����ɫ
function getRandomColor() {
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3', '#54a0ff', '#5f27cd'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// ������������֮���������
function daysBetween(date1, date2) {
    const oneDay = 24 * 60 * 60 * 1000;
    const firstDate = new Date(date1);
    const secondDate = new Date(date2);
    return Math.round(Math.abs((firstDate - secondDate) / oneDay));
}

// ��֤JSON��ʽ
function validateVocabularyJSON(data) {
    if (!Array.isArray(data)) {
        throw new Error('�ʿ��ļ���ʽ����Ӧ���������ʽ');
    }
    
    if (data.length === 0) {
        throw new Error('�ʿ��ļ�Ϊ��');
    }
    
    const firstItem = data[0];
    if (!firstItem.word || !firstItem.chinese) {
        throw new Error('�ʿ��ļ���ʽ����ȱ�ٱ�Ҫ�ֶ� word �� chinese');
    }
    
    return true;
}

// ����ΨһID
function generateUniqueId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}