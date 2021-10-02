from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import serializers, models
from rest_framework.viewsets import ModelViewSet


class ReviewViewSetAPI(ModelViewSet):
    """
    API for Review
    """
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Review.objects.all()

    def get_queryset(self):
        """
        list of all review for admin or list of own review for user
        """
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs.all()
        return qs.filter(writer=self.request.user)

    def perform_create(self, serializer):
        """
        add request user to serializer
        """
        serializer.save(writer=self.request.user)
