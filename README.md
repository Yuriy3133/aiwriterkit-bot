# AI Writer Kit — бесплатный Telegram‑бот (Deploy за 5–10 минут)

Простой бот без платных сервисов. Работает на **python-telegram-bot** через long polling.
PDF высылает ссылкой, вопросы принимает и (опционально) пересылает админу.

## 1) Что внутри
- `bot.py` — код бота
- `requirements.txt` — зависимости
- `render.yaml` — деплой на Render (бесплатно)
- `railway.json` — деплой на Railway (бесплатно)

---

## 2) Быстрый старт локально
1. Установи Python 3.10+
2. В терминале:
   ```bash
   pip install -r requirements.txt
   export BOT_TOKEN="ТОКЕН_ОТ_BOTFATHER"
   python bot.py
   ```
3. В Telegram: открой своего бота → отправь `/start`

---

## 3) Деплой на Render (бесплатно)
1. Зайди на https://render.com → Sign up (через GitHub/Google).
2. Создай новый **Blueprint**: "New + → Blueprint".
3. Укажи репозиторий, в котором лежат эти файлы (или загрузите ZIP через приватный репо).
4. Render сам подхватит `render.yaml`.
5. В переменных окружения **BOT_TOKEN** вставь свой токен от BotFather, **PDF_URL** можно оставить по умолчанию.
6. Создай сервис (тип **Worker**, план **Free**).
7. Нажми **Deploy** — через ~1 минуту бот будет онлайн.

> Если нет репозитория: создай новый на GitHub, загрузите туда файлы из архива.

---

## 4) Деплой на Railway (бесплатно)
1. Зайди на https://railway.app → Sign in.
2. Создай New Project → Deploy from GitHub (репозиторий с этими файлами).
3. В Settings проекта добавь переменные:
   - `BOT_TOKEN` — токен от BotFather
   - `PDF_URL` — `https://yuriy3133.github.io/ai-writer-kit/ai-writer-kit-guide-dark.pdf`
   - `ADMIN_CHAT_ID` — (по желанию) твой числовой Telegram ID
4. Railway сам определит Python и запустит `python bot.py` (описано в `railway.json`).

---

## 5) Как узнать свой ADMIN_CHAT_ID (необязательно)
- Напиши этому боту: **@userinfobot** — он покажет твой numeric ID.
- Или временно добавь в `handle_message` вывод `update.effective_chat.id` в консоль.

---

## 6) Кастомизация
- Измени текст приветствия в `WELCOME`.
- Замени `PDF_URL` на свою ссылку, если нужно.
- Добавь новые кнопки в `start()` и обработку в `button()`.

Готово. Бесплатно, просто и без лишних платформ.
