from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/0dfacd1c8fc60d6040a60.mp4")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/35c5739ae6e6bbcc696a4.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/pglpnti_ki_duniya")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Octave_support")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1225278379").split()))

