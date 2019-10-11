import telebot
import logging
from config import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Ну это по классике, логи

bot = telebot.TeleBot(Config.BOT_TOKEN)  # Создает объект класса "TeleBot", то есть нашего бота


@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])  # декоратор который заставляет пользователя реагировать на новые сообщения

@bot.message_handler(commands=['mo2'])

    
def sending_auto2(message):
    
    if message.text=="/mo2":
      bot.send_message(message.chat.id, 'Группа МО-2 \n \n'+'**Вторник**\n\n'+'15:20 (ауд. 231) лекция Python\n'+'**Среда**\n\n'+'13-40 (ауд. 230) лаба Python (1я подгруппа)\n10-10 (ауд. 235) лаба Python (2я подгруппа)\n12-00 (ауд. 235) лаба Python (3я подгруппа)\n')

    elif message.chat.id > 0:
      bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',disable_web_page_preview=True)  # Отправляет авто сообщение

    # NOTE
    # Не отправляем сообщения в общие чаты.
    # else:
      # bot.send_message(chat_id=message.chat.id, text='Это сообщение в чат', parse_mode='html',disable_web_page_preview=True)

if __name__ == '__main__':
    bot.polling()  # Заставляет бота получать уведомления о новых сообщениях
