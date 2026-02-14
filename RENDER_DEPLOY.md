# 🚀 Render पर Deploy करने की Complete Guide

## Step 1: Render Account बनाएं

1. [Render.com](https://render.com) पर जाएं
2. **Sign Up** button पर click करें
3. GitHub account से sign in करें
4. Render को GitHub access दें

## Step 2: New Web Service Create करें

1. Render Dashboard में **"New +"** button पर click करें
2. **"Web Service"** select करें
3. अपनी **telegram-teacher-student-bot** repository select करें
4. Repository को connect करें

## Step 3: Service Configuration

### Basic Settings:
- **Name**: `telegram-teacher-student-bot` (या अपनी पसंद का नाम)
- **Region**: Singapore (India के सबसे करीब) या Frankfurt
- **Branch**: `main`
- **Runtime**: `Python 3`

### Build & Deploy Settings:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python bot.py`

### Instance Type:
- **Free** plan select करें (छोटे bots के लिए काफी है)

## Step 4: Environment Variables Add करें

Render dashboard में **Environment** section में जाएं और ये variables add करें:

### 1. TELEGRAM_TOKEN
```
Key: TELEGRAM_TOKEN
Value: आपका telegram bot token
```

**कैसे पाएं:**
- Telegram पर @BotFather को message करें
- `/newbot` command send करें
- Bot का name और username दें
- Token copy करें

### 2. PERPLEXITY_API_KEY
```
Key: PERPLEXITY_API_KEY
Value: आपकी perplexity API key
```

**कैसे पाएं:**
- [Perplexity AI Settings](https://www.perplexity.ai/settings/api) पर जाएं
- Sign in करें
- API section में जाएं
- **Generate New API Key** पर click करें
- Key copy करें

### 3. ADMIN_IDS
```
Key: ADMIN_IDS
Value: आपकी telegram user ID (comma-separated अगर multiple हैं)
```

**Example:** `123456789,987654321`

**कैसे पाएं:**
- Telegram पर @userinfobot को message करें
- Bot आपकी user ID भेजेगा

### 4. TEACHER_IDS
```
Key: TEACHER_IDS
Value: Teacher telegram user IDs (comma-separated)
```

**Example:** `123456789,555666777`

## Step 5: Deploy करें

1. सभी environment variables add करने के बाद
2. **"Create Web Service"** button पर click करें
3. Render automatically bot को deploy करेगा
4. Deploy process को logs में देख सकते हैं

## Step 6: Deployment Verify करें

### Logs Check करें:
1. Render dashboard में अपनी service पर click करें
2. **"Logs"** tab में जाएं
3. देखें कि bot successfully start हो रहा है:
   ```
   Bot started!
   ```

### Bot Test करें:
1. Telegram पर अपने bot को open करें
2. `/start` command send करें
3. Bot को respond करना चाहिए

## 🔄 Auto-Deploy Setup

Render automatically deploy करेगा जब भी आप GitHub repository में changes push करेंगे:

```bash
# Local changes करें
git add .
git commit -m "Update bot features"
git push origin main

# Render automatically detect करेगा और redeploy करेगा
```

## ⚙️ Important Settings

### Health Check (Optional):
- Path: `/`
- अगर bot सिर्फ Telegram polling use कर रहा है तो disable कर दें

### Auto-Deploy:
- **Enable** रखें GitHub changes के लिए automatic deployment के लिए

## 🐛 Troubleshooting

### Problem 1: Bot Start नहीं हो रहा
**Solution:**
- Logs check करें
- Environment variables सही हैं या नहीं verify करें
- TELEGRAM_TOKEN और PERPLEXITY_API_KEY valid हैं check करें

### Problem 2: "Module not found" Error
**Solution:**
- `requirements.txt` में सभी dependencies listed हैं check करें
- Build logs में errors देखें

### Problem 3: Bot Respond नहीं कर रहा
**Solution:**
- Render service running है check करें (logs में "Bot started!" दिखना चाहिए)
- Telegram token सही है verify करें
- @BotFather पर जाकर bot status check करें

### Problem 4: Perplexity API Error
**Solution:**
- API key valid है check करें
- [Perplexity Settings](https://www.perplexity.ai/settings/api) पर API usage/limits check करें
- Logs में exact error message देखें

## 📊 Monitor Your Bot

### Render Dashboard:
- **Metrics**: CPU, Memory usage देखें
- **Logs**: Real-time logs access करें
- **Events**: Deployment history देखें

### Free Tier Limits:
- 750 hours/month (24/7 running के लिए काफी है)
- Bot inactive होने पर sleep mode में जा सकता है
- First request पर 30-60 seconds में wake up होगा

## 🔒 Security Best Practices

1. **Never commit** `.env` file to GitHub
2. Always use Render's environment variables
3. Keep API keys private
4. Regularly rotate API keys
5. Monitor logs for unusual activity

## 💡 Pro Tips

1. **Custom Domain** (Paid plans):
   - Render पर custom domain add कर सकते हैं
   
2. **Persistent Storage** (If needed):
   - अगर database चाहिए तो Render PostgreSQL add करें
   
3. **Better Performance**:
   - Paid plan use करें sleep mode avoid करने के लिए
   - Closer region select करें (Singapore for India)

4. **Backup**:
   - GitHub repository automatically backup है
   - Important data के लिए external database use करें

## 🎯 Next Steps

1. Bot को test करें सभी commands के साथ
2. Custom features add करें
3. Users को bot link share करें
4. Feedback लें और improve करें

## 📞 Support

Problems होने पर:
1. Render logs carefully check करें
2. GitHub Issues में report करें
3. [Render Community](https://community.render.com/) में help मांगें

---

**Happy Deploying! 🚀**

**Bot Link Format:**
```
t.me/your_bot_username
```

Deployment successful होने के बाद अपने bot को users के साथ share करें! 🎉
