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

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
WEB_APP_URL = os.getenv("WEB_APP_URL", "https://YOUR_DEPLOYED_APP.vercel.app")

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
            "🎮 Hunter System Ochish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [
            InlineKeyboardButton("📊 Statistika", callback_data="stats"),
            InlineKeyboardButton("🏆 Ranking", callback_data="ranking")
        ],
        [
            InlineKeyboardButton("❓ Yordam", callback_data="help"),
            InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"""
🗡️ <b>HUNTER SYSTEM'ga xush kelibsiz!</b>

Salom, <b>{user.first_name}</b>! 👋

Bu bot sizning kunlik quest'laringiz va skill rivojlanishingizni Solo Leveling uslubida kuzatadi.

<b>Qanday ishlaydi:</b>
✓ Kunlik vazifalar qo'shing
✓ Focus time hisoblang
✓ XP yig'ing
✓ Rankingizni ko'taring
✓ Skill'laringizni o'zlashtiring

<b>Bugingi Statistika:</b>
├ Level: {(user_data['total_xp'] // 50) + 1}
├ XP: {user_data['total_xp']} 
├ Bugun XP: {user_data['daily_xp']}
└ Streak: {user_data['streak']} kunlik

<b>👉 "🎮 Hunter System Ochish" tugmasini bosing va boshlang!</b>
"""
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/help - Yordam"""
    help_text = """
🗡️ <b>HUNTER SYSTEM - YORDAM</b>

<b>Asosiy Tushunchalar:</b>

📌 <b>DAILY QUESTS</b>
→ Har kun yangi vazifalar qo'shish
→ Har bir vazifa = +10 XP
→ Timer bilan vaqt hisoblaymiz
→ Timer XP = vaqt / 40 daqiqa

📌 <b>ONGOING MISSIONS</b>
→ Uzoq muddatli maqsadlar (1-7 kun)
→ Deadline va progress (0-100%)
→ Tugallash = +25 XP

📌 <b>SKILL TRACKING</b>
→ Kodlaш, English, o'qish va h.k.
→ Har "TRAIN" = +5 XP
→ Growth trend ko'ring (↑ ↓ →)

📌 <b>RANKING SISTEMA</b>
🟪 E-Rank: 0-99 XP
🟦 D-Rank: 100-299 XP
🟧 C-Rank: 300-699 XP
🟨 B-Rank: 700-1499 XP
🔴 A-Rank: 1500-2999 XP
⭐ S-Rank: 3000-4999 XP
👑 National: 5000+ XP

<b>Kunlik Rutin:</b>
1️⃣ App'ni oching
2️⃣ 3-5 ta vazifani qo'shing
3️⃣ Timer bilan bajaramiz
4️⃣ Done qilib XP olamiz
5️⃣ Oqshomda skill training
6️⃣ Streakni kesmaymiz

<b>Maslahat:</b>
💡 Har kun bitta QUEST = 7 XP min
💡 Haftalik streak = motivatsiya
💡 Focus time distractions'dan kuzat
💡 Skills regulyar o'zlashitiring

🎮 <b>App'ni ochish uchun /start bosing</b>
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

<b>Current Rank:</b>
{rank_info['current']['emoji']} <b>{rank_info['current']['name']}</b>

<b>XP Progress:</b>
{bar} {int(pct)}%
{rank_info['progress']} / {rank_info['needed']} XP

<b>Level & XP:</b>
├ Level: <code>{level}</code>
├ Total XP: <code>{user_data['total_xp']}</code>
├ Today XP: <code>{user_data['daily_xp']}</code>
└ Streak: <code>{user_data['streak']} days</code>

<b>Achievements:</b>
├ Quests Done: {user_data['completed_quests']}
├ Total Focus: {user_data['stats']['total_focus_time'] // 3600}h {(user_data['stats']['total_focus_time'] % 3600) // 60}m
└ Avg Daily XP: {user_data['stats']['avg_daily_xp']}

<b>Next Rank:</b>
{rank_info['next']['emoji']} {rank_info['next']['name']} 
({rank_info['needed']} XP kerak)
"""
    
    keyboard = [[InlineKeyboardButton("← Orqaga", callback_data="back_menu")]]
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
    
    ranking_text = "<b>🏆 RANKING SISTEMA</b>\n\n"
    
    for i, rank in enumerate(RANKS):
        is_current = rank == current_rank
        marker = "→ " if is_current else "  "
        next_xp = RANKS[i + 1]["min_xp"] if i + 1 < len(RANKS) else "∞"
        
        ranking_text += f"{marker}{rank['emoji']} <b>{rank['name']}</b>\n"
        ranking_text += f"   {rank['min_xp']} - {next_xp} XP\n\n"
    
    ranking_text += "\n<b>Maqsad:</b>\n"
    ranking_text += "E-Rank: 1 hafta\n"
    ranking_text += "D-Rank: 2 hafta\n"
    ranking_text += "C-Rank: 3-4 hafta\n"
    ranking_text += "B-Rank: 1-2 oy\n"
    ranking_text += "S-Rank: 2-3 oy\n"
    ranking_text += "National: 3-6 oy\n"
    
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

<b>1. DAILY QUESTS</b>
App'da "Daily Quests" tabiga o'ting:
• Yangi vazifa yozing
• ⏱️ Timer bosing (ishga tushadi)
• Vazifani bajarasiz
• ✓ Checkbox bosing (Done)
→ Har quest = +10 XP + timer XP

<b>2. ONGOING MISSIONS</b>
"Ongoing" tabiga o'ting:
• Mission nomi yozing
• Deadline belgilang
• Kategoriya tanlang
• Har kun progress yangilang
→ Tugallash = +25 XP

<b>3. SKILLS</b>
"Analysis" → "Skill Growth":
• Skill nomini yozing
• Har kun "TRAIN" bosing
→ Har TRAIN = +5 XP
→ Growth trend ko'ring

<b>4. FOCUS ANALYSIS</b>
"Analysis" → "Focus Drains":
• Instagram, TikTok va h.k.
• +15m bosib vaqt qo'shing
→ Chalg'ituvchilarni kuzating

<b>XP Hisob:</b>
✓ Daily quest = +10 XP
✓ Focus time = +1 XP (40 min)
✓ Ongoing done = +25 XP
✓ Skill train = +5 XP
✓ Distraction log = -motivatsiya

👉 Batafsil: /help
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

<b>User Info:</b>
ID: <code>{user_id}</code>
Name: {query.from_user.first_name}
Joined: {user_data['last_reset']}

<b>Notification Settings:</b>
🔔 Reminders: <code>OFF</code> (Free bot)
📊 Daily Report: <code>OFF</code> (Free bot)
⏰ Streak Alert: <code>OFF</code> (Free bot)

<b>Data:</b>
💾 Backup: <code>Avtomatik</code>
📁 Storage: <code>Local JSON</code>
🔒 Privacy: <code>100% Private</code>

<b>Malumot:</b>
• Barcha ma'lumotlar local JSON faylda
• Telefon o'chirilsa ham saqlandi
• Cloud'ga yuklash istagan bo'lsa - /cloudbackup
• Reset qilmoqchi? - /reset

<b>Version:</b> v1.0.0 (Free)
<b>Support:</b> @yourbot
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
            "🎮 Hunter System Ochish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [
            InlineKeyboardButton("📊 Statistika", callback_data="stats"),
            InlineKeyboardButton("🏆 Ranking", callback_data="ranking")
        ],
        [
            InlineKeyboardButton("❓ Yordam", callback_data="help"),
            InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")
        ]
    ]
    
    menu_text = """
🗡️ <b>MAIN MENU</b>

🎮 Hunter System ochish uchun birinchi tugmani bosing
📊 Sizning statistikangizni ko'rish uchun tugmalarni ishlating
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
⚡ <b>QUICK STATUS</b>

{rank['emoji']} <b>{rank['name']}</b>
Level {level} | {user_data['total_xp']} XP
Today: +{user_data['daily_xp']} XP
Streak: {user_data['streak']} 🔥

👉 /start bosib app'ni oching
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
        "⚠️ <b>EHTIYOT!</b>\n\n"
        "Barcha ma'lumotlaringizni o'chirishni xohlaysizmi?\n"
        "Bu amalni qaytarib bo'lmaydi! ❌",
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
    await query.edit_message_text("✅ <b>Barcha ma'lumotlar o'chirildi</b>\n\n/start bosing boshlash uchun")

async def cancel_reset_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reset bekor qilish"""
    query = update.callback_query
    await query.answer("Reset bekor qilindi")
    await query.edit_message_text("❌ Reset bekor qilindi\n\n/start bosing davom etish uchun")

# ============================================================================
# ERROR HANDLER
# ============================================================================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Xatolar uchun handler"""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Xato yuz berdi!\n\n"
                "Iltimos /start bosing yoki biroz vaqt o'tib qayta urinib ko'ring"
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
    
    # Bot commands (menu ko'rinish)
    commands = [
        BotCommand("start", "🎮 Hunter System ni ochish"),
        BotCommand("status", "⚡ Qisqa status"),
        BotCommand("help", "❓ Yordam va qo'llanma"),
        BotCommand("reset", "⚠️ Barcha ma'lumotlarni o'chirish"),
    ]
    
    # Run
    logger.info("🗡️ Hunter System Bot ishga tushdi!")
    logger.info(f"Web App URL: {WEB_APP_URL}")
    logger.info(f"Data file: {DATA_FILE}")
    
    # Polling ishga tushar
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
