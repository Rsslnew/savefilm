#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20247370
API_HASH = "813309fab8cd9fce260ce7269e543bdb"
BOT_TOKEN = "6877654187:AAFeeqTBTvxOvLtYBLAY6VEF9YFMb1JacJs"
SESSION = "1BVtsOL4BuwQzpaerJXfJMVc00ZkAvN6TIWhhXXbXM_bbTGf1xGsL5KQFSrEOG0vNCz3kSGFUNnFTdOHu9pkmYLH0ZEu4iRjMopRTaykXtXYmpC8ZamD-Rik7nUf8fPeT8qGc_S5ROSIjJNf7NLOsu9X3VQIC-7POqn84LNdQOy0nJsFcWHWGUSfyC9JEjddtOjaAf1v_4jYm19VwP2Q2BvvtJUHFge6fjHlR4fSzALnskzA-QhL4DeF1xKfnEo5_qmlicxBRX74C37Yub3ThSFYSucfYFE8iRwI8C8fUZeNriHLh8KgtRBRP88yECDiOX3-3mfXgKRvrr2pg86Dj794Jnked1Mw="
FORCESUB = "gafamousy"
AUTH = 1748872441

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
