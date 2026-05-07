# 🗡️ HUNTER SYSTEM BOT - O'RNATISH VA ISHGA TUSHIRISH

## 📋 Talablar

- **Python 3.10+** (download: https://www.python.org/downloads/)
- **Telegram Account**
- **Telegram Bot Token** (@BotFather'dan)
- **Internet ulanishi**

---

## 🚀 TEZKOR START (5 MINUT)

### 1. BotFather'dan Token Olish

```
1. Telegram'da @BotFather'ni qidiring
2. /start bosing
3. /newbot bosing
4. Bot nomini yozing (masalan: MyHunterBot)
5. Bot username yozing (masalan: my_hunter_bot_123)
6. TOKEN olabotsiz (masalan: 123456:ABC-DEF1234567890)
7. TOKEN'ni xotiraza oling (SIRLI!)
```

### 2. Fayllarni Tayyorlash

```bash
# 1. Yangi folder yaratish
mkdir hunter-system-bot
cd hunter-system-bot

# 2. Fayllarni yuklab olish
# bot.py
# requirements.txt
# (bu file'lar yuqorida berilgan)

# 3. Python kutubxonalarini o'rnatish
pip install -r requirements.txt
```

### 3. TOKEN'ni Bot'ga Qo'shish

**Variant A: Environment Variable (Tavsiya)**

```bash
# Windows (PowerShell)
$env:BOT_TOKEN = "YOUR_TOKEN_HERE"
python bot.py

# Linux/Mac (Terminal)
export BOT_TOKEN="YOUR_TOKEN_HERE"
python bot.py
```

**Variant B: bot.py'ga to'g'ri yozing**

`bot.py` faylini oching:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```
O'rniga haqiqiy token qo'ying:
```python
BOT_TOKEN = "123456:ABC-DEF1234567890"
```

### 4. Web App URL'ni Qo'shish

Bot quyidagi URL'larni qo'llab-quvvatlaydi:

**Variant A: Local Testing (Kompyuteringizda)**
```python
WEB_APP_URL = "http://localhost:8000/index.html"
```
Python server ishga tushirish:
```bash
cd folder_with_index.html
python -m http.server 8000
```
Keyin bot qaytan ishga tushing (boshqa terminalda)

**Variant B: Vercel'da (Tavsiya)**
```
1. https://vercel.com'ga o'ting
2. GitHub account bilan signup
3. index.html'ni GitHub'ga yuklab oling
4. Vercel'da "Import" bosing
5. Deploy link olabotsiz
6. bot.py'da o'rnatish:
```
```python
WEB_APP_URL = "https://your-app.vercel.app"
```

**Variant C: Netlify'da**
```
1. https://netlify.com'ga o'ting
2. index.html'ni drag-and-drop qiling
3. Deploy link olabotsiz
4. bot.py'da:
```
```python
WEB_APP_URL = "https://your-app.netlify.app"
```

### 5. Bot'ni Ishga Tushirish

```bash
python bot.py
```

**Agar muvaffaqiyatli bo'lsa:**
```
🗡️ Hunter System Bot ishga tushdi!
Web App URL: https://...
Data file: user_data.json
```

### 6. Telegram'da Test Qilish

```
1. Telegram'da bot username'ni qidiring
2. /start bosing
3. "🎮 Hunter System Ochish" tugmasini bosing
4. Web app ochilishi kerak
5. Vazifa qo'shib test qiling
```

---

## 📁 FAYL TUZILISHI

```
hunter-system-bot/
├── bot.py                 ← Bot kodi
├── requirements.txt       ← Python kutubxonalari
├── user_data.json        ← USER DATA (avtomatik yaratiladi)
├── index.html            ← Web App (alohida folder'da)
└── SETUP.md              ← Bu fayl
```

---

## 🔧 ADVANCED O'RNATISH

### Virtual Environment (Tavsiya)

```bash
# 1. Virtual env yaratish
python -m venv venv

# 2. Activate qilish
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Kutubxonalar o'rnatish
pip install -r requirements.txt

# 4. Bot ishga tushirish
python bot.py

# 5. Deactivate qilish (tugallasa)
deactivate
```

### Production'da (Linux Server)

```bash
# 1. SSH bilan serverga ulanish
ssh user@server_ip

# 2. Repository'ni clone qiling
git clone https://github.com/your-username/hunter-system-bot.git
cd hunter-system-bot

# 3. Virtual env + o'rnatish
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Environment variable qo'shing
export BOT_TOKEN="YOUR_TOKEN"
export WEB_APP_URL="https://your-app.vercel.app"

# 5. Background'da ishga tushirish (nohup)
nohup python3 bot.py > bot.log 2>&1 &

# 6. Logs ko'rish
tail -f bot.log
```

### Docker'da (Advanced)

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

CMD ["python", "bot.py"]
```

```bash
# Build va run qilish
docker build -t hunter-system-bot .
docker run -e BOT_TOKEN="YOUR_TOKEN" -e WEB_APP_URL="https://..." hunter-system-bot
```

---

## 🐛 XATOLAR VA YECHIMLAR

### "ModuleNotFoundError: No module named 'telegram'"

**Yechim:**
```bash
pip install python-telegram-bot
# yoki
pip install -r requirements.txt
```

### "Invalid token"

**Yechim:**
```
1. @BotFather'da /mybots bosing
2. Bot'ni tanlang
3. Token gavon bo'lishini tekshiring (yangi token oling)
4. BOT_TOKEN o'rnatish to'g'ri ekanligini tekshiring
```

### "Web App URL not accessible"

**Yechim:**
```
1. URL'ni brauzerda test qiling (https:// bo'lishi kerak)
2. index.html'ni host qiling (localhost emas)
3. CORS masalasi bo'lsa: https:// dan https://ni foydalaning
```

### "user_data.json permission denied"

**Yechim:**
```bash
# Linux/Mac:
chmod 644 user_data.json

# Yoki folder permissions:
chmod 755 .
```

### Bot "polling" qo'zg'almasdan to'xtaydi

**Yechim:**
```
1. Internet ulanishini tekshiring
2. TOKEN gavon bo'lshini tekshiring
3. Firewall masalasi bo'lsa port 443'ni oching
4. Log'ni ko'ring (bot.log)
```

---

## 📊 MAONIYLASH

Bot quyidagi ma'lumotlarni saqlaydi (JSON):

```json
{
  "123456789": {
    "user_id": 123456789,
    "total_xp": 250,
    "daily_xp": 50,
    "last_reset": "2026-05-07",
    "streak": 5,
    "completed_quests": 15,
    "stats": {
      "total_quests": 20,
      "total_focus_time": 3600,
      "avg_daily_xp": 45
    }
  }
}
```

**Security:**
- ✅ Serverda hech qanday password saqlanmaydi
- ✅ Barcha ma'lumotlar local JSON faylda (private)
- ✅ TOKEN hech qayerda log'ga yozilmaydi
- ✅ User data o'z ID bilan shifrlangan

---

## 🔄 YANGILASH VA UDELUPGRADE

### Code Yangilash

```bash
git pull origin main
pip install --upgrade -r requirements.txt
python bot.py
```

### Backup Ma'lumotlari

```bash
# user_data.json'ni backup qilish
cp user_data.json user_data.json.backup.$(date +%Y%m%d)

# Yoki Cloud'ga:
# - Google Drive'ga upload
# - Dropbox'ga upload
# - GitHub'ga commit
```

---

## 💬 SUPPORT

Bot'da xatolik yoki savollar bo'lsa:

```
1. Log'ni o'qing: python bot.py (terminal output)
2. Xato kodi bo'lsa Google'da qidiring
3. Bot source code'ni tekshiring
4. @BotFather'da /help bosing
```

---

## ✅ CHECKLSIT: Bot Tayyor ekanligini Tekshirish

- [ ] Python 3.10+ o'rnatilgan
- [ ] requirements.txt o'rnatilgan
- [ ] BOT_TOKEN qo'shilgan
- [ ] WEB_APP_URL qo'shilgan
- [ ] index.html hosted (vercel/netlify)
- [ ] `python bot.py` ishga tushar
- [ ] Telegram'da bot qidiring va /start bosing
- [ ] "🎮 Hunter System" tugmasi paydo bo'ladi
- [ ] Web app ochiladi va ishlaydi
- [ ] Vazifa qo'shib test qiling
- [ ] user_data.json yaratiladi

---

## 🎉 MUVAFFAQ!

Bot tayyor! Endi:
```
/start → /help → /status ko'ring
```

Happy hunting! 🗡️⚔️
