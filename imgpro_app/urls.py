from django.urls import path
from imgpro_app import views

app_name = 'imgpro_app'

urlpatterns = [
    path('', views.HomeImg, name='homeImg'),
    path('imgpro/', views.ImgPro, name='imgPro'),
    path('home/', views.NewHomeImg, name='homeImg2'),
]