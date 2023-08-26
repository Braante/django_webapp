from django.urls import path

from .views import SignUpView
from .import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('player/', views.players, name="players"),
    path('teams/', views.teams, name="teams"),
]