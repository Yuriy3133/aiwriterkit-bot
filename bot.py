from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
PDF_URL = os.getenv("PDF_URL", "https://yuriy3133.github.io/ai-writer-kit/ai-writer-kit-guide-dark.pdf")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # числовой ID (строка)

# Стартовое меню
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📥 Скачать PDF", callback_data="download_pdf")],
        [InlineKeyboardButton("❓ Задать вопрос", callback_data="ask_question")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Привет! Я бот AI Writer Kit.\nВыбери действие:", reply_markup=reply_markup)

# Обработка кнопок
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "download_pdf":
        await query.message.reply_text(f"📄 Вот ссылка на PDF: {PDF_URL}")
    elif query.data == "ask_question":
        await query.message.reply_text("❓ Напиши свой вопрос одним сообщением.")

# Ловим текстовые вопросы
async def handle_message(update: Update, context: CallbackContext):
    question = update.message.text
    user = update.message.from_user

    # Ответ пользователю
    await update.message.reply_text(f"✅ Спасибо! Получил: «{question}»\nСкоро вернусь с ответом.")

    # Уведомление админу
    if ADMIN_CHAT_ID:
        msg = f"💬 Новый вопрос от @{user.username or 'без ника'}:\n\n{question}"
        try:
            await context.bot.send_message(chat_id=int(ADMIN_CHAT_ID), text=msg)
        except Exception as e:
            print(f"Ошибка отправки админу: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
