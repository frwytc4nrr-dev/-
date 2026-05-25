import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("💳 Оплатить доступ", callback_data="pay"))
    markup.row(InlineKeyboardButton("🎁 Подарить доступ", callback_data="gift"))
    markup.row(InlineKeyboardButton("📋 Подробнее о программе", callback_data="info"))
    markup.row(InlineKeyboardButton("📢 Задать вопрос", callback_data="question"))
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Привет, {name} 👋\n\nЭтот бот поможет тебе получить доступ к программе.\n\nНажми на кнопку 👇",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "pay":
        bot.edit_message_text("💳 Для оплаты напишите нам: @manager", call.message.chat.id, call.message.message_id)
    elif call.data == "gift":
        bot.edit_message_text("🎁 Чтобы подарить доступ напишите: @manager", call.message.chat.id, call.message.message_id)
    elif call.data == "info":
        bot.edit_message_text(
            "📋 О программе:\n\n— Ежедневные тренировки\n— Поддержка куратора\n— Доступ к чату участников\n— Рекомендации по питанию\n\nСтоимость: 4990 руб.",
            call.message.chat.id,
            call.message.message_id
        )
    elif call.data == "question":
        bot.edit_message_text("📢 Задайте вопрос: @manager", call.message.chat.id, call.message.message_id)

bot.infinity_polling()
