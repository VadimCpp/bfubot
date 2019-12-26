# bfubot

> Telegram bot: https://t.me/pyfirstbotbot

This is the starter template for other bots built with python

# Getting started

Откройте терминал и перейдите в директорию с исходным кодом бота. Если вы ещё не скачивали исходники, сделать это и перейти в соответствующую директорию можно с помощью следующих команд:
```
git clone https://github.com/VadimCpp/bfubot.git
cd bfubot
```

Для работы бота необходимы модули, указанные в файле `requirements.txt`. Для их установки используйте следующую команду:
```
pip install -r requirements.txt
```

В папке с исходниками необходимо создать текстовый файл `.env` со следующим содержанием:
```
BOT_TOKEN=YOUR_BOT_TOKEN
MODE=debug
```
Вместо `YOUR_BOT_TOKEN` вставьте токен для бота.

Запустите бота.
```
python bot.py
```

**Используйте VPN в случае проблем с доступом к telegram.org с вашего локального устройства.**