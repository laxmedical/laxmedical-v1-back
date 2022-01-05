# chat/consumers.py
import json
from channels.db import database_sync_to_async
from django.db.models import Q

from django.core.paginator import Paginator

from users.models import Patient
from main.models import Fiche

from django.contrib.auth.models  import  User

def caisse_views():
    return {
    'main':         main,
    'DATA_TYPES':   [
        'create_patient',
        'create_fiche',
        'get_patients',
        'get_patient_profile',
        'get_seach_patients_list'
    ],
}

async def connect(socket):
    pass

async def disconnect(socket):
    pass

async def main(socket, data):
    print('reception enter')
    if data['type'] == 'create_patient':
        await _handle_create_patient(socket, data)
        
    if data['type'] == 'create_fiche':
        await _handle_create_fiche(socket, data)
        
    elif data['type'] == 'get_patients':
        await _handle_get_patients(socket, data)

    elif data['type'] == 'get_patient_profile':
        await _handle_patient_profile(socket, data)
        
    elif data['type'] == 'get_seach_patients_list':
        await _handle_seach_patients_list(socket, data)

    else:
        await _send(socket, {
                'type': 'reception',
                'status': 'warning',
                'content': data['content']
        })

async def _send(socket, data):        
    await socket.send(text_data=json.dumps(data))

async def _handle_create_patient(socket, data):
    print('_handle_create_patient')
    patient = await _create_patient(socket.user, data['content'])
    print(patient.birth_date)
    
    await _send(socket, {
        'type': 'create_patient',
        'status': 'success',
        'content': {
            'patient_id': patient.pk
        }
    })
    
async def _handle_create_fiche(socket, data):
    print('_handle_create_fiche')
    fiche = await _create_fiche(socket.user, data['content'])
    
    if fiche:
        print('send response fiche')
        await _send(socket, {
        'type': 'create_fiche',
        'status': 'success',
        'content': {
            'fiche_id': fiche
        }
        })
    else:
        await _send(socket, {
        'type': 'create_fiche',
        'status': 'warning',
        'content': {
            'fiche_id': None
        }
        })
        

async def _handle_patient_profile(socket, data):
    print('_handle_patient_profile')
    
    try: 
        patient_id =  int(data['content']['patient_id'])
                    
        patient_profile = await _get_patient_profile(patient_id)
    
        await _send(socket, {
        'type': 'patient_profile',
        'content': patient_profile
        })
    except ValueError:
        await _send(socket, {
        'type': 'patient_profile',
        'status': 'error',
        'content': {
            'error': 'ValueError'
        }
        })
        
async def _handle_get_patients(socket, data):
    print('_handle_get_patients')
    
    try: 
        page_index =  int(data['content']['page_index'])
                    
        patient_profile = await _get_patients(page_index)
    
        await _send(socket, {
        'type': 'patient_list',
        'status': '200',
        'content': patient_profile
        })
    except ValueError:
        await _send(socket, {
        'type': 'patient_list',
        'status': 'error',
        'content': {
            'error': 'ValueError'
        }
        })
   
async def _handle_seach_patients_list(socket, data):
    print('_handle_seach_patients_list')
                
    seach_patients_list = await _get_seach_patients_list()
    
    await _send(socket, {
        'type': 'seach_patients_list',
        'status': '200',
        'content': seach_patients_list
    })
 

@database_sync_to_async
def _create_patient(editor, data):
    username = data['username']
    first_name = data['first_name']
    last_name = data['last_name']
    sex = data['sex']
    birth_date = data['birth_date']
    adress = data['adress']

    patient = Patient.objects.create(
        editor=editor, 
        username=username, 
        first_name=first_name, 
        last_name=last_name, 
        sex=sex,
        birth_date=birth_date,
        adress=adress
    )
    
    patient.save()
    
    return patient

@database_sync_to_async
def _create_fiche(editor, data):
    poid = data['poid']
    temperature = data['temperature']
    description = data['description']
    
    try:
        patient = Patient.objects.get(pk=data['patient'])
        
        fiche = Fiche.objects.create(
        editor=editor, 
        patient=patient, 
        poid=poid, 
        temperature=temperature, 
        description=description
        )
        return fiche.pk
        
    except User.DoesNotExist:
        print('user n-existe pas !!!')
        return None
    
    patient.save()
    
    return patient

@database_sync_to_async
def _get_patient_profile(patient_id):
    patient = Patient.objects.get(pk=patient_id)
    fiches  = patient.fiches.all()
    return {
        'id': patient.pk,
        'username': patient.username,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'sex': patient.sex,
        'birth_date': str(patient.birth_date),
        'adress': patient.adress,
        'fiches': [
            {
                'id': fiche.pk,
                'editor': {
                    'username': fiche.editor.username,
                    'first_name': fiche.editor.first_name,
                    'last_name': fiche.editor.last_name,
                },
                'temperature': fiche.temperature,
                'poid': fiche.poid,
                'description': fiche.description,
                'created_date': str(fiche.date)
            } for fiche in fiches
        ]
    }
    
@database_sync_to_async
def _get_patients(page_index):
    all_patients = Patient.objects.all().order_by('-id')
    pages = Paginator(all_patients, 5)
    current_page = pages.page(page_index)
    patients = current_page.object_list

    return {
        'patients':[
            {
                'id': patient.pk,
                'username': patient.username,
                'first_name': patient.first_name,
                'last_name': patient.last_name,
                'sex': patient.sex,
                'birth_date': str(patient.birth_date),
                'adress': patient.adress,
                'fiches': patient.fiches.count()
            } for patient in all_patients
        ],
        'pagination': {
            'num_pages': pages.num_pages,
            'current_page_index': page_index,
        }
    }
    
@database_sync_to_async
def _get_seach_patients_list():
    all_patients = Patient.objects.all().order_by('-id')

    return {
        'patients':[
            {
               'name': patient.username + ' ' +
                        patient.first_name + ' ' +
                        patient.last_name,
                'id': patient.pk
            }for patient in all_patients
        ]
    }