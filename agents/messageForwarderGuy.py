
from db.models.ChatForwardInfo import ChatForwardInfo
from db.Database import Database
from telethon.client.telegramclient import TelegramClient
from tools.MessageForwarder import MessageForwarder
import telethon
import requests


class MessageForwarderGuy:
    def __init__(self, db: Database):
        self.db = db

    async def newMessage(self, client: TelegramClient, message: telethon.tl.patched.Message):
        dbObject = ChatForwardInfo(self.db)

        forwardingChannelObjects = dbObject.getAllRowsWithOriginChatId(
            message.chat_id)

        for obj in forwardingChannelObjects:
            if (len(obj.filterByWord) == 0) or any(word in message.raw_text for word in obj.filterByWord):
                await MessageForwarder(self.db, client, message,
                                       obj.destinationChatId)

                if obj.autoBuyParserLink is not None:
                    sendingData = {'data': message.raw_text}
                    response = requests.post(
                        obj.autoBuyParserLink, data=sendingData)
                print("new message")
