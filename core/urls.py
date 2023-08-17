from django.urls import path

from core.views import ContactView, home

app_name = 'core'

urlpatterns = [
    path('contato/', ContactView.as_view(), name='contact'),
    path('', home, name='home'),
]
