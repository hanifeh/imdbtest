from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from genre import serializers, models


class GenreViewSetAPI(ModelViewSet):
    """
    View Set for genre
    """
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()
