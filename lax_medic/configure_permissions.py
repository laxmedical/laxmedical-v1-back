from    django.contrib.auth.models  import  User, Group, Permission
from django.db.utils import IntegrityError

group_list = [
        {
        'name': 'receptionniste',
        'permission_codes': [
            'add_fiche',
            'change_fiche',
            'view_fiche',
            'add_patient',
            'change_patient',
            'view_patient'
            ]
        },
        {
        'name': 'caissier',
        'permission_codes': [
            'change_fiche',
            'view_fiche'
            ]
        },
        {
        'name': 'medecin generaliste',
        'permission_codes': [
            'change_fiche',
            'view_fiche',
            'view_consultation',
            'add_consultation'
            ]
        }
    ]

def configure_permissions(type='init'):
    
    if type == 'init':
        for group in group_list:
            try: 
                g = Group.objects.create(name=group['name'])
                print(g)
                for permission_code in group['permission_codes']:
                    print('perm : '+ permission_code)
                    try: 
                        g.permissions.add(Permission.objects.get(codename=permission_code))
                    except Permission.DoesNotExist:
                        print('perm n\'exist pas')
                    
                g.save()
                
            except IntegrityError:
                print('audmg')
                g = Group.objects.get(name=group['name'])
                print(g)
                for permission_code in group['permission_codes']:
                    print('perm : '+ permission_code)
                    try: 
                        g.permissions.add(Permission.objects.get(codename=permission_code))
                    except Permission.DoesNotExist:
                        print('perm n\'exist pas')
                    
                g.save()
    