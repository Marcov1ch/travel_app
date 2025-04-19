from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_visited = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.country}, {self.city} ({self.date_visited})"
