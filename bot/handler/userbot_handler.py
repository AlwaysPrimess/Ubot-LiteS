# bot/handlers/userbot_handler.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def create_userbot_intro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    keyboard = [
        [InlineKeyboardButton("📃 Saya Setuju", callback_data="agree_create_ubot")],
        [InlineKeyboardButton("🏠 Menu Utama", callback_data="back_start")],
    ]

    text = (
        "**🤖 LiteS-Userbot**\n\n"
        "**↪️ Kebijakan Pengembalian**\n"
        "Setelah melakukan pembayaran, jika Anda belum memperoleh/menerima manfaat dari pembelian, "
        "Anda dapat menggunakan hak penggantian dalam waktu 2 hari setelah pembelian. Namun, jika Anda telah "
        "menggunakan/menerima salah satu manfaat dari pembelian, termasuk akses ke fitur pembuatan userbot, maka Anda tidak lagi "
        "berhak atas pengembalian dana.\n\n"
        "**🆘 Dukungan**\nUntuk mendapatkan dukungan, Anda dapat:\n"
        "❍ Mengikuti prosedur pembelian dibot ini\n"
        "❍ Resiko userbot bisa [Baca Disini](https://telegra.ph/Resiko-Ubot-10-24)\n"
        "❍ Beli Userbot = SETUJU DAN PAHAM RESIKO\n\n"
        "**👉🏻 Tekan tombol 📃 Saya Setuju** untuk menyatakan bahwa Anda telah membaca dan menerima ketentuan ini dan melanjutkan pembelian.\n"
        "**Jika tidak, tekan tombol 🏠 Menu Utama.**\n\n"
        "**Ads:** [List VPS](https://t.me/moire_market/5)"
    )

    await query.edit_message_caption(caption=text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani input nomor dan OTP"""
    text = update.message.text

    if " " in text and all(x.isdigit() for x in text.split()):
        await update.message.reply_text("🔄 Memproses kode OTP kamu...")
        await update.message.reply_text("✅ Userbot berhasil tersambung!\nKetik /start untuk kembali ke menu utama.")
    elif text.startswith("62"):
        await update.message.reply_text("📩 Kode OTP telah dikirim!\nSilakan masukkan kode OTP dengan spasi, contoh: 1 2 3 4 5 6")
    else:
        return
