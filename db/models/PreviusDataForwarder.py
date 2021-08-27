from db.models.ChatForwardInfo import ChatForwardInfo
import json
from typing import List
from ..Database import Database
from telethon.sync import TelegramClient
from tools.MessageForwarder import MessageForwarder


class PreviusDataForwarder:

    def __init__(self, db: Database, client: TelegramClient):
        self.db = db
        self.client = client

    async def cycleFetch(self):
        allData = self.db.findMany("SELECT * FROM `previousforwarderdata`")

        await self.cycleUpdate(allData)

    async def GetLastMessages(self, chat, count, toChatId):
        messages = await self.client.get_messages(chat, count)
        messages.reverse()
        for item in messages:
            if item.message is not None:
                await MessageForwarder(self.db, self.client, item, toChatId)

        print("Last messages Sent Successfully")

    async def cycleUpdate(self, allData):
        for data in allData:
            prevForwarderDataId = data[0]
            chatForwardInfoId = data[1]
            count = data[2]
            cfi = ChatForwardInfo.getInfoWithId(self.db, chatForwardInfoId)
            await self.GetLastMessages(cfi.originChatId, count, cfi.destinationChatId)
            self.db.DeleteAt("previousforwarderdata", prevForwarderDataId)
