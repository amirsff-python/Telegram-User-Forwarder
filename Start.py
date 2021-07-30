from telethon.sync import TelegramClient, events
import json
from db.Database import Database
from tools.MessageForwarder import MessageForwarder

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 396609
api_hash = 'ce67f98e67793f11f1fa8e1bb8811ae6'

_FromChatId = -1001192056014
_ToChatId = -1001577013460
# _FromChatId = -1001591080248  # TEST
# _ToChatId = -1001515950052  # TEST


# async def ssss():
#     print('asd')

# with TelegramClient('name', api_id, api_hash) as client:
#     client.send_message('me', 'Hello, myself!')
#     print(client.download_profile_photo('me'))
# #    @client.on(events.NewMessage(pattern='(?i).*Hello'))
#     @client.on(events.NewMessage())
#     async def handler(event):
#         #   await event.reply('Hey!')
#       #   print("new mwssage")
#       a=27

#     async def asdf():
#        print('asdddd');
#     asdf()
#     client.run_until_disconnected()


client = TelegramClient('user', api_id, api_hash)
# client = TelegramClient('userTEST', api_id, api_hash)
db = Database()


async def main():
   #  client.send_message('me', 'Hello, myself!')
    # print(await client.download_profile_photo('me'))
    #    @client.on(events.NewMessage(pattern='(?i).*Hello'))

    @client.on(events.NewMessage())
    async def handler(event):
        #   await event.reply('Hey!')
        if event.chat_id == _FromChatId:
            await MessageForwarder(db, client, event.message, _ToChatId)
            print("new message")

    async def GetDialogs():
        dialogs = await client.get_dialogs()
        array = []
        for item in dialogs:
            array.append({
                "id": item.id,
                "name": item.name
            })

        jsonData = json.dumps(array)
        print('got the chats')

    async def GetLastMessages(chat, count):
        messages = await client.get_messages(chat, count)
        messages.reverse()
        for item in messages:
            if item.message is not None:
                await MessageForwarder(db, client, item, _ToChatId)

        print("Last messages Sent Successfully")

    # await GetDialogs()
    # await GetLastMessages(_FromChatId, 150)

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
