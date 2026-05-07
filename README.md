# 🗡️ Hunter System - Kunlik Quest Tracker

**Solo Leveling uslubidagi progresiya sistemi** - O'z maqsadlaringizni qanday ketayotganini real vaqtda ko'ring, XP yig'ing, rankingizni ko'taring.

---

## 📋 Mundarija
1. [O'ziga Umumiy Nazari](#oziga-umumiy-nazari)
2. [Asosiy Xususiyatlar](#asosiy-xususiyatlar)
3. [Qanday Ishlaydi](#qanday-ishlaydi)
4. [Texnik Tavsif](#texnik-tavsif)
5. [O'rnatish va Ishga Tushirish](#ornatish-va-ishga-tushirish)
6. [Foydalanish Bo'limi](#foydalanish-bolimi)
7. [Fayl Tuzilishi](#fayl-tuzilishi)
8. [Xatolar va Yechimlar](#xatolar-va-yechimlar)

---

## 📖 O'ziga Umumiy Nazari

**Hunter System** - sizning kunlik o'sishingizni Solo Leveling (anime/manga) uslubida ko'rsatuvchi veb-ilova.

**Asosiy fikr:**
- Her bir vazifa = **XP olish**
- XP to'plang = **Level ko'taring**
- Kunlik quest'lar + Focus time = **Streak yaratish**
- Progres ko'ring = **Motivatsiya ortadi**

Xuddi o'yinda level ko'tarilgani kabi, real hayotda ham o'z ko'nikmalaringizni kuchaytira olasiz! 💪

---

## ⚡ Asosiy Xususiyatlar

### 1️⃣ **Daily Quests** (Kunlik vazifalar)
- Har kun yangi vazifalar qo'shing
- Har bir vazifa = **+10 XP**
- ⏱️ **Timer** - vazifani bajarayotganda vaqt hisobi
- **Timer tugmasi** - "Play" bosing, timer ishga tushar. "Stop" bosing - vaqt saqlandi

**Misal:**
```
✓ Davs 30 daqiqa kod yozish → +10 XP + timer vaqti bo'yicha qo'shimcha XP
✓ 2 soat ingliz til o'qish → +10 XP + timer XP
```

### 2️⃣ **Ongoing Missions** (Uzoq muddatli missiyalar)
- 1-7 kunlik yoki oylik maqsadlar
- **Deadline** belgilang
- **Progress bar** (0-100%) - qancha qilganingiz ko'rinadi
- **Kategoriya** - Learning, Health, Project, Career, Personal

**Misal:**
```
📌 Fitnes plan - 15 kun
   Deadline: 2026-05-21
   Progress: 40% (6 kunni to'ldirdi)
   Status: 9 kun qoldi
```

### 3️⃣ **Progress Tab** (Progresiyani ko'rish)
- **Haftalik jadvali** - So'ngi 7 kunning XP ko'rsatkalari
- Rang kod:
  - 🟢 **Yashil** = 10+ XP (zo'r kun!)
  - 🟡 **Sariq** = 5-9 XP (o'rtacha)
  - 🔴 **Qizil** = 0-4 XP (past)

- **Activity Log** - oxirgi 20 ta narsaning tarixçasi
  - Nima qildingiz
  - Soati
  - Qancha XP oldingiz

### 4️⃣ **Analysis Tab** (Tahlil)
- **Focus Drains** (Chalg'ituvchilar)
  - Instagram, TikTok, YouTube, Discord vb.
  - "+15m" tugmasini bosib vaqt qo'shing
  - Grafik ko'rsatadi - qaysi narsada ko'p vaqt ketayaptimi

- **Skill Growth** (Ko'nikma rivojlanishi)
  - Coding, English, Drawing, Piano vb.
  - "TRAIN" tugmasini bosing = +5 XP bu ko'nikma uchun
  - Grafik ko'rsatadi - o'sib borayaptimi, pasayapmi

---

## 🎮 Qanday Ishlaydi

### Bosqa Butun Shuqun:

**1. Quest Qo'shish**
```
1. "Daily Quests" tabiga o'ting
2. "Enter new daily quest..." qatoriga yozing
3. "+ Add" tugmasini bosing
✓ Quest qo'shildi, timer 0:00 dan boshlandi
```

**2. Quest Bajarish**
```
1. ⏱️ Play tugmasini bosing - timer ishga tushar
2. Vazifani bajarayotganda shurungi qo'ysiz
3. Tugallasangiz "Stop" bosing
4. ✓ Checkbox bosing - "Done" qilindi
✓ +10 XP + vaqt bo'yicha qo'shimcha XP
```

**3. Timer System**
```
Misal: 45 daqiqa kod yozdi
  → Tugatganingizda timer: 45 min = 2700 soniya
  → 2700 / 60 = 45 daqiqa
  → 45 / 60 = 0.75 soat XP
  → +1 XP daqiqasiga (40 daqiqada +1 XP)
```

**4. Ongoing Mission Qo'shish**
```
1. "Ongoing" tabiga o'ting
2. "Enter ongoing mission..." yozing
3. "+ Add" bosing
4. MODAL oynasi paydo bo'ladi:
   - Mission Name: Nomi
   - Deadline: Sana (masalan 2026-06-15)
   - Category: Tanlang (Learning/Health/Project/etc)
5. "Confirm" bosing
✓ Mission qo'shildi, 0% progress bilan boshlanadi
```

**5. Progress Bo'yicha O'lchamlash**
```
1. Har kun "% Progress" yani qiymatni o'zgartiring
2. Masalan: 20%, 40%, 60%... 100%
3. 100% bo'lganda = +25 XP olasiz
```

**6. Skill Tracking**
```
1. "Analysis" tabiga o'ting
2. "Skill to track" yozing (Coding, English vb)
3. "+ Track" bosing
4. Har kun "TRAIN" bosing = +5 XP
5. Grafik ko'rinadi - o'sib borayaptimi (↑) yoki pasayapmi (↓)
```

---

## 💻 Texnik Tavsif

### Frontend (HTML/CSS/JS)

#### **Fayllar:**
- `index.html` - Butun aplikatsiya bitta faylda

#### **Texnologiyalar:**
- **HTML5** - Struktura
- **CSS3** - Dark tema (Solo Leveling uslubi)
- **Vanilla JavaScript** - Logika
- **LocalStorage** - Ma'lumotlar saqlash (brauzer xotirasi)
- **FontAwesome** - Ikonkalar

#### **Dizayn Elementlari:**
```
Dark Theme:
  - Background: #050a14 (qorong'i blu)
  - Text: #e2e8f0 (oq)
  - Accent: #00a8ff (neon blu)
  - Highlights: #a855f7 (purpur), #f59e0b (oltin)

Animatsiyalar:
  - Scanlines effect (retro ko'rinish)
  - Pulsing XP bar
  - Glow effects (neon)
  - Fade in/out transitions
```

#### **State Management:**
```javascript
state = {
  quests: [
    {name: "Kod yoz", done: false, elapsed: 0, timerRunning: false, timerStart: null}
  ],
  ongoing: [
    {name: "Fitnes", deadline: "2026-05-21", category: "Health", progress: 40, done: false}
  ],
  distractions: [
    {name: "Instagram", mins: 45}
  ],
  skills: [
    {name: "Coding", xp: 25, history: [0, 5, 10, 15, 20, 25]}
  ],
  totalXP: 150,
  log: [
    {time: "14:30", msg: "Quest added: Kod yoz", xp: 0}
  ],
  weekData: {
    "Mon Jan 1 2024": {score: 45, done: 3, total: 5}
  }
}
```

#### **LocalStorage Format:**
```javascript
localStorage.getItem('hs') → JSON string
// Har refresh baribir save bo'ladi
// Brauzer yopilsa ham ma'lumotlar saqlanadi
```

---

## 🚀 O'rnatish va Ishga Tushirish

### **Variant 1: Telegram Web App (Tavsiya qilinadi)**

**Telegram Botini Yaratish:**
```bash
1. @BotFather ga yozing Telegramda
2. /newbot bosing
3. Botning nomini kiriting (masalan: Hunter_System_Bot)
4. Token olabotsiz (masalan: 123456:ABC-DEF)
```

**Python Bot Kodi:**
```python
# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🎮 Open Hunter System", 
                           web_app=WebAppInfo(url="YOUR_WEB_APP_URL"))
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Xush kelibsiz!", reply_markup=reply_markup)

app = Application.builder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
```

### **Variant 2: Simple HTML (Kompyuter/Telefon Brauzerida)**

1. `index.html` faylini saqlang
2. Brauzerda oching: `file:///path/to/index.html`
3. Bitti!

### **Variant 3: Web Serveri (Vercel/Netlify)**

```bash
1. GitHub'ga yuklab oling
2. Vercel/Netlify'ga ulang
3. Avtomatik deploy bo'ladi
4. Link olabotsiz
```

---

## 📱 Foydalanish Bo'limi

### **Kunlik Rutin:**

**Ertalab (8:00):**
```
1. App ni oching
2. Bugun qilmoqchi bo'lgan 3-5 ta vazifani qo'shing
   - "30 min kod yozish"
   - "1 soat matem o'qish"
   - "15 min o'zim vaqtim" (sport, sho'lqa vb)
3. **Level Status** ko'ring (nechi XP kerak?)
```

**Kun bo'ylab:**
```
1. Vazifani boshlanganda ⏱️ Play bosing
2. Tugallanganda ✓ Checkbox bosing
3. Chalg'iyotganingiz vaqtni "+15m" orqali qo'shing
```

**Oqshom (21:00):**
```
1. "Progress" tabiga o'ting
2. Bugungi performance ko'ring
3. "Skill Growth" - har ko'nikma uchun 1-2 marta "TRAIN" bosing
4. Oxirgi 7 kunni tahlil qiling - qaysi kunlar yaxshi edi?
```

### **Haftalik Tahlil:**
```
Friday oqshom:
1. "Progress" - haftalik grafik ko'ring
2. "Analysis" -> Focus Drains
   - Qaysi narsalar ko'p vaqt oladir?
   - Keyingi hafta kamroq qilib qo'yish mumkinmi?
3. Strategi o'zgartiring agar kerak bo'lsa
```

---

## 📂 Fayl Tuzilishi

```
hunter-system/
│
├── index.html              ← Butun aplikatsiya
├── README.md              ← Bu fayl
├── bot.py                 ← Telegram bot kodi (optional)
├── requirements.txt       ← Python kutubxonalari
└── assets/
    └── logo.png          ← Optional: Logo
```

### **index.html Tuzilishi:**
```html
<!DOCTYPE html>
<html>
<head>
  <!-- Meta va CSS stilları -->
</head>
<body>
  <!-- Header (sistema xabari) -->
  <!-- Stats cards (Level, XP, Streak, Done) -->
  <!-- Rank bar (XP progress) -->
  
  <!-- Tabs -->
  ├── Daily Quests
  ├── Ongoing Missions
  ├── Progress
  └── Analysis
  
  <!-- Modals -->
  └── Add Ongoing Mission Dialog
  
  <!-- JavaScript (butun logika) -->
</body>
</html>
```

---

## 🔧 Xatolar va Yechimlar

### **Muammo 1: Ma'lumotlar saqlanmaydi**
```
❌ Sabab: LocalStorage o'chib ketdi yoki Private browsing
✓ Yechim: Normal tab oching, Private mode o'chib qo'ying
```

### **Muammo 2: Timer noto'g'ri hisoblanadi**
```
❌ Sabab: Brauzer tab background'da
✓ Yechim: App'ni aktiv tab'da saqlang
✓ Yechim: Timer'ni "Stop" bosib to'xtatib qo'ying
```

### **Muammo 3: Telegram botda web app ochilmaydi**
```
❌ Sabab: URL noto'g'ri yoki https emas
✓ Yechim: Telegram faqat https qabul qiladi (http emas)
✓ Yechim: Netlify/Vercel'da deploy qiling
✓ Yechim: self-signed SSL cert ishlatmang
```

### **Muammo 4: Mobil'da dizayn buzuladi**
```
✓ Yechim: Bitta .html faylda responsive
✓ Yechim: Grid va flex responsive qo'lyapti
✓ Yechim: Font size mobile uchun optimized
```

---

## 📊 Ranking Tizimi

| Rank | Min XP | Max XP | Ko'ring | Muddati |
|------|--------|--------|--------|---------|
| E-Rank | 0 | 99 | Boshlang'ich | 1 hafta |
| D-Rank | 100 | 299 | Boshlang'ich + | 2 hafta |
| C-Rank | 300 | 699 | Yetakchi | 3-4 hafta |
| B-Rank | 700 | 1499 | Ustozi | 1-2 oy |
| A-Rank | 1500 | 2999 | Tanlovli | 2-3 oy |
| S-Rank | 3000 | 4999 | Noyob | 3-4 oy |
| National | 5000+ | ∞ | Milliy | O'zbeksiz |

---

## 🎯 XP Tizimi

```javascript
// Har bir amaliyon uchun XP

Daily Quest Bajarish     → +10 XP
Daily Quest Vazifasida   → +1 XP (har 40 daqiqada)
Ongoing Mission Tugall   → +25 XP
Skill Training           → +5 XP (har bir "TRAIN")
Focus Time               → +1 XP (har 40 daqiqada)

Misal:
  Quest: "2 soat Python" (120 minut)
  → +10 XP (bazasi)
  → +3 XP (120 / 40 = 3)
  = +13 XP total
```

---

## 🌟 Advanced Features (Kelasi Versiya)

```
[ ] Export to CSV
[ ] Cloud sync (Google Drive)
[ ] Team mode (o'zaro kuzatish)
[ ] Achievements (badge sistemi)
[ ] Custom quests shaklonlari
[ ] Scheduled reminders
[ ] Dark/Light theme toggle
[ ] Multi-language support
```

---

## 📧 Masalalar va Takliflar

Agar muammo bo'lsa yoki shunaqa xohlasangiz:

```
1. GitHub Issues'da yozing
2. Email qilasiz
3. Telegram: @yourbot'ga xabar yuboring
```

---

## 📜 Litsenziya

**MIT License** - Shunchaki foydalaning, o'zgartiring, taqsim qiling!

---

## 👨‍💻 Qanday Ishlatildi

```
- HTML5, CSS3, Vanilla JS (Framework emas)
- FontAwesome Icons (6.4.0)
- Google Fonts (Rajdhani, Share Tech Mono)
- LocalStorage API (Browser storage)
- Zero Dependencies (Hech nima o'rnatish kerak emas!)
```

---

## 🚀 O'zlashtirish (Customization)

### **Rang O'zgartirish:**
```css
:root {
  --bg: #050a14;        /* Fon rangi */
  --blue: #00a8ff;      /* Asosiy rang */
  --purple: #7c3aed;    /* Secondary */
  --gold: #f59e0b;      /* Accent */
}
```

### **Ranking O'zgartirish:**
```javascript
const RANKS = [
  {name: 'E-Rank', min: 0, next: 100},
  {name: 'D-Rank', min: 100, next: 300},
  // Shunga o'xshash...
]
```

### **XP Miqdori O'zgartirish:**
```javascript
// Daily Quest = +10 XP (14-qatorda)
state.quests.push({...})
// +10 XP beradi

// Skill Training = +5 XP (540-qatorda)
state.skills[i].xp += 5;
```

---

## 💡 Maslahatlar

### **Solo Leveling Ruhida:**
1. **Her gun** bitta quest tugat = **7 XP min**
2. **Haftalik streakni** kesma (7 kunni ketma-ket)
3. **Focusing** distractions kuzating - 45 min > 20 min
4. **Skills** regulyar o'zlashtiring - tavaqalliy emas
5. **Ranking** yuzasidan sabrab bosing, XP emas

### **Motivatsiya Mantrag'i:**
```
Kunlik:  +20 XP = 5 kun = 1 Rank
Oylik:   +600 XP = C-Rank maqsad
Yillik:  +7000 XP = S-Rank yoki Uniqni
```

---

## 🎬 Video Tutorial Skripti

```
[0:00] Bosh sahifani ko'rsating
[0:30] "Daily Quests" qo'shing, Timer bosing
[1:00] Quest tugat, XP oling, Level ko'ring
[1:30] "Ongoing" missiyani qo'shing
[2:00] Progress tab, haftalik grafik
[2:30] Skills tab, training bo'limini ko'rsating
[3:00] "Analysis" - distractions va growth trends
[3:30] Login/Saving (LocalStorage)
```

---

## 📞 Support

```
🌐 Web:     https://yoursite.com
📱 Telegram: @hunterbotuz
💌 Email:    support@example.com
🐙 GitHub:   github.com/yourusername/hunter-system
```

---

**Xush kelibsiz Hunter System'ga! 🗡️ 
Bugun qilgan har bir vazifa sizni O'ndan yanada kuchliroq qiladi!**

*Built with ❤️ for achievers*
