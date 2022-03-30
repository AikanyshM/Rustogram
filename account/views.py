from django.shortcuts import render
from .models import User
from django.views.generic import CreateView

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'