
from    django  import forms

class ConnexionForm(forms.Form):
    username    =   forms.CharField(label="Prenom",max_length=20,)
    password    =   forms.CharField(label="Nom",max_length=20)