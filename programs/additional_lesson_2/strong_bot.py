
from telegram.ext import Application, MessageHandler, CommandHandler, filters
from telegram import KeyboardButton, ReplyKeyboardMarkup


# USER_ID = 1711747429


async def start(update, context):
    chat_id = update.effective_chat.id
    print(update)
    print(context)
    username = update.message.from_user.first_name
    await context.bot.send_message(chat_id=chat_id, text=f'Salam {username}')


async def echo_answer(update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=update.message.text)


async def show_buttons(update, conetxt):
    keyboard = [
        [
            KeyboardButton('Кнопка - 1'), 
            KeyboardButton('Кнопка - 2')
        ],
        [
            KeyboardButton('Кнопка - 3'), 
            KeyboardButton('Кнопка - 4'),
            KeyboardButton('Кнопка - 5')
        ],
        [
            KeyboardButton('Кнопка - 6'), 
            KeyboardButton('Кнопка - 7')
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'нажмите на любую кнопку',
        reply_markup=reply_markup
        )

                    # Между builder() и build() помещаем дополнительные параметры
app = Application.builder().token('your yoken').build()
# Обработчик комманд
app.add_handler(CommandHandler('start', start))
# Операции над фильтрами
# AND - &, OR - |, NOT = ~

# Обработчик комманд
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_answer))

# Обоработчик команд по кнопке
app.add_handler(CommandHandler('show_buttons', show_buttons))
app.run_polling()