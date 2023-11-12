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
SESSION = "1BVtsOGwBuzoaUMm-nsjcaQzQ1SviH4eSkqb_98G1Vn8vLWqE3fAStc6vLCijkwBpV5iG5GgGIzz_o5hcwuln4VIDXw0xVKpHXu_F4f9Ax5HuqzpZ4dU_FnwUkEsFpP9LHDUUZ7EFIlGGK7Pp7YYQuS2JTMZRmwvkz08UWR4oE2kF4gW9O8jn8DyLS2qZ1FpAdIFTYdDu4vyp-PsiYQ3KFf-cCKEGvYWdlmhoPTfF6fDMhjzeg18pXOHsd3gSXBTL01fg3K2HxafgntXiA54U9ZwuX2DkmtCUR5v-DtnSNbY3m69ZuEWHgvMNmd24eGvmIxib4g4Civ6edI9-SUv8jE9bSDwP5QM="
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
