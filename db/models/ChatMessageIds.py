import json
from typing import List
from ..Database import Database


class ChatMessageIds:

    def __init__(self, db: Database, id=0, originChatId=0, destinationChatId=0, originId=0, newId=0):
        self.db = db
        self.id = id
        self.originChatId = originChatId
        self.destinationChatId = destinationChatId
        self.originId = originId
        self.newId = newId

    def getLastMessageId(self, originChatId, destinationChatId, originId):
        sqlQuery = "SELECT `newId` FROM chatmessageids WHERE `originChatId`=%s And`destinationChatId`=%s And`originId`=%s"
        vals = (originChatId, destinationChatId, originId)
        idRow = self.db.findMany(sqlQuery, vals)

        if(len(idRow) != 0):
            return idRow[len(idRow)-1][0]

        return -1

    def SaveToDatabase(self):
        sqlQuery = "INSERT INTO `chatmessageids` (originChatId, destinationChatId,originId,newId) VALUES (%s, %s, %s, %s)"
        val = (self.originChatId, self.destinationChatId,
               self.originId, self.newId)
        self.db.insertOne(sqlQuery, val)
