from django.urls import path
from .views import home, admission, determining

app_name = 'management_app'


urlpatterns = [
    path('', home, name='home-page'),
    path('admission/', determining, name='determining-page'),
    path('admission/student/', admission, name='admission-page'),
]