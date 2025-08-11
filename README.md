# Name_converter_bot
Telegram bot to convert Names from Cyrillic to Latin script

Инструкция запуска Телеграмм-бота через Docker:

1. Установите Docker - https://docs.docker.com/engine/install/
2. Клонируйте репозиторий на локальный компьютер
3. Создайте файл .env и укажите в нем бот-токен: BOT_TOKEN=ваш_токен_бота
4. В терминале укажите команду, чтобы собрать Docker-образ: docker build -t name_converter_bot .
5. Запустите контейнер docker run --name name_converter_bot --env-file .env -d name_converter_bot
6. Чтобы остановить контейнер используйте команду docker stop name_converter_bot
7. Посмотреть логи можно через docker logs -f name_converter_bot 
