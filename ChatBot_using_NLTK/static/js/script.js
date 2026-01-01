// ===================== DOM ELEMENTS =====================
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const newChatBtn = document.getElementById('newChatBtn');
const sidebarToggle = document.getElementById('sidebarToggle');
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.querySelector('.sidebar');
const emojiBtn = document.getElementById('emojiBtn');
const emojiPicker = document.getElementById('emojiPicker');
const attachBtn = document.getElementById('attachBtn');
const loadingIndicator = document.getElementById('loadingIndicator');
const toastContainer = document.getElementById('toastContainer');

// ===================== STATE MANAGEMENT =====================
let isLoading = false;
let conversationHistory = [];

// ===================== EVENT LISTENERS =====================
document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
    loadConversationHistory();
});

function initializeEventListeners() {
    // Send message on button click
    sendBtn.addEventListener('click', sendMessage);

    // Send message on Enter key
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey && !isLoading) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Sidebar toggles
    sidebarToggle.addEventListener('click', toggleSidebar);
    menuToggle.addEventListener('click', toggleSidebar);

    // New chat
    newChatBtn.addEventListener('click', startNewChat);

    // Emoji picker
    emojiBtn.addEventListener('click', toggleEmojiPicker);
    document.querySelectorAll('.emoji').forEach(emoji => {
        emoji.addEventListener('click', insertEmoji);
    });

    // Close emoji picker when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.emoji-picker') && !e.target.closest('#emojiBtn')) {
            emojiPicker.classList.remove('active');
        }
    });

    // Auto-expand input as user types
    userInput.addEventListener('input', autoExpandInput);

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.sidebar') && !e.target.closest('.menu-toggle')) {
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('active');
            }
        }
    });

    // Attach button (placeholder functionality)
    attachBtn.addEventListener('click', () => {
        showToast('Fonctionnalité à venir', 'info');
    });
}

// ===================== MESSAGE HANDLING =====================
async function sendMessage() {
    const message = userInput.value.trim();

    if (!message || isLoading) return;

    // Add user message to chat
    addMessage(message, 'user');
    conversationHistory.push({ role: 'user', content: message });

    // Clear input
    userInput.value = '';
    resetInputHeight();
    emojiPicker.classList.remove('active');

    // Show loading indicator
    isLoading = true;
    showLoadingIndicator();

    try {
        // Send message to Flask backend
        const response = await fetch('/chat_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Add bot response to chat
        setTimeout(() => {
            addMessage(data.response, 'bot');
            conversationHistory.push({ role: 'bot', content: data.response });
            saveConversationHistory();
        }, 300);

    } catch (error) {
        console.error('Error:', error);
        showToast('Une erreur s\'est produite. Veuillez réessayer.', 'error');
        addMessage('Désolé, une erreur s\'est produite. Veuillez réessayer.', 'bot');
    } finally {
        isLoading = false;
        hideLoadingIndicator();
        userInput.focus();
    }
}

function addMessage(text, sender) {
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container', sender);

    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', `${sender}-message`);

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');
    contentDiv.textContent = text;

    const timeSpan = document.createElement('span');
    timeSpan.classList.add('message-time');
    timeSpan.textContent = getCurrentTime();

    messageDiv.appendChild(contentDiv);
    messageDiv.appendChild(timeSpan);
    messageContainer.appendChild(messageDiv);

    chatMessages.appendChild(messageContainer);

    // Scroll to bottom
    scrollToBottom();
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
}

// ===================== SIDEBAR & NAVIGATION =====================
function toggleSidebar() {
    sidebar.classList.toggle('active');
}

function startNewChat() {
    if (confirm('Êtes-vous sûr de vouloir commencer une nouvelle conversation ?')) {
        // Clear messages except initial message
        const messages = chatMessages.querySelectorAll('.message-container:not(.initial-message)');
        messages.forEach(msg => msg.remove());

        // Reset conversation history
        conversationHistory = [];
        localStorage.removeItem('conversationHistory');

        // Clear input
        userInput.value = '';
        resetInputHeight();

        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            sidebar.classList.remove('active');
        }

        showToast('Nouvelle conversation commencée', 'success');
        userInput.focus();
    }
}

// ===================== EMOJI PICKER =====================
function toggleEmojiPicker() {
    emojiPicker.classList.toggle('active');
}

function insertEmoji(e) {
    const emoji = e.target.dataset.emoji;
    userInput.value += emoji;
    emojiPicker.classList.remove('active');
    autoExpandInput();
    userInput.focus();
}

// ===================== INPUT MANAGEMENT =====================
function autoExpandInput() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
}

function resetInputHeight() {
    userInput.style.height = 'auto';
}

// ===================== LOADING INDICATOR =====================
function showLoadingIndicator() {
    loadingIndicator.classList.add('active');
}

function hideLoadingIndicator() {
    loadingIndicator.classList.remove('active');
}

// ===================== TOAST NOTIFICATIONS =====================
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.classList.add('toast', type);
    toast.textContent = message;

    toastContainer.appendChild(toast);

    // Auto-remove after 3 seconds
    setTimeout(() => {
        toast.style.animation = 'slideInRight 0.3s ease-out reverse';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// ===================== LOCAL STORAGE =====================
function saveConversationHistory() {
    localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
}

function loadConversationHistory() {
    const saved = localStorage.getItem('conversationHistory');
    if (saved) {
        conversationHistory = JSON.parse(saved);
        // Optionally restore messages to UI
    }
}

// ===================== RESPONSIVE BEHAVIOR =====================
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        sidebar.classList.remove('active');
    }
});

// ===================== ANIMATION ON SCROLL =====================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// ===================== KEYBOARD SHORTCUTS =====================
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K to focus input
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        userInput.focus();
    }

    // Escape to close emoji picker
    if (e.key === 'Escape') {
        emojiPicker.classList.remove('active');
    }

    // Escape to close sidebar on mobile
    if (e.key === 'Escape' && window.innerWidth <= 768) {
        sidebar.classList.remove('active');
    }
});

// ===================== ACCESSIBILITY =====================
// Improve focus management
userInput.addEventListener('focus', () => {
    userInput.parentElement.style.boxShadow = '0 0 20px rgba(124, 58, 237, 0.3)';
});

userInput.addEventListener('blur', () => {
    userInput.parentElement.style.boxShadow = 'none';
});

// ===================== INITIAL FOCUS =====================
setTimeout(() => {
    userInput.focus();
}, 500);

// ===================== PREVENT INITIAL MESSAGE FROM BEING EDITED =====================
document.addEventListener('DOMContentLoaded', () => {
    const initialMessage = document.querySelector('.initial-message');
    if (initialMessage) {
        observer.observe(initialMessage);
    }
});
