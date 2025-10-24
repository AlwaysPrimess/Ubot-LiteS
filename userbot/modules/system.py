# userbot/modules/system.py
from telethon import events
import platform
from userbot.utils.helpers import get_uptime

@events.register(events.NewMessage(pattern=r'^\.sys$'))
async def system_info(event):
    info = f"""
🧠 **LiteS System Info**
• Platform: {platform.system()}
• Release: {platform.release()}
• Machine: {platform.machine()}
• Python: {platform.python_version()}
• Uptime: {get_uptime()}
"""
    await event.reply(info)
