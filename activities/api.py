from rest_framework import viewsets

from .models import Activity, AResponse
from .serializers import ActivitySerializer, AResSerializer

class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class AResViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = AResponse.objects.all()
    serializer_class = AResSerializer