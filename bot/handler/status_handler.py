# bot/handlers/status_handler.py
from telegram import Update
from telegram.ext import ContextTypes
import datetime

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    name = update.effective_user.first_name
    uptime = "25m:17s"
    expire = "None"

    text = (
        f"**LiteS-Userbot**\n\n"
        f"**Status Ubot:** tidak aktif\n"
        f"**Status Pengguna:** *{name}*\n"
        f"**Prefixes :** .\n"
        f"**Tanggal Kedaluwarsa:** {expire}\n"
        f"**Uptime Ubot:** {uptime}"
    )

    await query.edit_message_caption(caption=text, parse_mode="Markdown")
