from    django.urls     import  path
from    .               import  views


urlpatterns =   [
    # les urls de l'application home
    path('', views.home, name = 'home'),
    path('connexion/', views.connect_user, name = 'connexion'),
    path('deconnection/',   views.disconnect_user, name = 'deconnection'),
    path('workplace/', views.workplace, name = 'workplace'),
    path('lax_medic/', views.lax_medic, name = 'lax_medic'),
]