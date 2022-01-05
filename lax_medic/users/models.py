from    django.db import models
from    django.contrib.auth.models  import  User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'personals/{instance.user.id}/avatars/{filename}'


class Personal(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)   # la liaison onToOn vers le modèle User
    avatar   =   models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    title    = models.CharField(max_length=100)
    is_online= models.BooleanField(default=False)

    def __unicode__(self):
        return  u"Profil de {0}".format(self.user.username)
    
    def __str__(self):
        return  u"Profil de {0}".format(self.user.username)
    