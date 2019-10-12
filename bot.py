import telebot
import logging
from config import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Ну это по классике, логи

bot = telebot.TeleBot(Config.BOT_TOKEN)  # Создает объект класса "TeleBot", то есть нашего бота

#file=open('Statistic.txt', 'r')
#file2=open('UserCounter.txt', 'r')
#file3=open('Statistic.txt', 'a')
#file4=open('UserCounter.txt', 'w')

#text=file.read()
#text2=file2.read()
#text2=int(text2)+1

@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])  # декоратор который заставляет пользователя реагировать на новые сообщения

@bot.message_handler(commands=['mo2'])

# Записывать в файл чат айди и каждый раз проверять если этот чат айди в это файле если нет то 
# плюс один запуск бота от уникального пользователя

def sending_auto2(message):
    
    if message.text=="/mo2":
      bot.send_message(message.chat.id, 'Группа МО-2 \n \n'+'*Вторник*'+'\n'+'15:20 (ауд. 231) лекция Python\n\n'+'*Среда*'+'\n'+'13-40 (ауд. 230) лаба Python (1я подгруппа)\n10-10 (ауд. 235) лаба Python (2я подгруппа)\n12-00 (ауд. 235) лаба Python (3я подгруппа)\n', parse_mode="Markdown")
      
      #if message.chat.id not in text:
        #file3.write(message.chat.id+', ')
        #file4.write(text2)

    elif message.chat.id > 0:
      bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',disable_web_page_preview=True)  # Отправляет авто сообщение
      
      #if message.chat.id not in text:
        #file3.write(message.chat.id+', ')
        #file4.write(text2)


    # NOTE
    # Не отправляем сообщения в общие чаты.
    # else:
      # bot.send_message(chat_id=message.chat.id, text='Это сообщение в чат', parse_mode='html',disable_web_page_preview=True)

if __name__ == '__main__':
    bot.polling()  # Заставляет бота получать уведомления о новых сообщениях

file.close()
file2.close()
file3.close()
file4.close()
