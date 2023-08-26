from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
import requests

# Create your views here.

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def players(request):
    page = request.GET.get('page', 1)
    response = f"https://www.balldontlie.io/api/v1/players?page={page}"
    rep = requests.get(response)
    playersData = rep.json()
    return render(request, 'home.html', {'playersData': playersData})

def playersData(request, playerId):
    response = f"https://www.balldontlie.io/api/v1/players/{playerId}"
    rep = requests.get(response)
    playerData = rep.json()
    return render(request, 'home.html', {'playerData': playerData})

def teams(request):
    page = request.GET.get('page', 1)
    response = f"https://www.balldontlie.io/api/v1/teams?page={page}"
    rep = requests.get(response)
    teamsData = rep.json()
    return render(request, 'teams.html', {'teamsData': teamsData})

def teamsData(request, teamId):
    response = f"https://www.balldontlie.io/api/v1/teams/{teamId}"
    rep = requests.get(response)
    teamData = rep.json()
    return render(request, 'teams.html', {'teamData': teamData})