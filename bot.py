from os import getenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

TOKEN = getenv("BOT_TOKEN", "PASTE_YOUR_TOKEN_HERE")
PDF_URL = getenv("PDF_URL", "https://yuriy3133.github.io/ai-writer-kit/ai-writer-kit-guide-dark.pdf")
ADMIN_CHAT_ID = getenv("ADMIN_CHAT_ID")  # optional: your Telegram numeric ID to get questions forwarded

WELCOME = "👋 Привет! Я бот AI Writer Kit.\nВыбери действие:"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Скачать PDF", callback_data="download_pdf")],
        [InlineKeyboardButton("❓ Задать вопрос", callback_data="ask_question")]
    ]
    await update.message.reply_text(WELCOME, reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "download_pdf":
        await query.message.reply_text(f"📄 Вот ссылка на PDF:\n{PDF_URL}")
    elif query.data == "ask_question":
        await query.message.reply_text("❓ Напиши свой вопрос одним сообщением.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return
    question = update.message.text.strip()
    await update.message.reply_text(
        f"✅ Спасибо! Получил:\n«{question}»\n\nСкоро вернусь с ответом."
    )
    # Optional: forward to admin
    if ADMIN_CHAT_ID:
        try:
            await context.bot.send_message(chat_id=int(ADMIN_CHAT_ID),
                                           text=f"💬 Новый вопрос от @{update.effective_user.username or update.effective_user.id}:\n{question}")
        except Exception as e:
            # Fail silently for user, but log to console
            print("Failed to notify admin:", e)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Доступные команды: /start — меню, /help — помощь.")

def main():
    if not TOKEN or TOKEN == "PASTE_YOUR_TOKEN_HERE":
        raise RuntimeError("Укажи токен: переменная окружения BOT_TOKEN или вставь его в файл.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    # Long polling (проще и бесплатно на Render/Railway)
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
