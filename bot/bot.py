# bot/bot.py
import logging
import os
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)
from bot.handlers import (
    start_handler,
    help_handler,
    loyalty_handler,
    userbot_handler,
    status_handler,
    feature_handler,
    support_handler,
    language_handler,
    reset_handler,
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def set_my_commands(application):
    commands = [
        BotCommand("start", "Mulai bot LiteS"),
        BotCommand("help", "Panduan & dukungan pengguna LiteS"),
    ]
    await application.bot.set_my_commands(commands)

def run_bot():
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN tidak ditemukan di file .env")

    app = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start_handler.start))
    app.add_handler(CommandHandler("help", help_handler.help_command))
    app.add_handler(CallbackQueryHandler(start_handler.button_handler))
    app.add_handler(CallbackQueryHandler(loyalty_handler.button_handler))
    app.add_handler(CallbackQueryHandler(userbot_handler.button_handler))
    app.add_handler(CallbackQueryHandler(status_handler.button_handler))
    app.add_handler(CallbackQueryHandler(feature_handler.button_handler))
    app.add_handler(CallbackQueryHandler(support_handler.button_handler))
    app.add_handler(CallbackQueryHandler(language_handler.button_handler))
    app.add_handler(CallbackQueryHandler(reset_handler.button_handler))
    app.add_handler(MessageHandler(filters.TEXT, userbot_handler.text_handler))

    app.post_init = set_my_commands

    logger.info("🤖 LiteS Bot sedang berjalan...")
    app.run_polling()
