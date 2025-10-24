# userbot/modules/admin.py
from telethon import events
from userbot.utils.helpers import get_uptime
import datetime

@events.register(events.NewMessage(pattern=r'^\.ping$'))
async def ping(event):
    start = datetime.datetime.now()
    msg = await event.reply("🔄 Pong...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"🏓 **Pong!** `{ms}ms` | Uptime: `{get_uptime()}`")

@events.register(events.NewMessage(pattern=r'^\.id$'))
async def get_id(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        await event.reply(f"👤 **User ID:** `{replied.sender_id}`")
    else:
        await event.reply(f"👤 **Your ID:** `{event.sender_id}`")
