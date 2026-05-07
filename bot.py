import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Jurnalga doimiy yozib borish
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger(__name__).setLevel(logging.INFO)

# O'zingizning bot tokeningizni kiriting
BOT_TOKEN = "7771805386:AAHFLwyQLXQjNOpfTa5iBcEbG4ZwusNzQyM"
# Sizning Vercel / Netlify web ilova linki (HTTPS bo'lishi shart!)
WEB_APP_URL = "https://yoursite.vercel.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """`/start` bosilganda ishlaydigan rasm."""
    user = update.effective_user
    
    # Hunter System yoki Wallet kabi mini app'ni ochish uchun tugma
    keyboard = [
        [
            InlineKeyboardButton(
                "🗡️ Open Hunter System",
                web_app=WebAppInfo(url=WEB_APP_URL),
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Xush kelibsiz {user.first_name}!\n\n"
        f"Keling bugungi rejalaringizni tuzamiz. Quests oling va XP yig'ing!",
        reply_markup=reply_markup,
    )

def main() -> None:
    """Botni ishga tushirish."""
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi... (Ctrl+C yordamida to'xtatishingiz mumkin)")
    # Polling orqali yangi xabarlarni tinglash
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
