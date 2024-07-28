from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_video', views.loader, name='loader'),
]