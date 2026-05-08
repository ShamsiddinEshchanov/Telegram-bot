#!/usr/bin/env python3
"""
🗡️ HUNTER SYSTEM BOT
Solo Leveling uslubidagi Telegram Web App Bot
Pullik rejimi yoq - FAQAT FREE

Telegram: @BotFather'dan token oling
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Optional
import os

from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup, 
    WebAppInfo, BotCommand
)
from telegram.ext import (
    Application, CommandHandler, ContextTypes, 
    MessageHandler, filters, CallbackQueryHandler
)
from telegram.constants import ParseMode

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================================================
# KONFIGURATSIYA
# ============================================================================

BOT_TOKEN = os.getenv("7771805386:AAHFLwyQLXQjNOpfTa5iBcEbG4ZwusNzQyM", "YOUR_BOT_TOKEN_HERE")
WEB_APP_URL = os.getenv("https://telegram-bot-seven-cyan-94.vercel.app/", "https://YOUR_DEPLOYED_APP.vercel.app")

# E-agar local'da test qilmoqchi bo'lsangiz:
# WEB_APP_URL = "http://localhost:8000/index.html"  # Local
# WEB_APP_URL = "https://yourdomain.com/index.html"  # Production

RANKS = [
    {"name": "E-Rank", "emoji": "🟪", "min_xp": 0, "next_xp": 100},
    {"name": "D-Rank", "emoji": "🟦", "min_xp": 100, "next_xp": 300},
    {"name": "C-Rank", "emoji": "🟧", "min_xp": 300, "next_xp": 700},
    {"name": "B-Rank", "emoji": "🟨", "min_xp": 700, "next_xp": 1500},
    {"name": "A-Rank", "emoji": "🔴", "min_xp": 1500, "next_xp": 3000},
    {"name": "S-Rank", "emoji": "⭐", "min_xp": 3000, "next_xp": 5000},
    {"name": "National", "emoji": "👑", "min_xp": 5000, "next_xp": float('inf')},
]

# ============================================================================
# USER DATA (JSON FILE'DA SAQLASH)
# ============================================================================

DATA_FILE = "user_data.json"

def load_user_data(user_id: int) -> dict:
    """User ma'lumotlarini JSON'dan yuklash"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                all_data = json.load(f)
                if str(user_id) in all_data:
                    return all_data[str(user_id)]
    except Exception as e:
        logger.error(f"Error loading data: {e}")
    
    # Default user data
    return {
        "user_id": user_id,
        "total_xp": 0,
        "daily_xp": 0,
        "last_reset": datetime.now().strftime("%Y-%m-%d"),
        "streak": 0,
        "completed_quests": 0,
        "stats": {
            "total_quests": 0,
            "total_focus_time": 0,  # sekundda
            "avg_daily_xp": 0,
        }
    }

def save_user_data(user_id: int, data: dict):
    """User ma'lumotlarini JSON'ga saqlash"""
    try:
        all_data = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                all_data = json.load(f)
        
        all_data[str(user_id)] = data
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def get_user_rank(xp: int) -> dict:
    """XP'ga qarab rank qaytar"""
    for i in range(len(RANKS) - 1, -1, -1):
        if xp >= RANKS[i]["min_xp"]:
            current = RANKS[i]
            next_rank = RANKS[i + 1] if i + 1 < len(RANKS) else None
            return {
                "current": current,
                "next": next_rank,
                "progress": xp - current["min_xp"],
                "needed": (next_rank["min_xp"] - current["min_xp"]) if next_rank else 0
            }
    return {"current": RANKS[0], "next": RANKS[1], "progress": 0, "needed": 100}

# ============================================================================
# MAIN COMMANDS
# ============================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start - Bot ishga tushar
    Main menu ko'rsatadi
    """
    user = update.effective_user
    user_id = user.id
    user_data = load_user_data(user_id)
    
    # Daily reset check
    today = datetime.now().strftime("%Y-%m-%d")
    if user_data.get("last_reset") != today:
        user_data["daily_xp"] = 0
        user_data["last_reset"] = today
        save_user_data(user_id, user_data)
    
    # Keyboard
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Hunter Tizimini Ochish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [
            InlineKeyboardButton("📊 Statistika", callback_data="stats"),
            InlineKeyboardButton("🏆 Reyting", callback_data="ranking")
        ],
        [
            InlineKeyboardButton("❓ Yordam", callback_data="help"),
            InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"""
🗡️ <b>HUNTER TIZIMIGA XO'SH KELIBSIZ!</b>

Assalomu alaykum, <b>{user.first_name}</b>! 👋

Bu bot sizning kunlik vazifalaringiz va ko'nikmalaringiz rivojlanishini Solo Leveling uslubida kuzatadi.

