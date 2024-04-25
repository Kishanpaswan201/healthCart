
from django.urls import path
from .views import *

urlpatterns = [
    path("",CustomerSignUpView.as_view()),
    path("login",CustomerLogin.as_view(), name="log-in"),
]