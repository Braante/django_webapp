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
    return render(request, 'moreAboutPlayers.html', {'playerData': playerData})

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
    players_response = requests.get(f"https://www.balldontlie.io/api/v1/players?team_ids[]={teamId}")
    playerData = players_response.json()
    return render(request, 'moreAboutTeams.html', {'teamData': teamData, 'playerData': playerData})

def games(request):
    page = request.GET.get('page', 1)
    response = f"https://www.balldontlie.io/api/v1/games?page={page}"
    rep = requests.get(response)
    gamesData = rep.json()
    return render(request, 'games.html', {'gamesData': gamesData})

def gameData(request, gameId):
    response = f"https://www.balldontlie.io/api/v1/games/{gameId}"
    rep = requests.get(response)
    gameData = rep.json()
    return render(request, 'moreAboutGames.html', {'gameData': gameData})