from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.index, name='index'),
    path('get_video', views.loader, name='loader'),
    path('video', views.video , name= 'video'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]