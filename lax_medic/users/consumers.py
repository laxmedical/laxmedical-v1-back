# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login, logout, get_user
from django.contrib.auth import  authenticate
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.db.models import Q

from .models import Personal
from chat.models import SimpleTextMessage

def users_views():
    return {
    'connect':      connect,
    'disconnect':   disconnect,
    'main':         main,
    'DATA_TYPES': [
            'init',
            'login',
            'logout',
            'get_personals_list'
        ],
    }
async def connect(socket):
    print('call connect from users')
    personal = await _get_personal(socket.user)
    if personal is not None:
        await _set_personal_online(personal ,True)
        socket.personal = personal
        print(socket.user)

        await _handle_personal_group(socket, connected=True)


    
    #await _init(socket)

async def disconnect(socket):
    print('call disconnect from users')
        # Leave room group
    if socket.personal is not None:
        print(socket.user.pk)
        await _set_personal_online(socket.personal, False)

    await _handle_personal_group(socket, connected=False)
    
    await _notified_connection(socket)


async def main(socket, data):
    if data['type'] == 'init':
        await _init(socket)

    elif data['type'] == 'login':
        await _login(socket, data)
        
    elif data['type'] == 'logout':
        await _logout(socket)
        
    elif data['type'] == 'get_personals_list':
        await _send_personals_list(socket)
 
    else:
        await _init(socket)

async def _init(socket):
    personal = socket.personal
    if personal is not None:
        p = await sync_to_async(socket.user.get_all_permissions)()
        pers = [str(per) for per in p]

        avatar =  None
        
        try: 
            avatar =  personal.avatar.url
        except ValueError:
            print('error ava')
            avatar =  None
        
        await socket.send(text_data=json.dumps(
            {
                'type': 'init',
                'content': {
                    'is_auth': True,
                    'user': {
                        'id': socket.user.pk,
                        'username': socket.user.username,
                        'first_name': socket.user.first_name,
                        'last_name': socket.user.last_name,
                        'title': personal.title,
                        'avatar': avatar,
                        'permisions': pers
                    }
                }
            }
        ))

        await _notified_connection(socket)
    else:
        await socket.send(text_data=json.dumps(
            {
                'type': 'init',
                'content': {
                    'is_auth': False
                }
            }
        ))

async def _login(socket, data):
    u = await get_user(socket.scope)
    username, password = data['content']['username'], data['content']['password']

    user        = await sync_to_async(authenticate)(username=username,password=password)

    personal = await _get_personal(user)
    if personal is not None:
        print(personal.is_online)
        print('login')
        await login(socket.scope, user)
        socket.user = await get_user(socket.scope)
        await _set_personal_online(personal ,True)
        socket.personal = personal
        
        await _handle_personal_group(socket, connected=True)

        p = await sync_to_async(socket.user.get_all_permissions)()
        pers = [str(per) for per in p]
        
        avatar =  None
        
        try: 
            avatar =  personal.avatar.url
        except ValueError:
            avatar =  None
        
        await _send(socket,{
                'type': 'login',
                'status': 'success',
                'content': {
                    'is_auth': True,
                    'user': {
                        'id': socket.user.pk,
                        'username': socket.user.username,
                        'first_name': socket.user.first_name,
                        'last_name': socket.user.last_name,
                        'title': personal.title,
                        'avatar': avatar,
                        'permisions': pers
                    }
                }
            })

    elif user is not None:        
        await _send(socket,{
                'type': 'login',
                'status': 'not allowed',
                'content': {
                '   is_auth': False,
                    'user': {
                        'id': None,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    }
                }
            })

    else:
        await _send(socket,{
            'type': 'login',
            'status': '404',
            'content': {
                'is_auth': False,
                'user': None
            }
        })

async def _logout(socket):
    if socket.personal:
        
        await _set_personal_online(socket.personal, False)

        logout(socket.scope)
        
        await socket.send(text_data=json.dumps(
            {
                'type': 'logout',
                'status': 'success',
            }
        ))
        await _handle_personal_group(socket, connected=False)
        await _notified_connection(socket)
    else:
        await socket.send(text_data=json.dumps(
            {
                'type': 'logout',
                'status': 'warning',
            }
        ))

async def _send_personals_list(socket):
    if socket.personal is not None:
        personals_list = await _get_personals(self_id=socket.personal.pk, me=socket.user)
        print('get_online_personals_list')
        await _send(socket, {
            'type': 'personals_list',
            'content': personals_list 
        })


async def _handle_personal_group(socket, connected: bool):
    print('_handle_personal_group')
    if connected:
        print('add group')
        await socket.channel_layer.group_add(
            str(socket.user.pk),
            socket.channel_name
        )
    else:
        await socket.channel_layer.group_discard(
            str(socket.user.pk),
            socket.channel_name
        )

    await socket.channel_layer.group_add(
        'connected_users',
        socket.channel_name
    )

async def _notified_connection(socket):
    online_users = await _get_online_users()
    connected_users =  {
        'type': 'connected_users',
        'content': online_users
    }
    await _send(socket, connected_users, to='connected_users')

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
def _get_online_users():
    print('get online users ')
    return [{               
            'id'      : personal.user.id,
            'username': personal.user.username
            } for personal in Personal.objects.filter(is_online=True)
        ]


@database_sync_to_async
def _get_personal(user):
    try:
        if user is not None and not user.is_anonymous:
            personal = Personal.objects.get(user=user)
            return personal
    except Personal.DoesNotExist:
        print('personnel ne correspond pas ')
        return None

@database_sync_to_async
def _get_personals(self_id, me):
    #if personal is not None:
    query_set = Personal.objects.all()
    personals_list =[]
    
    for personal in query_set:
        if personal.pk is not self_id:
            avatar =  None
        
            try: 
                avatar =  personal.avatar.url
            except ValueError:
                print('error ava')
                avatar =  None
                
                
            message_list = SimpleTextMessage.objects.filter(
            Q(author=me, to=personal.user) | 
            Q(author=personal.user, to=me)
            ).order_by('-date')
            
            last_message = ' '
            if message_list.count() != 0:
                last_message = message_list[0].message
            personals_list.append(
            {
            'id':           personal.user.pk,
            'username':     personal.user.username,
            'first_name':   personal.user.first_name,
            'last_name':    personal.user.last_name,
            'last_message': last_message,
            'avatar':       avatar,
            'is_online':    personal.is_online
            } )
        
    return personals_list


@database_sync_to_async
def _set_personal_online(personal, is_online):
    personal.is_online = is_online
    personal.save()
