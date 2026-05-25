import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💳 Оплатить доступ", callback_data="pay")],
        [InlineKeyboardButton("🎁 Подарить доступ", callback_data="gift")],
        [InlineKeyboardButton("📋 Подробнее о программе", callback_data="info")],
        [InlineKeyboardButton("📢 Задать вопрос", callback_data="question")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Привет, {user.first_name} 👋\n\n"
        f"Этот бот поможет тебе получить доступ к программе.\n\n"
        f"Нажми на кнопку 👇",
        reply_markup=markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "pay":
        await query.edit_message_text("💳 Для оплаты напишите нам: @manager")
    elif query.data == "gift":
        await query.edit_message_text("🎁 Чтобы подарить доступ напишите: @manager")
    elif query.data == "info":
        await query.edit_message_text(
            "📋 О программе:\n\n"
            "— Ежедневные тренировки\n"
            "— Поддержка куратора\n"
            "— Доступ к чату участников\n"
            "— Рекомендации по питанию\n\n"
            "Стоимость: 4990 руб."
        )
    elif query.data == "question":
        await query.edit_message_text("📢 Задайте вопрос: @manager")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
