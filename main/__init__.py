#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22918031
API_HASH = "a5c57d945a1a1214edecb04cc18c6e70"
BOT_TOKEN = "6892668789:AAEFpw7g5HC0sMjh5nx8JlAEcSk_00I-9_4"
SESSION = "BQFds48AHG5eG0VUF63B5hU4rgRoE1i26Yc4dwYofgFvIZ8exgrmJ7Dedl7ahsg3mM8jjluTZUBkH5rOX51IUGtsvKWvfK9k02dgTtEI9-KwaixRJQx6qzBGvUsBgo6JFF-nWA0xr73OUZKb7Ykf-MocL2RYNo6tbYhXsqkKzl6aVdj6GoRKMGIhAYimbVfarCSOJqbKPLoPQBctukZBWuqjULp7CnzhtwN1mjg8CRZrbNVVzR3dCnyvaQ4er1TYPGqQ4NJCIhFhgjxXuVDKY9Yf14ZkvA0pgDztPR-_fAIUvkaXgS2uHYkyeOxoq5r-ugX0rCy4IysOCbMyCZGjeFAnG60C-wAAAABWdGtvAA"
FORCESUB = "Callmee99i"
AUTH = 1450470255

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
