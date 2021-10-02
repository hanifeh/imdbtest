
from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Serializer class for genre
    """

    class Meta:
        model = models.Genre
        fields = (
            'name',
        )
