from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("home/signup/", SignUpView.as_view(name="signup.html"), name="FDP"),
]