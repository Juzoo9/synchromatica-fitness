# 🏋️‍♂️ Synchromatica Fitness — Telegram Mini App & Web Трекер

<p align="center">
  <a href="https://juzoo9.github.io/synchromatica-fitness/"><img src="https://img.shields.io/badge/🚀_Запустить_приложение-GitHub_Pages-2ecc71?style=for-the-badge" alt="Launch App"></a>
  <a href="https://t.me/synchromatica"><img src="https://img.shields.io/badge/📢_Telegram_Канал-Synchromatica_AI-0088cc?style=for-the-badge&logo=telegram" alt="Telegram Channel"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Статус-24%2F7_Online-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Шифрование-AES--256--GCM_%2B_SHA--256-blueviolet" alt="Encryption">
  <img src="https://img.shields.io/badge/Платформа-Telegram_Mini_App_%2B_Web-blue" alt="Platform">
  <img src="https://img.shields.io/badge/Архитектура-Zero--Backend_%2F_Client--Side-orange" alt="Architecture">
</p>

---

## ⚡ О проекте

**Synchromatica Fitness** — открытый автономный трекер тренировок с алгоритмами прогрессии нагрузок (NSCA) и сквозным шифрованием данных. 

Проект спроектирован как высокоэффективный **Zero-Backend Telegram Mini App**:
- Работает **24/7 без серверов и баз данных** (статический хостинг на GitHub Pages + Telegram CloudStorage).
- Адаптирован под **смартфоны в Telegram** и **десктопные браузеры на ПК** с единой синхронизацией по защищённому токену.
- Разработан в рамках портфолио решений по автоматизации и Telegram-инфраструктуре студии **[Synchromatica AI](https://t.me/synchromatica)**.

👉 **[Запустить веб-версию трекера онлайн](https://juzoo9.github.io/synchromatica-fitness/)**

---

## 🤖 О канале автора: Synchromatica AI | Автоматизация бизнеса

> 💡 **«Я делаю автоматизацию, которая заменяет сотрудников на скрипты. Не в метафорическом смысле — реально. AI-маркетинг.»**  
> 
> В Telegram-канале [**@synchromatica**](https://t.me/synchromatica) автор делится реальным опытом создания IT-проектов и автоматизации процессов для бизнеса:
> - ⚙️ **Замена рутины на скрипты**: как автоматизировать обработку лидов, клиентские воронки и работу операторов без раздувания штата;
> - 🧠 **AI-агенты и нейросети**: внедрение LLM (CrewAI, LangGraph, OpenRouter) в маркетинг, поддержку и бизнес-задачи;
> - 📱 **Telegram Mini Apps и боты**: разбор архитектуры продакшн-проектов (как этот фитнес-трекер), работа с Telegram CloudStorage, базами данных и защитой;
> - 📊 **Парсеры и автоворонки**: сбор данных, мониторинг конкурентов и генерация трафика.
> 
> 👉 **[Перейти в Telegram-канал @synchromatica](https://t.me/synchromatica)**

---

## 💼 Разработка проектов и автоматизация бизнеса под ключ

Нужна автоматизация рабочих процессов, замена рутины сотрудников или разработка цифрового продукта?

**Что разрабатываю под ключ:**
- 🔹 **Telegram Mini Apps & Боты**: адаптивные WebApps любого уровня сложности, платежи, работа с Telegram CloudStorage, виброотклики;
- 🔹 **AI-автоматизация & Агенты**: чат-боты техподдержки, умные классификаторы заявок, интеграция нейросетей в CRM и маркетинг;
- 🔹 **Парсеры и сбор данных**: мониторинг конкурентов, цен, маркетплейсов и баз данных с защитой от блокировок;
- 🔹 **Интеграции**: связки Telegram ↔ CRM (Битрикс24, amoCRM) ↔ Google Sheets ↔ МойСклад.

📩 **Связаться для консультации или заказа проекта:**
- **Личка в Telegram:** [**@DigitalCoinMainer**](https://t.me/DigitalCoinMainer)
- **Telegram-канал:** [**@synchromatica**](https://t.me/synchromatica)
- **GitHub:** [**@Juzoo9**](https://github.com/Juzoo9)

---

## 🚀 Что под капотом у трекера

### 1. 🔒 Сквозное шифрование и приватность (Privacy-First)
* **Односторонний хэш SHA-256 с солью**: реальный Telegram ID никогда не фигурирует в ссылках или ключах хранилища. Восстановить реальный аккаунт математически невозможно.
* **Шифрование AES-GCM 256-bit**: все подходы, рабочие веса и заметки шифруются локально на устройстве перед отправкой в Telegram CloudStorage.

### 2. 🧠 Спортивная прогрессия весов (NSCA 2-for-2 Rule & Double Progression)
* Алгоритм анализирует подходы: если вы выполняете целевой вес 2 тренировки подряд на 10+ повторений — система рекомендует прибавить `+2.5 кг` (верх тела) или `+5 кг` (ноги).
* Детектор плато предупреждает о застое веса при 3+ сессиях подряд без роста.

### 3. 💻 Раздельная адаптация Web (ПК) и Mobile (Telegram)
* **В Telegram**: компактный мобильный вид, тактильный отклик (Haptic Feedback), быстрый таймер отдыха.
* **На ПК**: двухколоночный дашборд 1020px, скрытая нижняя панель, интерактивные SVG-графики весов.

---

## 🤖 Как привязать трекер к своему боту за 1 минуту

Компьютер держать включённым не нужно — всё бесплатно хостится на GitHub Pages:

1. Откройте [@BotFather](https://t.me/BotFather) в Telegram.
2. Введите команду `/mybots` и выберите вашего бота.
3. Перейдите: **Bot Settings** → **Menu Button** → **Configure menu button**.
4. Укажите ссылку:
   ```text
   https://juzoo9.github.io/synchromatica-fitness/
   ```
5. Введите название кнопки (например, `🏋️ Трекер`).

Готово! Каждый пользователь открывает приложение со своей изолированной зашифрованной базой данных.

---

<p align="center">
  Разработано <b><a href="https://t.me/DigitalCoinMainer">@DigitalCoinMainer</a></b> · Проекты и кейсы в канале: <b><a href="https://t.me/synchromatica">@synchromatica</a></b>
</p>
