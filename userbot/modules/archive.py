# userbot/modules/archive.py
from telethon import events

@events.register(events.NewMessage(pattern=r'^\.save (.+)'))
async def save(event):
    text = event.pattern_match.group(1)
    with open("saved.txt", "a") as f:
        f.write(text + "\n")
    await event.reply("✅ Tersimpan ke saved.txt")

@events.register(events.NewMessage(pattern=r'^\.list$'))
async def list_saved(event):
    try:
        with open("saved.txt", "r") as f:
            data = f.read()
        await event.reply(f"📁 **Saved Notes:**\n\n{data}")
    except FileNotFoundError:
        await event.reply("📂 Belum ada data tersimpan.")
