import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')

# Perplexity API Key
PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY', 'YOUR_PERPLEXITY_API_KEY')

# Admin IDs (comma-separated in .env)
ADMIN_IDS = [int(id.strip()) for id in os.getenv('ADMIN_IDS', '').split(',') if id.strip()]

# Teacher IDs (comma-separated in .env)
TEACHER_IDS = [int(id.strip()) for id in os.getenv('TEACHER_IDS', '').split(',') if id.strip()]

# Bot Settings
MAX_CONVERSATION_HISTORY = 10
