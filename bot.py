import os
import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start - показывает кнопку с веб-приложением"""
    
    web_app_url = os.environ.get('WEB_APP_URL')
    
    if not web_app_url:
        await update.message.reply_text(
            "⚠️ Бот настраивается, попробуйте через минуту..."
        )
        return
    
    keyboard = [
        [InlineKeyboardButton(
            "📚 Открыть библиотеку критериев", 
            web_app=WebAppInfo(url=web_app_url)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 *Добро пожаловать в DanceBrain!*\n\n"
        "📖 Библиотека критериев оценки танцев\n"
        "🏆 WDSF Standard Dance - Judging System 2.1\n\n"
        "Нажмите кнопку ниже, чтобы открыть библиотеку:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /help"""
    await update.message.reply_text(
        "📚 *DanceBrain - Библиотека критериев*\n\n"
        "*Команды:*\n"
        "/start - Открыть библиотеку\n"
        "/help - Показать эту справку\n\n"
        "*Возможности:*\n"
        "• 📝 Текстовые заметки\n"
        "• 🎥 Видео с транскрипциями\n"
        "• 🔗 Ссылки на материалы\n\n"
        "Все данные сохраняются в Telegram Cloud! ☁️",
        parse_mode='Markdown'
    )

def main():
    """Запуск бота"""
    TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN не установлен в переменных окружения!")
    
    logger.info("🤖 Запуск DanceBrain бота...")
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    logger.info("✅ Бот запущен и ожидает команды!")
    logger.info(f"👤 Бот: @{application.bot.username}")
    
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

if __name__ == '__main__':
    main()
```

4. Нажмите **"Commit changes..."** → **"Commit changes"**

---

## Шаг 2.3: Создание requirements.txt

1. **"Add file"** → **"Create new file"**
2. Имя: `requirements.txt`
3. Вставьте:
```
python-telegram-bot==20.7
