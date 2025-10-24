# bot/handlers/language_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def language_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_caption(caption="Berhasil Ganti Ke Bahasa Indonesia 🇮🇩", parse_mode="Markdown")
