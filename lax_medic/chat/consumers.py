# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login, logout, get_user
from django.contrib.auth import  authenticate
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.db.models import Q

from    django.contrib.auth.models  import  User, Group
from .models import SimpleTextMessage
 

def chat_views():
    return {
    'main':         main,
    'DATA_TYPES':   [
        'chat',
        'get_simple_messages',
    ],
}

async def connect(socket):
    pass

async def disconnect(socket):
    pass

async def main(socket, data):
    print('Chat enter')
    if data['type'] == 'get_simple_messages':
        await _send_simple_messages(socket, data)
        
    elif data['type'] == 'chat':
        await _chat(socket, data)
 
    else:
        await _send(socket, {
                'type': 'chat',
                'status': 'warning',
                'content': data['content']
        })

async def _send_simple_messages(socket, data):
    me      = socket.user
    friend  = await _get_user(data['content']['room'])
    messages= await _get_simple_messages(me, friend)
    print(friend)
    messages.reverse()
    await _send(socket, {
        'type': 'simple_messages',
        'content':{
            'room': data['content']['room'],
            'room_name': friend.username,
            'messages': messages
        }
    })

async def _chat(socket, data):
    print('chat')
    me      = socket.user
    to      = None
    message = data['content']['message']
    message_code= data['content']['message_code']
    if data['content']['room_type'] == 'simple':
        print(data)
        to  = await _get_user(data['content']['to'])

    created = await _create_message(
        me, to, data['content']['room_type'],
        data['content']['message_type'],
        message_code, message)
    if created:
        data_send =  {
            'type': 'chat',
            'content': {
                'type': 'message',
                'message': {               
                    'author'    : {
                        'id': me.pk,
                        'username': me.username
                    },
                    'to'        : {
                        'id': to.pk,
                        'username': to.username
                    },
                    'message_id': created.pk,
                    'is_received'  : created.is_received,
                    'is_seen'   : created.is_seen,
                    'message'   : created.message,
                    'date'      : str(created.date)
                }
            }
        }
        await _send(socket,data_send)
        await _send(socket, data_send, to=data['content']['to'])


async def _send(socket, data, to=None):   
    print(to)  
    if to is not None:
        print('transfert send ')
        await socket.channel_layer.group_send(
                str(to),
                {
                    'type': 'transfert',
                    'data': data
                }
            )
    else: 
        await socket.send(text_data=json.dumps(data))

@database_sync_to_async
def _get_simple_messages(me, friend):
    query = SimpleTextMessage.objects.filter(
            Q(author=me, to=friend) | 
            Q(author=friend, to=me)
        ).order_by('-date')[:7]
    print(query)
    return [{
        'author'    : {
            'id': message.author.pk,
            'username': message.author.username
        },
        'to'        : {
            'id': message.to.pk,
            'username': message.to.username
        },
        'message_id': message.pk,
        'is_received'  : message.is_received,
        'is_seen'   : message.is_seen,
        'message'   : message.message,
        'date'      : str(message.date)
    } for message in query]

@database_sync_to_async
def _create_message(me, to, room_type, message_type, message_code, message):
    create_message = None
    if room_type == 'simple':
        if message_type == 'text':
            create_message = SimpleTextMessage.objects.create(
            author=me,
            to=to,
            message=message,
            message_code=message_code)
    if create_message:    
        create_message.save()
    
    return create_message


@database_sync_to_async
def _set_message_received(personal, is_online):
    pass

@database_sync_to_async
def _get_user(pk):
    try:
        user = User.objects.get(pk=pk)
        return user
    except User.DoesNotExist:
        print('user n-existe pas !!!')
        return None