from datetime import datetime, date
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

def _parse(text: str):
    return datetime.strptime(text.strip(), "%Y-%m-%d").date()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь дату в формате ГГГГ-ММ-ДД, и я скажу, сколько дней осталось или прошло."
    )

async def calc_days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        target = _parse(update.message.text)
        today = date.today()
        delta = (target - today).days
        if delta > 0:
            await update.message.reply_text(f"До {target} осталось {delta} дней.")
        elif delta < 0:
            await update.message.reply_text(f"С {target} прошло {-delta} дней.")
        else:
            await update.message.reply_text("Сегодня именно эта дата!")
    except ValueError:
        await update.message.reply_text("Неверный формат. Используй ГГГГ-ММ-ДД.")

def main():
    TOKEN = "token"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc_days))
    app.run_polling()

if __name__ == "__main__":
    main()
