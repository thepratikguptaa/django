from django.urls import path
from . import views

# localhost:8000/batman/
urlpatterns = [
    path('', views.batman, name='batman'),
    path('<int:batman_id>/', views.weapon_details, name='weapon_details'),
]