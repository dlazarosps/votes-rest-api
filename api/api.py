"""
viewsets definitions
"""
from rest_framework import viewsets

from api.models import Agenda
from api.serializers import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    """
    Agenda Model Viewset (resource / controller)

    Args:
        viewsets (Agenda): as_view
    """

    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()
