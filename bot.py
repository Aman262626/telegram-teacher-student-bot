import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import aiohttp
from config import TELEGRAM_TOKEN, PERPLEXITY_API_KEY, TEACHER_IDS, ADMIN_IDS

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# User role storage (in production, use database)
user_roles = {}  # user_id: 'teacher' or 'student'
conversation_history = {}  # user_id: [messages]

class PerplexityAPI:
    """Perplexity API client"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"
    
    async def ask(self, messages, model="llama-3.1-sonar-small-128k-online"):
        """Send request to Perplexity API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, json=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['choices'][0]['message']['content']
                else:
                    error_text = await response.text()
                    logger.error(f"Perplexity API error: {error_text}")
                    return "Sorry, I encountered an error. Please try again."

perplexity = PerplexityAPI(PERPLEXITY_API_KEY)

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    user = update.effective_user
    user_id = user.id
    
    # Check if user is admin/teacher
    if user_id in ADMIN_IDS or user_id in TEACHER_IDS:
        user_roles[user_id] = 'teacher'
        role = "👨‍🏫 Teacher"
    else:
        user_roles[user_id] = 'student'
        role = "👨‍🎓 Student"
    
    welcome_message = f"""🎓 **Welcome to Teacher-Student Bot!**

Hello {user.first_name}!
Your Role: {role}

**Available Commands:**
/start - Start the bot
/help - Get help
/role - Check your role
/clear - Clear conversation history
/ask - Ask a question (for students)
/teach - Teach mode (for teachers)
/explain - Detailed explanation mode

Simply send your message to chat with the AI!
    """
    
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command handler"""
    user_id = update.effective_user.id
    role = user_roles.get(user_id, 'student')
    
    if role == 'teacher':
        help_text = """👨‍🏫 **Teacher Mode Help**

**Your Capabilities:**
- Create detailed lesson plans
- Answer advanced questions
- Get comprehensive explanations
- Access to latest information via Perplexity AI

**Commands:**
/teach [topic] - Create lesson plan
/explain [concept] - Deep explanation
/ask [question] - General questions

**Tips:**
- Be specific with your questions
- Use /teach for structured content
- Conversation history is maintained
        """
    else:
        help_text = """👨‍🎓 **Student Mode Help**

**Your Capabilities:**
- Ask questions on any topic
- Get easy-to-understand explanations
- Learn with examples
- Access latest information

**Commands:**
/ask [question] - Ask anything
/explain [topic] - Get simple explanation

**Tips:**
- Ask clear questions
- Request examples if needed
- Say "explain like I'm 5" for simpler answers
        """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def role_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user role"""
    user_id = update.effective_user.id
    role = user_roles.get(user_id, 'student')
    
    role_emoji = "👨‍🏫" if role == 'teacher' else "👨‍🎓"
    await update.message.reply_text(f"Your current role: {role_emoji} **{role.title()}**", parse_mode='Markdown')

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear conversation history"""
    user_id = update.effective_user.id
    conversation_history[user_id] = []
    await update.message.reply_text("✅ Conversation history cleared!")

async def ask_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ask question command"""
    user_id = update.effective_user.id
    question = ' '.join(context.args)
    
    if not question:
        await update.message.reply_text("Please provide a question. Usage: /ask [your question]")
        return
    
    await handle_message_with_role(update, context, question)

async def teach_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Teach mode for teachers"""
    user_id = update.effective_user.id
    role = user_roles.get(user_id, 'student')
    
    if role != 'teacher':
        await update.message.reply_text("⚠️ This command is only for teachers!")
        return
    
    topic = ' '.join(context.args)
    if not topic:
        await update.message.reply_text("Please provide a topic. Usage: /teach [topic]")
        return
    
    # Create teaching prompt
    prompt = f"Create a comprehensive lesson plan for teaching '{topic}'. Include: 1) Learning objectives, 2) Key concepts, 3) Examples, 4) Practice exercises, 5) Assessment methods."
    
    await update.message.reply_text("📚 Creating lesson plan...")
    
    messages = [{"role": "system", "content": "You are an expert teacher creating educational content."},
                {"role": "user", "content": prompt}]
    
    response = await perplexity.ask(messages)
    await update.message.reply_text(response, parse_mode='Markdown')

async def explain_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Explain concept command"""
    concept = ' '.join(context.args)
    
    if not concept:
        await update.message.reply_text("Please provide a concept. Usage: /explain [concept]")
        return
    
    user_id = update.effective_user.id
    role = user_roles.get(user_id, 'student')
    
    if role == 'student':
        prompt = f"Explain '{concept}' in simple terms with examples, as if explaining to a student."
    else:
        prompt = f"Provide a detailed explanation of '{concept}' with advanced concepts, applications, and latest developments."
    
    await update.message.reply_text("🔍 Generating explanation...")
    
    messages = [{"role": "system", "content": "You are a helpful educational assistant."},
                {"role": "user", "content": prompt}]
    
    response = await perplexity.ask(messages)
    await update.message.reply_text(response, parse_mode='Markdown')

async def handle_message_with_role(update: Update, context: ContextTypes.DEFAULT_TYPE, custom_text=None):
    """Handle regular messages based on user role"""
    user_id = update.effective_user.id
    user_text = custom_text or update.message.text
    role = user_roles.get(user_id, 'student')
    
    # Initialize conversation history
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    
    # Add user message to history
    conversation_history[user_id].append({"role": "user", "content": user_text})
    
    # Keep only last 10 messages
    if len(conversation_history[user_id]) > 10:
        conversation_history[user_id] = conversation_history[user_id][-10:]
    
    # Create system prompt based on role
    if role == 'teacher':
        system_prompt = "You are an AI assistant for teachers. Provide detailed, comprehensive answers with latest information, research, and advanced concepts. Include citations and sources when relevant."
    else:
        system_prompt = "You are an AI tutor for students. Explain concepts clearly and simply with examples. Make learning easy and engaging. Break down complex topics into simple terms."
    
    # Prepare messages for API
    messages = [{"role": "system", "content": system_prompt}] + conversation_history[user_id]
    
    # Show typing indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    # Get response from Perplexity
    response = await perplexity.ask(messages)
    
    # Add assistant response to history
    conversation_history[user_id].append({"role": "assistant", "content": response})
    
    # Send response
    await update.message.reply_text(response, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages"""
    await handle_message_with_role(update, context)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.message:
        await update.message.reply_text("Sorry, an error occurred. Please try again later.")

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("role", role_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(CommandHandler("ask", ask_command))
    application.add_handler(CommandHandler("teach", teach_command))
    application.add_handler(CommandHandler("explain", explain_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
