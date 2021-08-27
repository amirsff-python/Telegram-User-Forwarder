from telethon.sync import TelegramClient, events
import json
from db.Database import Database
from db.models.ChatMessageIds import ChatMessageIds
import telethon


async def MessageForwarder(db: Database, client: TelegramClient, message: telethon.tl.patched.Message, _ToChatId: int):
    sentMessage = None
    if message.forward is not None:
        sentMessage = await client.forward_messages(_ToChatId, message)
    else:
        if(message.is_reply):
            lastMessage = ChatMessageIds(db).getLastMessageId(
                message.chat_id, _ToChatId, message.reply_to_msg_id)
            if lastMessage != -1:
                sentMessage = await client.send_message(_ToChatId, message, reply_to=lastMessage)
        if sentMessage is None:
            sentMessage = await client.send_message(_ToChatId, message)

        # saving the old id and new id to database
        # db.insertMessage(message.id, sentMessage.id)
        chatMessageId = ChatMessageIds(
            db, originChatId=message.chat_id, destinationChatId=_ToChatId, originId=message.id, newId=sentMessage.id)
        chatMessageId.SaveToDatabase()
