from db.models.Settings import Settings
from db.models.PreviusDataForwarder import PreviusDataForwarder
from telethon.sync import TelegramClient, events
import json
from db.Database import Database
from agents.messageForwarderGuy import MessageForwarderGuy
from tools.MessageForwarder import MessageForwarder
import requests
import time
import threading
import asyncio

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 396609
api_hash = 'ce67f98e67793f11f1fa8e1bb8811ae6'


client = TelegramClient('User', api_id, api_hash)
# client = TelegramClient('user313', api_id, api_hash)
db = Database()
messageForwarderGuy = MessageForwarderGuy(db)
settings = Settings(db, client)
previusDataForwarder = PreviusDataForwarder(db, client)


async def main():
   #  client.send_message('me', 'Hello, myself!')
    # print(await client.download_profile_photo('me'))
    #    @client.on(events.NewMessage(pattern='(?i).*Hello'))

    @client.on(events.NewMessage())
    async def handler(event):
        await messageForwarderGuy.newMessage(client, event.message)

        # await MessageForwarder(db, client, messageForwarderGuy, _ToChatId)
        # query = {'data':event.message.raw_text}
        # response = requests.post('http://localhost:8000/signal360Parser', data=query)
        # print("new message")

    async def Cycle():
        while(True):
            await asyncio.sleep(5)
            db.setSelfConnection()
            if client.is_connected() is False:
                continue
            await settings.cycleFetch()
            await previusDataForwarder.cycleFetch()
            # print('cycle')

    # asyncio.run(Cycle,)
    # await GetDialogs()
    # await GetLastMessages(_FromChatId, 20)

    asyncio.gather(
        client.run_until_disconnected(),
        await Cycle(),
    )
    # await client.run_until_disconnected()


def Resetttt():
    time.sleep(5)
    print('slept')


Resetttt()


# while(True):
#     settings.cycleUpdate()
#     print('cycle')
#     time.sleep(10)


# t1 = threading.Thread(target=Cycle, args=[])
# t1.start()

with client:
    client.loop.run_until_complete(main())
