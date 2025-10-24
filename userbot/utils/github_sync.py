# userbot/utils/github_sync.py
from bot.config.github import github_update
import json

def sync_users_to_github():
    with open("userbot/database/users.json", "r") as f:
        content = f.read()
    github_update("userbot/database/users.json", content, "sync user data")
