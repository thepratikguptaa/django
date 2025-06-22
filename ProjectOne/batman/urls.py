from django.urls import path
from . import views

# localhost:8000/batman/
urlpatterns = [
    path('', views.batman, name='batman'),
]