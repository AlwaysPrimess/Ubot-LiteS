# userbot/modules/afk.py
from telethon import events

AFK = {}

@events.register(events.NewMessage(pattern=r'^\.afk (.+)'))
async def set_afk(event):
    reason = event.pattern_match.group(1)
    AFK[event.sender_id] = reason
    await event.reply(f"💤 **AFK aktif:** {reason}")

@events.register(events.NewMessage(incoming=True))
async def check_afk(event):
    if event.is_private and event.chat_id in AFK:
        await event.reply(f"💤 Pengguna sedang AFK: {AFK[event.chat_id]}")
