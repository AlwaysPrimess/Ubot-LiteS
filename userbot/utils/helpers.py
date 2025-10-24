# userbot/utils/helpers.py
import datetime

def format_uptime(seconds: int):
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs}h:{mins}m:{sec}s"

def get_const_status(user_name: str):
    uptime = "25m:17s"
    return f"{user_name}/{uptime}"
