from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from movie import serializers, models


class MovieViewSetAPI(ModelViewSet):
    """
    View Set for movie
    """
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'created_date', 'director']
    ordering_fields = ['name', 'created_date', 'director']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
