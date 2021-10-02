from django.db import models
from genre.models import Genre


class Movie(models.Model):
    """
    model for one movie
    """
    name = models.CharField(max_length=50, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    created_date = models.DateField()
    director = models.CharField(max_length=50)
    summery = models.TextField()

    def __str__(self):
        return self.name
