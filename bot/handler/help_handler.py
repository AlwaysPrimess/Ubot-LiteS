# bot/handlers/help_handler.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 Resiko Userbot", url="https://telegra.ph/Resiko-Ubot-10-24")],
        [InlineKeyboardButton("🏠 Kembali", callback_data="back_start")],
    ]

    text = (
        "**📘 Panduan Pengguna LiteS**\n\n"
        "Cara membuat userbot:\n"
        "1. Tekan tombol *Buat Userbot* di menu utama.\n"
        "2. Ikuti instruksi pengisian nomor dan kode OTP.\n"
        "3. Setelah tersambung, userbot aktif otomatis.\n\n"
        "**⚠️ Ketentuan:**\n"
        "Resiko dan syarat bisa kamu baca di tautan berikut:\n"
        "[Baca Disini](https://telegra.ph/Resiko-Ubot-10-24)\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
