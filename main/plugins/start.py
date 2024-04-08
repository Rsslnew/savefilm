#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("𝘬𝘪𝘳𝘪𝘮 𝘴𝘢𝘺𝘢 𝘨𝘢𝘮𝘣𝘢𝘳 𝘢𝘵𝘢𝘶 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 𝘺𝘢𝘯𝘨 𝘮𝘢𝘶 𝘥𝘪 𝘤𝘰𝘱𝘺 𝘧𝘪𝘭𝘮 𝘯𝘺𝘢 𝘢𝘵𝘢𝘶 𝘷𝘪𝘥𝘦𝘰 𝘢𝘱𝘢 𝘴𝘢𝘫𝘢 𝘶𝘯𝘵𝘶𝘬 𝘵𝘩𝘶𝘮𝘣𝘯𝘢𝘪𝘭 𝘴𝘦𝘣𝘢𝘨𝘢𝘪 𝘣𝘢𝘭𝘢𝘴𝘢𝘯 𝘱𝘦𝘴𝘢𝘯 𝘪𝘯𝘪.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Tʜᴜᴍʙɴᴀɪʟ ʙᴇʀʜᴀsɪʟ ᴅɪsɪᴍᴘᴀɴ!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs!')
    except Exception:
        await event.edit("ᴛɪᴅᴀᴋ ᴀᴅᴀ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ᴅɪsɪᴍᴘᴀɴ.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "𝘕𝘦𝘳𝘰 𝘋𝘢𝘱𝘢𝘵 𝘊𝘭𝘰𝘯𝘪𝘯𝘨 𝘛𝘢𝘶𝘵𝘢𝘯 𝘱𝘦𝘴𝘢𝘯 𝘢𝘱𝘢 𝘱𝘶𝘯 𝘶𝘯𝘵𝘶𝘬 𝘥𝘪𝘬𝘭𝘰𝘯𝘪𝘯𝘨 𝘥𝘪 𝘴𝘪𝘯𝘪, 𝘜𝘯𝘵𝘶𝘬 𝘱𝘦𝘴𝘢𝘯 𝘴𝘢𝘭𝘶𝘳𝘢𝘯 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 , 𝘬𝘪𝘳𝘪𝘮 𝘵𝘢𝘶𝘵𝘢𝘯 𝘶𝘯𝘥𝘢𝘯𝘨𝘢𝘯 𝘵𝘦𝘳𝘭𝘦𝘣𝘪𝘩 𝘥𝘢𝘩𝘶𝘭𝘶.\n\n**SUPPORT:** @neropublik"
    await start_srb(event, text)
    
