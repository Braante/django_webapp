"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from home import views
from home.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.players, name="players"),
    path('teams/', views.teams, name="teams"),
    path('games/', views.games, name="games"),
    path('<int:playerId>/', views.playersData, name="moreAboutPlayers"),
    path('teams/<int:teamId>/', views.teamsData, name="moreAboutTeams"),
    path('games/<int:gameId>/', views.gameData, name="moreAboutGames"),
    path("home/", include("django.contrib.auth.urls")),
    path("home/signup/", SignUpView.as_view(), name="signup"),
]
