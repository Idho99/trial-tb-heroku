from django.shortcuts import render

# Create your views here.
def HomeUser (request):
    return render(request, 'user_app/home_user.html')

def LoginView (request):
    return render(request, 'user_app/login.html')

def LogoutView (request):
    return render(request, 'user_app/logut.html')

def RegistrationView (request):
    return render(request, 'user_app/registration.html')