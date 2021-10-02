from django.db import models


class Genre(models.Model):
    """
    model for one genre
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
