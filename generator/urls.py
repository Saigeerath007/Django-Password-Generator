from django.urls import path
from . import views

app_name= 'gen'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<str:invalid_url>/', views.error)
]
