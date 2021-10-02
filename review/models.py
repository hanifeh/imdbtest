from django.db import models
from movie.models import Movie
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """
    model for one movie
    """
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    writer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    body = models.TextField()

    class Meta:
        unique_together = [['movie', 'writer']]

    def __str__(self):
        return f"{self.writer} {self.movie}"
