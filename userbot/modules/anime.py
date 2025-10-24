# userbot/modules/anime.py
from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'^\.anime (.+)'))
async def anime(event):
    query = event.pattern_match.group(1)
    r = requests.get(f"https://api.jikan.moe/v4/anime?q={query}&limit=1")
    if r.status_code != 200:
        await event.reply("❌ Anime tidak ditemukan.")
        return
    data = r.json()["data"][0]
    teks = f"🎌 **{data['title']}**\n"
    teks += f"📅 Tahun: {data['year']}\n⭐ Rating: {data['score']}\n"
    teks += f"📺 Episode: {data['episodes']}\n📖 {data['synopsis'][:300]}..."
    await event.reply(teks)
