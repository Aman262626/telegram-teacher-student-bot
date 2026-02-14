# 🎓 Telegram Teacher-Student Bot with Perplexity AI

एक advanced Telegram bot जो Teacher और Student दोनों के लिए AI-powered learning assistant है। Perplexity API का उपयोग करके real-time information और intelligent responses provide करता है।

## ✨ Features

### 👨‍🏫 Teacher Mode
- Detailed lesson plan creation
- Advanced explanations with latest research
- Comprehensive answers with citations
- Teaching content generation
- Access to current information

### 👨‍🎓 Student Mode
- Simple, easy-to-understand explanations
- Interactive Q&A
- Examples and practice materials
- Beginner-friendly responses
- Personalized learning support

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Telegram account
- Perplexity API key

### Step 1: Clone Repository
```bash
git clone https://github.com/Aman262626/telegram-teacher-student-bot.git
cd telegram-teacher-student-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configuration
1. `.env.example` को `.env` में rename करें
2. अपनी details भरें:

```env
TELEGRAM_TOKEN=your_bot_token_from_botfather
PERPLEXITY_API_KEY=your_perplexity_api_key
ADMIN_IDS=your_telegram_user_id
TEACHER_IDS=teacher_telegram_user_ids
```

### Step 4: Get Required Tokens

#### Telegram Bot Token:
1. Telegram पर @BotFather को message करें
2. `/newbot` command send करें
3. Bot का name और username दें
4. आपको token मिलेगा

#### Perplexity API Key:
1. [Perplexity AI Settings](https://www.perplexity.ai/settings/api) पर जाएं
2. API key generate करें
3. Copy करें और `.env` में paste करें

#### Your Telegram User ID:
1. Telegram पर @userinfobot को message करें
2. आपकी user ID मिल जाएगी

### Step 5: Run Bot
```bash
python bot.py
```

## 📱 Bot Commands

### General Commands
- `/start` - Bot शुरू करें
- `/help` - Help message
- `/role` - अपना current role देखें
- `/clear` - Conversation history clear करें

### Student Commands
- `/ask [question]` - कोई भी question पूछें
- `/explain [topic]` - Simple explanation पाएं
- Simply type your message - Direct chat

### Teacher Commands
- `/teach [topic]` - Lesson plan बनाएं
- `/explain [concept]` - Detailed explanation
- `/ask [question]` - Advanced questions

## 💡 Usage Examples

### For Students:
```
/ask What is photosynthesis?
/explain quantum physics
How do I solve quadratic equations?
```

### For Teachers:
```
/teach introduction to calculus
/explain machine learning algorithms
Create a quiz on Indian history
```

## 🛠️ Deployment

### Deploy on Render:
1. [Render.com](https://render.com) पर account बनाएं
2. New Web Service create करें
3. GitHub repository connect करें
4. Environment variables add करें
5. Deploy करें

### Deploy on Railway:
1. [Railway.app](https://railway.app) पर account बनाएं
2. New Project create करें
3. GitHub repository connect करें
4. Variables add करें
5. Deploy करें

## 🔧 Customization

### Add More Features:
- `bot.py` में नए commands add करें
- Perplexity models change करें (config में)
- Custom prompts बनाएं
- Database integration करें (SQLite/MongoDB)

### Modify Roles:
- `config.py` में teacher/admin IDs update करें
- Role-based features customize करें

## 📊 Project Structure
```
telegram-teacher-student-bot/
│
├── bot.py              # Main bot logic
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── README.md          # Documentation
```

## 🔒 Security
- Never commit `.env` file to GitHub
- Keep your API keys private
- Use environment variables for sensitive data
- Regularly update dependencies

## 🤝 Contributing
Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License
MIT License - Feel free to use and modify

## 🙏 Credits
- Powered by [Perplexity AI](https://www.perplexity.ai/)
- Built with [python-telegram-bot](https://python-telegram-bot.org/)

## 📞 Support
Issues या questions के लिए GitHub Issues use करें।

---

**Made with ❤️ for Teachers and Students**

**Happy Learning! 🎓**
