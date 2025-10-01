# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24712525"))
API_HASH = getenv("API_HASH", "648708266952f0d981f5f23d97c32992")
BOT_TOKEN = getenv("BOT_TOKEN", "8304937637:AAFeSBm59kqQZTmBOhV8MB4ug4z31RzUuQA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6334323103").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
