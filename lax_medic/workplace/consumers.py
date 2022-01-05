# chat/consumers.py
import json
from channels.db import database_sync_to_async
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Patient, Fiche, Consultation
from django.contrib.auth.models  import  User


def workplace_views():
    return {
    'main':         main,
    'DATA_TYPES':   [
        'create_patient',
        'create_fiche',
        'get_fiche',
        'get_patients',
        'get_patient_profile',
        'get_seach_patients_list',
        'create_consultation',
        'get_consultation',
    ],
}

async def connect(socket):
    pass

async def disconnect(socket):
    pass

async def main(socket, data):
    print('workplace enter')
    if data['type'] == 'create_patient':
        await _handle_create_patient(socket, data)
        
    elif data['type'] == 'create_fiche':
        await _handle_create_fiche(socket, data)
        
    elif data['type'] == 'get_fiche':
        await _handle_get_fiche(socket, data)
        
    elif data['type'] == 'get_patients':
        await _handle_get_patients(socket, data)

    elif data['type'] == 'get_patient_profile':
        await _handle_patient_profile(socket, data)
        
    elif data['type'] == 'get_seach_patients_list':
        await _handle_seach_patients_list(socket, data)
        
    elif data['type'] == 'create_consultation':
        await _handle_create_consultation(socket, data)
        
    elif data['type'] == 'get_consultation':
        await _handle_get_consultation(socket, data)

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
           
async def _handle_get_fiche(socket, data):
    print('_handle_get_fiche')
    fiche = await _get_fiche(data['content']['fiche_id'])
    
    if fiche:
        print('send response fiche')
        await _send(socket, {
        'type': 'fiche',
        'status': 'success',
        'content': fiche
        })
    else:
        await _send(socket, {
        'type': 'create_fiche',
        'status': '404',
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
 
async def _handle_create_consultation(socket, data):
    print('_handle_create_consultation')
                
    consultation_id = await _create_consultation(socket.user, data['content'])
    
    await _send(socket, {
        'type': 'create_consultation',
        'status': 'success',
        'content': {
            'consultation_id': consultation_id
            }
    })
    
async def _handle_get_consultation(socket, data):
    print('_handle_get_consultation')
                
    consultation = await _get_consultations(data['content']['fiche_id'])
    
    await _send(socket, {
        'type': 'consultations',
        'status': '202',
        'content': consultation
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
    
@database_sync_to_async
def _get_fiche(fiche_id):
    
    try:
        fiche = Fiche.objects.get(pk=fiche_id)
        
        return {
            'id': fiche.pk,
            'editor': {
                'username': fiche.editor.username,
            },
            'patient': {
                'username': fiche.patient.username
            },
            'created_date': str(fiche.date),
            'poid': fiche.poid,
            'temperature': fiche.temperature,
            'description': fiche.description
        }
        
    except Fiche.DoesNotExist:
        print('user n-existe pas !!!')
        return None

@database_sync_to_async
def _get_patient_profile(patient_id):
    patient = Patient.objects.get(pk=patient_id)
    fiches  = patient.fiches.all().order_by('-date')
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
        ],
        'editor': {
        'username': patient.editor.username,
        'first_name': patient.editor.first_name,
        'last_name': patient.editor.last_name,
        }
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
        
@database_sync_to_async
def _create_consultation(editor, data):
    try:
        fiche = Fiche.objects.get(pk=data['fiche_id'])
        consultation = Consultation.objects.create(
            editor=editor,
            fiche=fiche, 
            note=data['note'], 
            conclusion=data['conclusion'])
        return consultation.pk

    except Fiche.DoesNotExist:
        print('user n-existe pas !!!')
        return None
    
@database_sync_to_async
def _get_consultations(fiche_id):
    
    def get_editor(consultation):
        try:
            return {
                'username': consultation.editor.username,
                'first_name': consultation.editor.first_name
                }
    
        except :
            return None
    
    try:
        fiche = Fiche.objects.get(pk=fiche_id)
        
        consultations = fiche.consultations.all().order_by('-date')
        return [
        {
            'id': consultation.pk,
            'editor': get_editor(consultation),
            'note': consultation.note,
            'conclusion': consultation.conclusion,
            'date': str(consultation.date)
        } for consultation in consultations
        ]

    except Fiche.DoesNotExist:
        print('Fiche n-existe pas !!!')
        return None
    
    except :
        print('user n-existe pas !!!')
        return [
        {
            'id': consultation.pk,
            'editor': None,
            'note': consultation.note,
            'conclusion': consultation.conclusion,
            'date': str(consultation.date)
        } for consultation in consultations
        ]
    