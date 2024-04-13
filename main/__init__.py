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
BOT_TOKEN = "6712604457:AAFGqieLmNQKOw-yd1s_iJV61nb7bA8N4Cs"
SESSION = "BQEHOHgALte0GFmARHIAG2Ge5kGROz3HqfImZdzXEr8xnar_oMr4PzX3YLmyK9ERMCfjFv04xMz7od504BWq7ccW3xqCEvMK6qsb3Cl_YQ-KwG5vB96BA04KQ3ZcDRntVbVVER4nBkHZ2WJ-6z8-AE3lj3C4e-KAUBBJ47D3AVAzaYosnXIG7kTLlv-WYVFXEkN2amXcbBT3_EVx--XVDPGf1DHURgdsgCb7pyXQLtHNq5x8gLZIvT25T3Gcbp1UDOAeWjQey_ffuWQqszfhWbTUFSYfuHbH3g7rvlYzCMNdLeK6LiuwqwH0T9U0UEgI_QJyn-DpJL_VtnGjLMPMDD35Y5cjQQAAAABoPaz5AA"
FORCESUB = "avvvfuckk"
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
