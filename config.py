import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Aapki Details Yahan Add Kar Di Hain
API_ID = int(getenv("API_ID", "34135757"))
API_HASH = getenv("API_HASH", "d3d5548fe0d98eb1fb793c2c37c9e5c8")
BOT_TOKEN = getenv("BOT_TOKEN", "8541688649:AAHLhJLdVk9lT6uOsD-u4qfCY0wmM2RUiaY")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://misssqn:VICTOR01@cluster0.3otqmso.mongodb.net/?appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

# Logger aur Owner ID
LOGGER_ID = int(getenv("LOGGER_ID", "-1008581811595"))
OWNER_ID = int(getenv("OWNER_ID", "8581811595"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Upstream Repo (Aapki apni repo ka link bhi daal sakte hain yahan)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMMUKASH/DOREAMON-_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support Links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/radhesupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+PKYLDIEYiTljMzMx")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# String Session (Ise Render ke Env Var mein daalna mat bhulna)
STRING1 = getenv("STRING_SESSION", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images (Aapki Image Update Kar Di Hai)
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/fc78336c4402d1f53d696-95139de88bc561d55a.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/fc78336c4402d1f53d696-95139de88bc561d55a.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong.")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong.")
