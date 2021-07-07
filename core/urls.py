from django.urls import path

from .views import contact, home

app_name = 'core'

urlpatterns = [
    path('contato/', contact, name='contact'),
    path('', home, name='home'),
]
