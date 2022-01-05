from workplace.models import Consultation
from workplace.models import WorkplaceSetting

def init():
    print('no app settings')
    #quick init in developpement mode
    consultation_settions = WorkplaceSetting.objects.create(type='consultion', data={
        'structure': [
            {'title': 'Plainte pricipale'},
            {'title': 'Anamnèse'}],
        'owner': {
            'name': 'Bob',
            'other_pets': [{
                'name': 'Fishy',
            }],
        },
    })
    