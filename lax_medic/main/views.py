from    django.shortcuts    import  render, redirect
from    django.urls         import  reverse
from    .form               import  ConnexionForm
from    django.contrib.auth import  authenticate, login, logout
from    django.contrib.auth.decorators  import  login_required

# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def lax_medic(request):
    return render(request, 'main/index.html')


@login_required(login_url='/')
def workplace(request):
    return redirect('http://localhost:3000')

def connect_user(request):
    clien = request.method
    error   =   False
    if request.method=="POST":
        form    =   ConnexionForm(request.POST)
        if form.is_valid():
            username    =   form.cleaned_data["username"]# Nousrécupérons le nom d'utilisateur
            password    =   form.cleaned_data["password"]# ... et le mot de passe
            user        =   authenticate(username=username,password=password) #Nous vérifions si les données sont correctes
            if user:# Si l'objet renvoyé n'est pas None
                login(request,user)# nous connectons l'utilisateur
                return redirect(reverse(connect_user))
            else:#sinon une erreur sera affichée
                    error   =   True
    else:
        form    =   ConnexionForm()
            
    return render(request,'main/login.html',locals())

def disconnect_user(request):
    logout(request)
    return redirect(reverse(connect_user))