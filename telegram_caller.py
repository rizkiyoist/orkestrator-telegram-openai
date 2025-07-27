# modifikasi dari https://python-telegram-bot.org originally licensed under LGPLv3
#
# Copyright (c) Rizki Hadiaturrasyid
#

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()