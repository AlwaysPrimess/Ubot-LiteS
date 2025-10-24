# bot/handlers/loyalty_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def loyalty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    text = (
        "Anda bukan pengguna userbot, silahkan lakukan pembuatan ubot "
        "jika sudah diberikan hak akses oleh owner atau seles."
    )
    await query.edit_message_caption(caption=text, parse_mode="Markdown")
