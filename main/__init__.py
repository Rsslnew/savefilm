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
SESSION = "BQEHOHgAjBh1J8kk2gyHffZNCJT3jKEcN7y1L2zadq9GLGD7zJqe0Sn9uvsKXuLqSlxtEbYaEDncLwP3xbnwpaBXY0lSSgYQKIyZF3MR1IYvIYIw2jmDr4kEm1NultXx5qVqcBtLq7dzjt0kc7KN1q_PC8OT5qWqERWayAuYE9e4DMsvJ71VZXO-Xi8ro7vq9uguhzmVHIS3Fgixf0CAVeFkrO3PMs-0mL6Wlt2SFu3sB1Tz0Z2K2FHRUlq9-SH0JGNT_6m2ZpX8iH_Sekrb-gi0tX1RPjbNCuRdkCeoBUrMRZXCjdDFVjnUPZvI-QFyAlR_ZTWPPQocSqlqdCFgt8djakxWkQAAAABoPaz5AA"
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
