from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('', views.HomeUser, name='user_home'),
    path('login/', views.LoginView, name='user_login'),
    path('logout/', views.LogoutView, name='user_logout'),
    path('registration/', views.RegistrationView, name='registration')
]