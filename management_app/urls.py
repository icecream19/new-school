from django.urls import path
from .views import home

app_name = 'management_app'


urlpatterns = [
    path('', home, name='home-page')
]