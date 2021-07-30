import mysql.connector


class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="telegeamforwardedmessages"
        )

    def getAllMessages(self):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT * FROM forwardedmessages")

        myresult = mycursor.fetchall()

        return myresult

    def getNewMessage(self, oldId):
        mycursor = self.mydb.cursor()

        mycursor.execute(
            "SELECT * FROM forwardedmessages WHERE `originId`=%s" % (oldId))

        myresult = mycursor.fetchall()
        
        if len(myresult)==0:
            return -1

        return myresult[0][2]
        
    def insertMessage(self, originId,newId):
        mycursor = self.mydb.cursor()
        
        sql = "INSERT INTO forwardedmessages (originId, newId) VALUES (%s, %s)"
        val = (originId, newId)
        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()
        self.mydb.commit()
        
        return myresult

