from django.db import models
from django.utils import timezone

# Create your models here.

class SaveGotham(models.Model):
    WEAPON_CHOICE = [
        ("BR", "Batarang"),
        ("GG", "Grapnel Gun"),
        ("BM", "Batmobile"),
        ("BP", "Batplane"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="save-gotham/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=WEAPON_CHOICE)