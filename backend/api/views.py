from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import KenyaConflictData
from .serializers import IncidentSerializer

class IncidentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing incidents.
    """
    queryset = KenyaConflictData.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [AllowAny]  # Allow any user to access the API
    filterset_fields = {
        'event_date': ['exact', 'year', 'month', 'day', 'gte', 'lte'],
        'event_type': ['exact', 'icontains'],
        'admin1': ['exact', 'icontains'],
        'admin2': ['exact', 'icontains'],
        'fatalities': ['exact', 'gte', 'lte'],
    }