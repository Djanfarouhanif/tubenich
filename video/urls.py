from django.http import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]