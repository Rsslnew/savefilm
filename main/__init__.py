#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("22879626", default=None, cast=int)
API_HASH = config("a95117f1a742d53ca1abc520b9b29356", default=None)
BOT_TOKEN = config("6491172782:AAEOEh3Hlba27Ikq9drh6NDZYtsUOsjvdws", default=None)
SESSION = config("BQFdHYoAgcqC0VHHb1XfXK9CmW6z9UP_Fo6-zIZecO8zkBOFNDdQYqHui5MysZUfBsg4SgsL5ADMeuuTmJfgprrBOh_lq2kEBMW-AjvL4qSJ0hHLHjyDp1x9JOJlnuOmeglrcXUKHIGpImv-QSuWYz5s9F6pzfoXZyicJfE5t05__EOyL3BK2nKZjzi6jHQ_dDK7lFr_O3ibwaHkSC5bjfut88VNuZUlVEHykhhZ9eLUaEdFKsP2wc1g835cvj1THRAEQBEDBH1qb7S6U8Gv1pm5Xij9m28SzW60WldCLtOP1UfO_jI8MQdj7gShCFCr7AqLfhRV1hcCqBNiylXBufsX4ggSqQAAAAGEE_BvAA", default=None)
FORCESUB = config("-1001980570314", default=None)
AUTH = config("6510866543", default=None, cast=int)

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
