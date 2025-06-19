
# Create your models here.
from django.db import models
from accounts.models import CustomUser

class SchoolLocation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='joined_schools')
    lat = models.FloatField()
    lon = models.FloatField()
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} joined ({self.lat}, {self.lon})"
