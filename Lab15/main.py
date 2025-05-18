import random
import string
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

user_passwords = {}

def start(update: Update, context: CallbackContext):
    keyboard = [
        ['Сгенерировать пароль'],
        ['Мои сгенерированные пароли'],
        ['Очистить мои пароли'],
        ['О боте']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(f'Привет! Я бот для генерации паролей.', reply_markup=reply_markup)

def generate_password(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    length = random.randint(8,16)
    password = ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%^&*()') for _ in range(length))
    
    if user_id not in user_passwords:
        user_passwords[user_id] = []
    user_passwords[user_id].append(password)
    
    update.message.reply_text(f'Ваш новый пароль: {password}')

def show_passwords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if user_id not in user_passwords or not user_passwords[user_id]:
        update.message.reply_text('У вас еще нет сгенерированных паролей.')
        return
    
    passwords_text = 'Ваши пароли:\n' + '\n'.join([f'{i+1}. {pwd}' for i, pwd in enumerate(user_passwords[user_id])])
    update.message.reply_text(passwords_text)

def clear_passwords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    
    if user_id not in user_passwords or not user_passwords[user_id]:
        update.message.reply_text('У вас нет паролей для очистки.')
        return
    
    user_passwords[user_id] = []
    update.message.reply_text('Все ваши пароли удалены.')

def about_bot(update: Update, context: CallbackContext):
    about_text = 'Бот для генерации и хранения паролей.\nПароли хранятся только до перезапуска бота.'
    update.message.reply_text(about_text)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    
    commands = {
        'Сгенерировать пароль': generate_password,
        'Мои сгенерированные пароли': show_passwords,
        'Очистить мои пароли': clear_passwords,
        'О боте': about_bot
    }
    
    if text in commands:
        commands[text](update, context)
    else:
        update.message.reply_text('Используйте кнопки меню.')

def main():
    token = 'ВСТАВЬТЕ СВОЙ ТОКЕН'
    
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
