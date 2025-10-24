# userbot/modules/animasi.py
from telethon import events
import asyncio

@events.register(events.NewMessage(pattern=r'^\.hack$'))
async def animasi_hack(event):
    anim = [
        "💻 Mengakses data...",
        "🔍 Memindai jaringan...",
        "📡 Menembus firewall...",
        "⚙️ Mengambil token...",
        "💣 BOOM! Sistem berhasil diambil alih!"
    ]
    for i in anim:
        await event.edit(i)
        await asyncio.sleep(1.5)
