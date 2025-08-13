from telegram import Update
from telegram.ext import ContextTypes

# async digunakan supaya bisa pakai keyword await
# await diperlukan supaya program menunggu pesan
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)