from django.db import models


class Sport(models.Model):
    country = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.sport
