
from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
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
        )
