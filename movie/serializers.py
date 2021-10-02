from rest_framework import serializers
from . import models
from genre.serializers import GenreSerializer
from django.forms.models import model_to_dict


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer class for Movie
    """

    class Meta:
        model = models.Movie
        fields = (
            'name',
            'genre',
            'created_date',
            'director',
            'summery',
            'get_review_rate',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(models.Genre.objects.get(movie=instance))
        representation['genre'] = model_to_dict(models.Genre.objects.get(movie=instance))
        representation['review_rate'] = representation.pop('get_review_rate')
        return representation