# bot/handlers/feature_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def feature(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    text = (
        "**🧩 Daftar Fitur LiteS Userbot**\n"
        "• Broadcast\n"
        "• Auto PM\n"
        "• Prefix Custom\n"
        "• Trial 12 Hari\n"
        "• Anti Delay Reset\n"
        "• Dan banyak lagi..."
    )
    await query.edit_message_caption(caption=text, parse_mode="Markdown")
