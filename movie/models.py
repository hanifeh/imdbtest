from statistics import mean

from django.db import models
from genre.models import Genre


class Movie(models.Model):
    """
    model for one movie
    """
    name = models.CharField(max_length=50, unique=True)
    genre = models.ManyToManyField(Genre)
    created_date = models.DateField()
    director = models.CharField(max_length=50)
    summery = models.TextField()

    def __str__(self):
        return self.name

    def get_review_rate(self):
        rates = [review.rate for review in self.review_set.all()]
        if rates:
            return mean(rates)
        else:
            return 'no review'

    get_review_rate.short_description = 'review rate'
