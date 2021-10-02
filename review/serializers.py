from rest_framework import serializers
from . import models
from movie.serializers import MovieSerializer


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer class for Review
    """
    # movie = serializers.CharField(source='movie.name')

    class Meta:
        model = models.Review
        fields = (
            'movie',
            'created_date',
            'rate',
            'body',
        )
