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
SESSION = "1BVtsOL4Bu6volwhUyn_lCYUeCnindU0t4OrDqlv1yxiqXdwiIDvmROWphCrXjdoy8glzgWuZEZ-7Z3pjHqvm_XaFmWrj4TkHNAwOOhmgIDxDzyDFUGRDH727EV42VSPQerJpbyPBhKfUUnyWA-AqUWAHD_bt21czkUjJrsWse23TSHbHLgJQqnk-mALPtQjoSkVydPk3y1Db52Y3NH39aGpAPYOnPXUUcXIRWAiZId382MHX1Uw8uPgr4jhrqR9QEDVAzrZjWqe9c_n2vosAVuTeJIArN9w-DxT1UjTEGWPhx6E08B5yIpWoXpkGXmS2iOrhUGIlQOTTaSs34CZlOOqMCKVEuhY="
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
