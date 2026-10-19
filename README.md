# 🏋️‍♂️ Synchromatica Fitness — Telegram Mini App & Web Трекер

<p align="center">
  <a href="https://juzoo9.github.io/synchromatica-fitness/"><img src="https://img.shields.io/badge/🚀_Запустить_приложение-GitHub_Pages-2ecc71?style=for-the-badge" alt="Launch App"></a>
  <a href="https://t.me/synchromatica"><img src="https://img.shields.io/badge/📢_Telegram_Канал-@synchromatica-0088cc?style=for-the-badge&logo=telegram" alt="Telegram Channel"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Статус-24%2F7_Online-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Шифрование-AES--256--GCM_%2B_SHA--256-blueviolet" alt="Encryption">
  <img src="https://img.shields.io/badge/Платформа-Telegram_Mini_App_%2B_Web-blue" alt="Platform">
  <img src="https://img.shields.io/badge/Хранилище-Telegram_CloudStorage_%2B_Local-orange" alt="Storage">
</p>

---

## ⚡ О проекте

**Synchromatica Fitness** — автономный персональный трекер тренировок в зале с научно обоснованной аналитикой прогрессии весов, работающий 24/7 без серверов и баз данных. 

Приложение адаптировано как для мобильного интерфейса **Telegram Mini App**, так и для десктопного **Web-браузера на ПК** с автоматической синхронизацией по защищённой персональной ссылке.

👉 **[Открыть приложение онлайн](https://juzoo9.github.io/synchromatica-fitness/)**

---

## 🎁 Полезные материалы и сообщество 

> 💡 **Ищешь проверенные программы тренировок и схемы прогрессии?**  
> В Telegram-канале [**@synchromatica**](https://t.me/synchromatica) публикуются:
> - 📋 Готовые тренировочные сплиты (Push-Pull-Legs, Верх/Низ, Full Body) с адаптацией под этот трекер;
> - 🔬 Научные разборы гипертрофии и силовых плато (NSCA, Brad Schoenfeld, Eric Helms);
> - 🤖 Промпты для фитнес-нейросетей и калькуляторы калорий/КБЖУ.
> 
> 👉 **[Перейти в канал @synchromatica и забрать схемы](https://t.me/synchromatica)**

---

## 🚀 Ключевые возможности

### 1. 🧠 Научная аналитика прогрессии (NSCA & Double Progression)
* **Правило 2-для-2 (NSCA 2-for-2 Rule)**: если вы выполняете вес 2 тренировки подряд на 10+ повторений — алгоритм рекомендует шаг в весе (`+2.5 кг` для верха, `+5 кг` для ног).
* **Детектор плато**: выявление застоя веса (3+ сессии подряд без роста повторений) и советы по преодолению (микрошаги, смена диапазона повторений).
* **Подсказки прямо во время подхода**: трекер напоминает прошлый рекорд и рекомендует вес для первого подхода.

### 2. 📅 Расписание и полная кастомизация
* Готовый базовый сплит: **Понедельник** (Грудь/Трицепс), **Среда** (Спина/Бицепс), **Пятница** (Ноги/Плечи).
* Создание произвольных тренировок и дней (Суббота: Кардио/Пресс, Full Body и др.).
* Добавление любых упражнений прямо на лету во время идущей тренировки.

### 3. 🔒 Сквозное одностороннее шифрование (Privacy-First)
* **Никаких открытых Telegram ID**: идентификатор пользователя пропускается через односторонний хэш **SHA-256** с солью. Реальный аккаунт восстановить невозможно.
* **Шифрование данных AES-GCM 256-bit**: все тренировки, веса и история хранятся в зашифрованном виде. Доступ к расшифровке имеет только владелец ключа.

### 4. 💻 Адаптивный Web (ПК) + Telegram (Мобилка)
* **В Telegram**: мобильный интерфейс, безопасные отступы, тактильный виброотклик (Telegram Haptics).
* **На компьютере**: просторный двухколоночный дашборд, скрытая нижняя шторка, верхние вкладки, интерактивные SVG-графики весов.

### 5. 🗄️ Хранение по ключам и резервные копии
* Каждая тренировка сохраняется отдельным ключом (`w_<id>`), что снимает лимит 4 КБ и позволяет хранить историю годами.
* Кнопка **«📥 Резервная копия»**: экспорт и импорт базы данных в один клик в формате JSON.

---

## 🤖 Как подключить трекер к своему боту в Telegram

Вам не нужно писать код или держать включённый компьютер — приложение развёрнуто на серверах GitHub Pages:

1. Откройте официального бота [@BotFather](https://t.me/BotFather) в Telegram.
2. Введите команду `/mybots` и выберите вашего бота.
3. Перейдите: **Bot Settings** → **Menu Button** → **Configure menu button**.
4. Укажите ссылку:
   ```text
   https://juzoo9.github.io/synchromatica-fitness/
   ```
5. Введите название кнопки (например, `🏋️ Трекер` или `💪 Зал`).

Готово! Теперь кнопка меню в боте будет открывать трекер в Telegram с привязкой к аккаунту каждого пользователя.

---

## 💼 Разработка ботов и AI-агентов под ключ (Воронка 2)

> 🛠️ **Нужен Telegram Mini App, сложный Telegram-бот или AI-автоматизация для вашего бизнеса?**
>
> Специализируюсь на:
> - Telegram Mini Apps & WebApps (адаптивные интерфейсы, PWA, CloudStorage);
> - AI-агентах (CrewAI, LangGraph, OpenRouter, GPT-4, Claude);
> - Защищённых парсерах и микросервисах (Python, FastAPI, PostgreSQL).
> 
> 📩 **Связаться со мной:**
> - Telegram: [**@DigitalCoinMainer**](https://t.me/DigitalCoinMainer)
> - Telegram-канал: [**@synchromatica**](https://t.me/synchromatica)
> - GitHub: [**@Juzoo9**](https://github.com/Juzoo9)

---

## 🛠️ Локальный запуск (опционально)

Если вы хотите запустить собственного Telegram-бота с генерацией ссылок на Python:

```bash
# Клонируйте репозиторий
git clone https://github.com/Juzoo9/synchromatica-fitness.git
cd synchromatica-fitness

# Установите зависимости
pip install -r requirements.txt

# Настройте .env
cp .env.example .env
# Укажите ваш BOT_TOKEN из @BotFather

# Запустите бота
python bot.py
```

---

<p align="center">
  Разработано с ❤️ для тех, кто прогрессирует в зале.<br>
  Подписывайтесь на обновления: <b><a href="https://t.me/synchromatica">@synchromatica</a></b>
</p>
