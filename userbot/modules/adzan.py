# userbot/modules/adzan.py
from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'^\.adzan (.+)'))
async def adzan(event):
    kota = event.pattern_match.group(1)
    r = requests.get(f"https://api.myquran.com/v2/sholat/jadwal/{kota}/today")
    if r.status_code != 200:
        await event.reply("❌ Gagal mengambil jadwal sholat.")
        return
    data = r.json()
    jadwal = data["data"]["jadwal"]
    teks = f"🕌 **Jadwal Sholat - {data['data']['lokasi']}**\n\n"
    for key, val in jadwal.items():
        if key != "tanggal":
            teks += f"• **{key.title()}**: `{val}`\n"
    await event.reply(teks)
