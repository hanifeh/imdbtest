from rest_framework import serializers
from . import models
from genre.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer class for Movie
    """
    # genre = GenreSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = (
            'name',
            'genre',
            'created_date',
            'director',
            'summery',
        )
