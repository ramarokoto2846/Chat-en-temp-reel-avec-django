import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation.template import context_re

from chatreal.forms import CustomUserCreationForm
from chatreal.models import CustomUser
from chatAppDjango import settings


# Create your views here.
def Inscriptions(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def Connexion(request):
    if request.method == 'POST':

        nomuser = request.POST['nomuser']
        motdepass = request.POST['motdepass']

        user = authenticate(request, username=nomuser, password=motdepass)
        if user is not None:
            login(request, user)
            return redirect('plateform')
        else:
            context = {
                'em': "Nom d'utilisateur ou mot de passe incorect.",
            }
            return render(request, 'connexion.html', context)

    return render(request, 'connexion.html')


@login_required
def Deconnexion(request):
    logout(request)
    return redirect('index')


def Index(request):
    return render(request, 'index.html')


@login_required
def Plateform(request):
    user = request.user
    users = CustomUser.objects.exclude(id=user.id)

    contexte = {
        "user": user,
        "users": users,
    }

    return render(request, 'plateform.html', contexte)


def Discussion(request, id):
    amie = get_object_or_404(CustomUser, id=id)
    return render(request, 'discussion.html', {"amie":amie})