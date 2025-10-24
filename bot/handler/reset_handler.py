# bot/handlers/reset_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def reset_handler_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "reset_prefix":
        text = "Buat userbot dulu!!"
    else:
        text = "Hanya owner/akses yang dapat menggunakan perintah ini."

    await query.edit_message_caption(caption=text, parse_mode="Markdown")
