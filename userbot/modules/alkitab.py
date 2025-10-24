# userbot/modules/alkitab.py
from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'^\.alkitab (.+)'))
async def alkitab(event):
    ayat = event.pattern_match.group(1)
    r = requests.get(f"https://alkitab-api.vercel.app/api/passage?passage={ayat}")
    if r.status_code != 200:
        await event.reply("❌ Ayat tidak ditemukan.")
        return
    data = r.json()
    teks = f"✝️ **{data['reference']}**\n\n{data['content']}"
    await event.reply(teks)
