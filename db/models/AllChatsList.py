import json
from typing import List
from ..Database import Database
from telethon.sync import TelegramClient


class AllChatsList:

    def __init__(self, db: Database, client: TelegramClient):
        self.db = db
        self.client = client

    async def GetDialogs(self):
        if self.client.is_connected() is False:
            return
        try:
            dialogs = await self.client.get_dialogs()
        except:
            dialogs = []
        array = []
        for item in dialogs:
            array.append({
                "id": item.id,
                "name": item.name
            })

        # jsonData = json.dumps(array)
        print('got the chats')
        return array

    def insertAllChats(self, data):
        query = "INSERT INTO `allchatslist` (`chatName`,`chatId`) VALUES "
        for i in data:
            query += "('%s',%s)" % (i['name'], i['id'])+","
        query = query[:-1]

        self.db.insertOne(query)

    async def resetAllChatsList(self):
        self.db.clearAllChatsList()
        allDialogs = await self.GetDialogs()
        self.insertAllChats(allDialogs)
