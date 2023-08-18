from django.urls import path

from core.views import ContactView, HomeView

app_name = 'core'

urlpatterns = [
    path('contato/', ContactView.as_view(), name='contact'),
    path('', HomeView.as_view(), name='home'),
]
