# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login, logout, get_user
from django.contrib.auth import  authenticate
from asgiref.sync import sync_to_async

#   Import applicaions view
from users.consumers    import users_views
from chat.consumers     import chat_views
from workplace.consumers import workplace_views

APP_VIEWS = [
    users_views(),
    chat_views(),
    workplace_views()
]

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat'
        self.user = self.scope["user"]
        self.personal = None

        await self.accept()
        await self.call_apps(run='connect')

    async def disconnect(self, close_code):
        await self.call_apps(run='disconnect')

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        await self.call_apps(data, call_one_app=True)

    async def transfert(self, event):
        print('transfert')
        await self.send(text_data=json.dumps(event['data']))

    async def call_apps(self, data={}, run='main', call_one_app=False):
        for view in APP_VIEWS:
            if run in view:
                if run == 'connect' or run == 'disconnect':
                    await view[run](self)
                    if call_one_app:
                        break
                elif run == 'main' and data['type'] in view['DATA_TYPES']:
                    await view[run](self, data)
                    if call_one_app:
                        break
                else:
                    continue