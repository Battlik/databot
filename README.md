databot Yandex:
Пользователь отправляете дату в формате YYYY-MM-DD — бот отвечает, сколько дней осталось до этой даты/сколько прошло с этого времени. Команда /start показывает краткую подсказку.

Возможности:
Понимает даты вида "2025-11-05".
Отвечает: "До 2025-12-31 осталось N дней" / "С 2025-12-31 прошло N дней" / «Сегодня именно эта дата!».
Основан на python-telegram-bot v20+ (асинхронный API).

Требования:
Python 3.9+

Зависимости:
python-telegram-bot>=20,<21

Быстрый старт:
Создайте бота у @BotFather
Сохраните токен, вида 123456:ABCDEF...
Клонируйте проект и установите зависимости
git clone <Repository> days-bot
cd days-bot
python -m venv .venv
source .venv/bin/activate   
(# Windows: .venv\Scripts\activate)
pip install -r requirements.txt
Укажите токен
