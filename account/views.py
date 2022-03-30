from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout


class RegisterView(CreateView):
    model = User
    template_name = 'form.html'
    fields = ('username', 'password')
    success_url = reverse_lazy('post_list')

def auth_user(request):
    user = request.user
    print(user)

    return HttpResponse(user.username)


def check_user(request):
    if request.method == "GET":
        return render(request, 'form.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username, password = password)
        user.save()

        return HttpResponse(f'Пользователь {user.username} создан')

def change_password(request):
    if request.method == "GET":
        return render(request, 'form.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return HttpResponse(f'У пользователя {user.username} пароль изменен')

def login_view(request):
    if request.method == "GET":
        return render(request, 'form.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if request.user.is_authenticated:
            return render(request, 'auth.html')
        else:
            return HttpResponse("Попробуйте еще раз!")

def logout_view(request):
    logout(request)
    return HttpResponse("До свидания")



    