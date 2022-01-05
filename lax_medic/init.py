
from configure_permissions import configure_permissions
import app_settings
from django.contrib.auth.models  import  User

def init():
    try: 
        admin = User.objects.create_superuser(username='akelax', email='akelaxmerdi@gmail.com', password='derferger')
        admin.save()
    
        #quick init in developpement mode
        chrome = User.objects.create(username='chrome', email='chrome@gmail.com' , password='cocomeme')
        chrome.save()
        fire = User.objects.create(username='fire', email='fire@gmail.com' , password='fifirere')
        fire.save()
        opera = User.objects.create(username='opera', email='opera@gmail.com' , password='peperara')
        opera.save()
        
        configure_permissions()
          
    except :
        print('create users warning')     
                
    app_settings.init()
    
def migrate():
    configure_permissions()