# userbot/modules/alquran.py
from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'^\.quran (.+)'))
async def quran(event):
    ayat = event.pattern_match.group(1)
    url = f"https://api.quran.gading.dev/surah/{ayat}"
    r = requests.get(url)
    if r.status_code != 200:
        await event.reply("❌ Surah tidak ditemukan.")
        return
    data = r.json()["data"]
    teks = f"📖 **{data['name']['transliteration']['id']}**\n"
    teks += f"Artinya: {data['name']['translation']['id']}\n"
    teks += f"Jumlah ayat: {data['numberOfVerses']}\n"
    teks += f"Audio: {data['preBismillah']['text']['arabic'] if data.get('preBismillah') else 'Tidak ada'}"
    await event.reply(teks)