<b>Qanday ishlaydi:</b>
✓ Kunlik vazifalar qo'shing
✓ Diqqat vaqtini hisoblang
✓ XP yig'ing
✓ Reytingingizni ko'taring
✓ Ko'nikmalaringizni o'zlashtiring

<b>Bugungi Statistika:</b>
├ Daraja: {(user_data['total_xp'] // 50) + 1}
├ XP: {user_data['total_xp']} 
├ Bugun XP: {user_data['daily_xp']}
└ Seriya: {user_data['streak']} kunlik

<b>👉 "🎮 Hunter Tizimini Ochish" tugmasini bosing va boshlang!</b>
"""
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/help - Yordam"""
    help_text = """
🗡️ <b>HUNTER TIZIMI - YORDAM</b>

<b>Asosiy Tushunchalar:</b>

📌 <b>KUNLIK VAZIFALAR</b>
→ Har kun yangi vazifalar qo'shing
→ Har bir vazifa = +10 XP
→ Taymer bilan vaqt hisoblang
→ Taymer XP = vaqt / 40 daqiqa

📌 <b>DAVOM ETAYOTGAN MISSIYALAR</b>
→ Uzoq muddatli maqsadlar (1-7 kun)
→ Muddat va jarayon (0-100%)
→ Tugallash = +25 XP

📌 <b>KO'NIKMA KUZATUVI</b>
→ Dasturlash, Inglizcha, o'qish va h.k.
→ Har "MASHQ" = +5 XP
→ O'sish tendensiyasini ko'ring (↑ ↓ →)

📌 <b>REYTING TIZIMI</b>
🟪 E-Daraja: 0-99 XP
🟦 D-Daraja: 100-299 XP
🟧 C-Daraja: 300-699 XP
🟨 B-Daraja: 700-1499 XP
🔴 A-Daraja: 1500-2999 XP
⭐ S-Daraja: 3000-4999 XP
👑 Milliy: 5000+ XP

<b>Kunlik Tartib:</b>
1️⃣ Ilovani oching
2️⃣ 3-5 ta vazifa qo'shing
3️⃣ Taymer bilan bajaring
4️⃣ Bajarildi deb belgilab XP oling
5️⃣ Kechqurun ko'nikma mashqi
6️⃣ Seriyani uzmaymiz

<b>Maslahat:</b>
💡 Har kun bitta VAZIFA = kamida 7 XP
💡 Haftalik seriya = motivatsiya
💡 Chalg'ituvchilarni kuzating
💡 Ko'nikmalarni muntazam o'zlashtiring

🎮 <b>Ilovani ochish uchun /start bosing</b>
"""
    
    await update.message.reply_text(
        help_text,
        parse_mode=ParseMode.HTML
    )

async def stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback: /stats button"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    user_data = load_user_data(user_id)
    
    # Bugun reset check
    today = datetime.now().strftime("%Y-%m-%d")
    if user_data.get("last_reset") != today:
        user_data["daily_xp"] = 0
        user_data["last_reset"] = today
        save_user_data(user_id, user_data)
    
    rank_info = get_user_rank(user_data["total_xp"])
    level = (user_data["total_xp"] // 50) + 1
    
    # Progress bar
    pct = (rank_info["progress"] / rank_info["needed"] * 100) if rank_info["needed"] > 0 else 100
    bar = "█" * int(pct // 10) + "░" * (10 - int(pct // 10))
    
    stats_text = f"""
📊 <b>STATISTIKA - {query.from_user.first_name}</b>

<b>Joriy Daraja:</b>
{rank_info['current']['emoji']} <b>{rank_info['current']['name']}</b>

<b>XP Jarayoni:</b>
{bar} {int(pct)}%
{rank_info['progress']} / {rank_info['needed']} XP

<b>Daraja va XP:</b>
├ Daraja: <code>{level}</code>
├ Jami XP: <code>{user_data['total_xp']}</code>
├ Bugun XP: <code>{user_data['daily_xp']}</code>
└ Seriya: <code>{user_data['streak']} kun</code>

<b>Yutuqlar:</b>
├ Bajarilgan Vazifalar: {user_data['completed_quests']}
├ Jami Diqqat Vaqti: {user_data['stats']['total_focus_time'] // 3600}s {(user_data['stats']['total_focus_time'] % 3600) // 60}d
└ O'rtacha Kunlik XP: {user_data['stats']['avg_daily_xp']}

<b>Keyingi Daraja:</b>
{rank_info['next']['emoji']} {rank_info['next']['name']} 
({rank_info['needed']} XP kerak)
"""
    
    keyboard = [[InlineKeyboardButton("← Orqaga qaytish", callback_data="back_menu")]]
    await query.edit_message_text(
        stats_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def ranking_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback: /ranking button"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    user_data = load_user_data(user_id)
    current_rank = get_user_rank(user_data["total_xp"])["current"]
    
    ranking_text = "<b>🏆 REYTING TIZIMI</b>\n\n"
    
    for i, rank in enumerate(RANKS):
        is_current = rank == current_rank
        marker = "→ " if is_current else "  "
        next_xp = RANKS[i + 1]["min_xp"] if i + 1 < len(RANKS) else "∞"
        
        ranking_text += f"{marker}{rank['emoji']} <b>{rank['name']}</b>\n"
        ranking_text += f"   {rank['min_xp']} - {next_xp} XP\n\n"
    
    ranking_text += "\n<b>Taxminiy Maqsad:</b>\n"
    ranking_text += "E-Daraja: 1 hafta\n"
    ranking_text += "D-Daraja: 2 hafta\n"
    ranking_text += "C-Daraja: 3-4 hafta\n"
    ranking_text += "B-Daraja: 1-2 oy\n"
    ranking_text += "S-Daraja: 2-3 oy\n"
    ranking_text += "Milliy: 3-6 oy\n"
    
    keyboard = [[InlineKeyboardButton("← Orqaga", callback_data="back_menu")]]
    await query.edit_message_text(
        ranking_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback: /help button"""
    query = update.callback_query
    await query.answer()
    
    help_text = """
<b>❓ QANDAY ISHLAYDI</b>

<b>1. KUNLIK VAZIFALAR</b>
Ilovada "Kunlik Vazifalar" yorlig'iga o'ting:
• Yangi vazifa yozing
• ⏱️ Taymerni bosing (ishga tushadi)
• Vazifani bajaring
• ✓ Belgi bosing (Bajarildi)
→ Har vazifa = +10 XP + taymer XP

<b>2. DAVOM ETAYOTGAN MISSIYALAR</b>
"Missiyalar" yorlig'iga o'ting:
• Missiya nomini yozing
• Muddatini belgilang
• Toifasini tanlang
• Har kun jarayonni yangilang
→ Tugallash = +25 XP

<b>3. KO'NIKMALAR</b>
"Tahlil" → "Ko'nikma O'sishi":
• Ko'nikma nomini yozing
• Har kun "MASHQ" bosing
→ Har MASHQ = +5 XP
→ O'sish tendensiyasini ko'ring

<b>4. DIQQAT TAHLILI</b>
"Tahlil" → "Chalg'ituvchilar":
• Instagram, TikTok va h.k.
• +15 daqiqa bosib vaqt qo'shing
→ Chalg'ituvchilarni kuzating

<b>XP Hisob-kitobi:</b>
✓ Kunlik vazifa = +10 XP
✓ Diqqat vaqti = +1 XP (40 daq)
✓ Missiya tugallash = +25 XP
✓ Ko'nikma mashqi = +5 XP
✓ Chalg'ituvchi = -motivatsiya

👉 Batafsil: /yordam
"""
    
    keyboard = [[InlineKeyboardButton("← Orqaga", callback_data="back_menu")]]
    await query.edit_message_text(
        help_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def settings_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback: /settings button"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    user_data = load_user_data(user_id)
    
    settings_text = f"""
⚙️ <b>SOZLAMALAR</b>

<b>Foydalanuvchi Ma'lumoti:</b>
ID: <code>{user_id}</code>
Ism: {query.from_user.first_name}
Qo'shilgan: {user_data['last_reset']}

<b>Bildirishnoma Sozlamalari:</b>
🔔 Eslatmalar: <code>O'CHI</code> (Bepul bot)
📊 Kunlik Hisobot: <code>O'CHI</code> (Bepul bot)
⏰ Seriya Ogohlantirish: <code>O'CHI</code> (Bepul bot)

<b>Ma'lumotlar:</b>
💾 Zaxira: <code>Avtomatik</code>
📁 Saqlash: <code>Mahalliy JSON</code>
🔒 Maxfiylik: <code>100% Shaxsiy</code>

<b>Eslatma:</b>
• Barcha ma'lumotlar mahalliy JSON faylda saqlanadi
• Telefon o'chirilsa ham saqlanadi
• Bulutga yuklash uchun - /cloudbackup
• Tozalash uchun? - /reset

<b>Versiya:</b> v1.0.0 (Bepul)
<b>Yordam:</b> @yourbot
"""
    
    keyboard = [[InlineKeyboardButton("← Orqaga", callback_data="back_menu")]]
    await query.edit_message_text(
        settings_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def back_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Orqaga qaytish"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Hunter Tizimini Ochish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [
            InlineKeyboardButton("📊 Statistika", callback_data="stats"),
            InlineKeyboardButton("🏆 Reyting", callback_data="ranking")
        ],
        [
            InlineKeyboardButton("❓ Yordam", callback_data="help"),
            InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")
        ]
    ]
    
    menu_text = """
🗡️ <b>ASOSIY MENYU</b>

🎮 Hunter Tizimini ochish uchun birinchi tugmani bosing
📊 Statistikangizni ko'rish uchun tugmalardan foydalaning
"""
    
    await query.edit_message_text(
        menu_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/status - Qisqa statistic"""
    user_id = update.effective_user.id
    user_data = load_user_data(user_id)
    
    today = datetime.now().strftime("%Y-%m-%d")
    if user_data.get("last_reset") != today:
        user_data["daily_xp"] = 0
        user_data["last_reset"] = today
        save_user_data(user_id, user_data)
    
    rank = get_user_rank(user_data["total_xp"])["current"]
    level = (user_data["total_xp"] // 50) + 1
    
    status = f"""
⚡ <b>TEZKOR HOLAT</b>

{rank['emoji']} <b>{rank['name']}</b>
Daraja {level} | {user_data['total_xp']} XP
Bugun: +{user_data['daily_xp']} XP
Seriya: {user_data['streak']} 🔥

👉 /start bosib ilovani oching
"""
    
    await update.message.reply_text(status, parse_mode=ParseMode.HTML)

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/reset - Barcha ma'lumotlarni o'chirish (EHTIYOT!)"""
    user_id = update.effective_user.id
    
    keyboard = [
        [
            InlineKeyboardButton("✅ Ha, o'chir", callback_data="confirm_reset"),
            InlineKeyboardButton("❌ Yo'q, orqaga", callback_data="cancel_reset")
        ]
    ]
    
    await update.message.reply_text(
        "⚠️ <b>DIQQAT!</b>\n\n"
        "Barcha ma'lumotlaringizni o'chirishni xohlaysizmi?\n"
        "Bu amalni ortga qaytarib bo'lmaydi! ❌",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

async def confirm_reset_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reset tasdiqlash"""
    query = update.callback_query
    user_id = query.from_user.id
    
    user_data = load_user_data(user_id)
    user_data = {
        "user_id": user_id,
        "total_xp": 0,
        "daily_xp": 0,
        "last_reset": datetime.now().strftime("%Y-%m-%d"),
        "streak": 0,
        "completed_quests": 0,
        "stats": {
            "total_quests": 0,
            "total_focus_time": 0,
            "avg_daily_xp": 0,
        }
    }
    save_user_data(user_id, user_data)
    
    await query.answer("Ma'lumotlar o'chirildi!")
    await query.edit_message_text("✅ <b>Barcha ma'lumotlar o'chirildi</b>\n\nBoshlash uchun /start bosing")

async def cancel_reset_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reset bekor qilish"""
    query = update.callback_query
    await query.answer("Bekor qilindi")
    await query.edit_message_text("❌ Tozalash bekor qilindi\n\nDavom etish uchun /start bosing")

# ============================================================================
# ERROR HANDLER
# ============================================================================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Xatolar uchun handler"""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Xatolik yuz berdi!\n\n"
                "Iltimos /start bosing yoki biroz vaqt o'tib qayta urinib ko'ring."
            )
        except Exception as e:
            logger.error(f"Failed to send error message: {e}")

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main() -> None:
    """Bot ishga tushirish"""
    
    # Application yaratish
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("reset", reset_command))
    
    # Callback handlers
    application.add_handler(CallbackQueryHandler(stats_callback, pattern="^stats$"))
    application.add_handler(CallbackQueryHandler(ranking_callback, pattern="^ranking$"))
    application.add_handler(CallbackQueryHandler(help_callback, pattern="^help$"))
    application.add_handler(CallbackQueryHandler(settings_callback, pattern="^settings$"))
    application.add_handler(CallbackQueryHandler(back_menu_callback, pattern="^back_menu$"))
    application.add_handler(CallbackQueryHandler(confirm_reset_callback, pattern="^confirm_reset$"))
    application.add_handler(CallbackQueryHandler(cancel_reset_callback, pattern="^cancel_reset$"))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Bot commands (menyu ko'rinishi)
    commands = [
        BotCommand("start", "🎮 Hunter Tizimini ochish"),
        BotCommand("status", "⚡ Tezkor holat"),
        BotCommand("help", "❓ Yordam va qo'llanma"),
        BotCommand("reset", "⚠️ Barcha ma'lumotlarni o'chirish"),
    ]
    
    # Ishga tushirish
    logger.info("🗡️ Hunter Tizimi Boti ishga tushdi!")
    logger.info(f"Veb-ilova URL: {WEB_APP_URL}")
    logger.info(f"Ma'lumotlar fayli: {DATA_FILE}")
    
    # Polling ishga tushar
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
