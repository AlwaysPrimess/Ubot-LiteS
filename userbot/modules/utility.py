# userbot/modules/utility.py
from telethon import events
import datetime, time

@events.register(events.NewMessage(pattern=r'^\.time$'))
async def time_now(event):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await event.reply(f"⏰ Sekarang jam: `{now}`")

@events.register(events.NewMessage(pattern=r'^\.date$'))
async def date_today(event):
    today = datetime.datetime.now().strftime("%d %B %Y")
    await event.reply(f"📅 Tanggal: `{today}`")
