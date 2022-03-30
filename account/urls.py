from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='form.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='form.html')),
    path('password_reset/',auth_views.PasswordResetConfirmView.as_view(template_name='confirm_reset.html')),
    path('change_password/', auth_views.PasswordChangeDoneView.as_view(template_name='confirm_change.html')),

]

