import mysql.connector


class Database:

    def __init__(self):
        self.setSelfConnection()

    def setSelfConnection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="TelegramSmartAssistant"
        )

    # def getAllMessages(self):
    #     try:
    #         mycursor = self.mydb.cursor()
    #     except:
    #         self.setSelfConnection()
    #         mycursor = self.mydb.cursor()

    #     mycursor.execute("SELECT * FROM forwardedmessages")

    #     myresult = mycursor.fetchall()

    #     return myresult

    # def getNewMessage(self, oldId):
    #     try:
    #         mycursor = self.mydb.cursor()
    #     except:
    #         self.setSelfConnection()
    #         mycursor = self.mydb.cursor()

    #     mycursor.execute(
    #         "SELECT * FROM forwardedmessages WHERE `originId`=%s" % (oldId))

    #     myresult = mycursor.fetchall()

    #     if len(myresult)==0:
    #         return -1

    #     return myresult[0][2]

    # def insertMessage(self, originId,newId):
    #     try:
    #         mycursor = self.mydb.cursor()
    #     except:
    #         self.setSelfConnection()
    #         mycursor = self.mydb.cursor()

    #     sql = "INSERT INTO forwardedmessages (originId, newId) VALUES (%s, %s)"
    #     val = (originId, newId)
    #     mycursor.execute(sql, val)

    #     myresult = mycursor.fetchall()
    #     self.mydb.commit()

    #     return myresult

    # def insertMessage(self, originId,newId):
    #     try:
    #         mycursor = self.mydb.cursor()
    #     except:
    #         self.setSelfConnection()
    #         mycursor = self.mydb.cursor()

    #     sql = "INSERT INTO forwardedmessages (originId, newId) VALUES (%s, %s)"
    #     val = (originId, newId)
    #     mycursor.execute(sql, val)

    #     myresult = mycursor.fetchall()
    #     self.mydb.commit()

    #     return myresult

    def findMany(self, query, val=None):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()

        if val is not None:
            mycursor.execute(query, val)
        else:
            mycursor.execute(query)

        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return []

        return myresult

    def findOne(self, query, values=None):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()

        if values is not None:
            mycursor.execute(query, values)
        else:
            mycursor.execute(query)

        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return None

        return myresult[0]

    def clearAllChatsList(self):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()
        query = "DELETE FROM `allchatslist`"
        mycursor.execute(query)

        myresult = mycursor.fetchall()
        self.mydb.commit()
        return 0

    def insertOne(self, query, values=None):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()

        if values is not None:
            mycursor.execute(query, values)
        else:
            mycursor.execute(query)

        myresult = mycursor.fetchall()
        self.mydb.commit()

        return myresult

    def Update(self, query):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()

        mycursor.execute(query)

        myresult = mycursor.fetchall()
        self.mydb.commit()

        return myresult

    def DeleteAt(self, tableName, id):
        try:
            mycursor = self.mydb.cursor()
        except:
            self.setSelfConnection()
            mycursor = self.mydb.cursor()

        query = "DELETE FROM `%s` WHERE `id` = %s" % (tableName, id)

        mycursor.execute(query)

        myresult = mycursor.fetchall()
        self.mydb.commit()

        return myresult
