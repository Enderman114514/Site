from django.urls import path

from . import views

app_name = 'e_site'
urlpatterns = [
    path('', views.home, name='index'),
]