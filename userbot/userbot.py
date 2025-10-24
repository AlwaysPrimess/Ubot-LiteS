# userbot/userbot.py
from telethon import TelegramClient, events
import json
import asyncio
import os

async def run_userbot():
    with open("userbot/database/config.json", "r") as f:
        config = json.load(f)

    api_id = config.get("api_id")
    api_hash = config.get("api_hash")
    session_name = config.get("session", "LiteSUserbot")

    client = TelegramClient(session_name, api_id, api_hash)

    @client.on(events.NewMessage(pattern=r"\.help"))
    async def help_command(event):
        await event.reply(
            "**🧩 LiteS Userbot Modules (10 Total)**\n"
            "• admin\n• adzan\n• alquran\n• anime\n• alkitab\n"
            "• animasi\n• afk\n• archive\n• system\n• utility\n\n"
            "_Gunakan sesuai prefix yang telah Anda set._"
        )

    print("✅ LiteS Userbot sedang berjalan...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(run_userbot())
