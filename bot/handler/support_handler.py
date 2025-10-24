# bot/handlers/support_handler.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("📖 Resiko Ubot", url="https://telegra.ph/Resiko-Ubot-10-24")],
        [InlineKeyboardButton("🏠 Kembali", callback_data="back_start")],
    ]

    text = (
        "**🆘 Dukungan LiteS Userbot**\n\n"
        "Panduan lengkap cara membuat userbot tersedia di sini.\n"
        "Klik tombol di bawah untuk membaca resiko userbot."
    )

    await query.edit_message_caption(caption=text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
