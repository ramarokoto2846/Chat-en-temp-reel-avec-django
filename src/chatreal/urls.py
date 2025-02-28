from .views import Index, Connexion, Inscriptions, Plateform, Deconnexion, Discussion
from django.urls import path

urlpatterns = [
    path('', Index, name="index"),
    path('connexion/', Connexion, name="connexion"),
    path('inscriptions/', Inscriptions, name="inscription"),
    path('plateform/', Plateform, name="plateform"),
    path('deconnexion/', Deconnexion, name="deconnexion"),

    path('discussion/<str:uid>/', Discussion, name='discussion')
]