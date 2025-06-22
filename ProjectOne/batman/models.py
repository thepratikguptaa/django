from django.db import models
from django.utils import timezone

# Create your models here.

class SaveGotham(models.Model):
    WEAPON_CHOICE = [
        ("Batarang", "Batarang"),
        ("Grapnel Gun", "Grapnel Gun"),
        ("Batmobile", "Batmobile"),
        ("Batplane", "Batplane"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="save-gotham/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=WEAPON_CHOICE)
    description = models.TextField(default="No description provided.")

    def __str__(self):
        return self.name # return the name of the save