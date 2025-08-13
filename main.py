# modifikasi dari https://python-telegram-bot.org originally licensed under LGPLv3
#
# Copyright (c) Rizki Hadiaturrasyid
#

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import test_caller


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("your token here").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, test_caller.echo))

app.run_polling()