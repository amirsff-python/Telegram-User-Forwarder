from db.models.AllChatsList import AllChatsList
from io import StringIO
import json
from typing import List
from ..Database import Database
from telethon.sync import TelegramClient


class Settings:

    def __init__(self, db: Database, client: TelegramClient):
        self.db = db
        self.UpdateAllChatsList = 1
        self.client = client

    async def cycleFetch(self):
        setting = self.db.findOne("SELECT * FROM `settings`")
        self.UpdateAllChatsList = setting[0]
        await self.cycleUpdate()

    async def cycleUpdate(self):
        if self.UpdateAllChatsList > 0:
            cfi = AllChatsList(self.db, self.client)
            await cfi.resetAllChatsList(self.UpdateAllChatsList % 2 == 0)
            query = "UPDATE `settings` SET `UpdateAllChatsList`=%s" % (
                self.UpdateAllChatsList - 1)
            self.db.Update(query)
