from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

#one to many relationship model
class CandidateReviews(models.Model):
    RATING_OPTIONS = [
        ("1/5", "1/5: Not Worthy"),
        ("2/5", "2/5: Poor"),
        ("3/5", "3/5: Average"),
        ("4/5", "4/5: Good"),
        ("5/5", "5/5: Best"),
    ]
    candidate = models.ForeignKey(SaveGotham, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100, choices=RATING_OPTIONS)
    comment = models.TextField(default="No comment provided.")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.candidate.name}'