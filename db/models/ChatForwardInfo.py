from io import StringIO
import json
from typing import List
from ..Database import Database


class ChatForwardInfo:

    def __init__(self, db: Database, id=0, originChatId=0, destinationChatId=0, filterByWord=[], autoBuyParserLink=None):
        self.db = db
        self.id = id
        self.originChatId = originChatId
        self.destinationChatId = destinationChatId
        self.filterByWord = filterByWord
        self.autoBuyParserLink = autoBuyParserLink

    def getInfoWithId(db, id):
        sqlQuery = "SELECT * FROM chatforwardinfo WHERE `id`=%s" % (
            id)
        allForwardingRows = db.findOne(sqlQuery)
        info = ChatForwardInfo(
            db, allForwardingRows[0], allForwardingRows[1], allForwardingRows[2], json.loads(allForwardingRows[3]), allForwardingRows[4])

        return info

    def getAllRowsWithOriginChatId(self, originChatId):
        sqlQuery = "SELECT * FROM chatforwardinfo WHERE `originChatId`=%s" % (
            originChatId)
        allForwardingRows = self.db.findMany(sqlQuery)

        infos = [ChatForwardInfo(self.db)]
        for i in allForwardingRows:
            info = ChatForwardInfo(
                self.db, i[0], i[1], i[2], json.loads(i[3]), i[4])
            infos.append(info)

        infos.remove(infos[0])
        return infos
