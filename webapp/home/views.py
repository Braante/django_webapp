from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import requests

# Create your views here.

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def players_list(request):
    page = request.GET.get('page', 1)
    response = f"https://www.balldontlie.io/api/v1/players?page={page}"
    rep = requests.get(response)
    players_data = rep.json()
    return render(request, 'home.html', {'players_data': players_data})

def players_infos(request, player_id):
    response = f"https://www.balldontlie.io/api/v1/players/{player_id}"
    rep = requests.get(response)
    player_data = rep.json()
    return render(request, 'players_infos.html', {'player_data': player_data})

