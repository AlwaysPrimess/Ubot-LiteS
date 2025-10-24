# bot/handlers/start_handler.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💎 Loyalty Poin", callback_data="loyalty"),
            InlineKeyboardButton("🤖 Buat Userbot", callback_data="create_userbot"),
        ],
        [
            InlineKeyboardButton("📊 Status Akun", callback_data="status"),
            InlineKeyboardButton("🧩 Cek Fitur", callback_data="feature"),
        ],
        [
            InlineKeyboardButton("🆘 Dukungan", callback_data="support"),
            InlineKeyboardButton("🌐 Bahasa", callback_data="language"),
        ],
        [
            InlineKeyboardButton("🌀 Reset Emoji", callback_data="reset_emoji"),
            InlineKeyboardButton("🌀 Reset Prefix", callback_data="reset_prefix"),
        ],
        [
            InlineKeyboardButton("🌀 Reset Text", callback_data="reset_text"),
            InlineKeyboardButton("🔁 Reset Userbot", callback_data="reset_userbot"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "**📢 Halo!** FVIOSS_- [Litex-Userbot](https://t.me/Lite_Xbot) "
        "**siap membantumu membuat Userbot dengan fitur Broadcast dan bonus menarik dari Loyalty Point dan Kode Referral.**\n"
        "**💵 System Auto-Payment:**Nikmati kemudahan sistem pembayaran otomatis (auto payment) tanpa perlu menunggu owner online!Pilih button [buat userbot] dan ikuti intruksinya.\n"
        "**🈂️ Fitur Utama (via Button):**• Fitur Broadcast.• Fitur Auto PM.\n"
        "**📋 Syarat dan ketentuan akun telegram!.**[BACA DISINI](https://telegra.ph/Resiko-Ubot-10-24) **ketentuanya!.**"
        "**Ads:** [List VPS](https://t.me/moire_market/5)"
    )

    await update.message.reply_photo(
        photo=open("bot/assets/start_banner.jpg", "rb"),
        caption=text,
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "loyalty":
        from .loyalty_handler import loyalty
        return await loyalty(update, context)
    elif data == "create_userbot":
        from .userbot_handler import create_userbot_intro
        return await create_userbot_intro(update, context)
    elif data == "status":
        from .status_handler import status
        return await status(update, context)
    elif data == "feature":
        from .feature_handler import feature
        return await feature(update, context)
    elif data == "support":
        from .support_handler import support
        return await support(update, context)
    elif data == "language":
        from .language_handler import language_menu
        return await language_menu(update, context)
    elif data.startswith("reset_"):
        from .reset_handler import reset_handler_button
        return await reset_handler_button(update, context)
