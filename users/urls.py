from django.conf.urls import url
from .views import *

app_name = 'users'

urlpatterns = [
    url(r'^create/?$', RegistrationAPIView.as_view()),
    url(r'^login/?$', LoginAPIView.as_view()),

]
