from telethon.sync import TelegramClient, events
import json
from db.Database import Database


async def MessageForwarder(db: Database, client: TelegramClient, message, _ToChatId: int):
    sentMessage = None
    if message.forward is not None:
        sentMessage = await client.forward_messages(_ToChatId, message)
    else:
        if(message.is_reply):
            lastMessage = db.getNewMessage(message.reply_to_msg_id)
            if lastMessage != -1:
                sentMessage = await client.send_message(_ToChatId, message, reply_to=lastMessage)
        if sentMessage is None:
            sentMessage = await client.send_message(_ToChatId, message)
        
        # saving the old id and new id to database
        db.insertMessage(message.id,sentMessage.id)
        abcd=1234
