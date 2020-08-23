"""
viewsets definitions
"""
from rest_framework import viewsets

from api.models import Agenda, Session
from api.serializers import AgendaSerializer, SessionSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    """
    Agenda Model Viewset (resource / controller)

    Args:
        viewsets (Agenda): as_view
    """

    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()


class SessionViewSet(viewsets.ModelViewSet):
    """
    Session Model Viewset (resource / controller)

    Args:
        viewsets (Session): as_view
    """

    serializer_class = SessionSerializer
    queryset = Session.objects.all()
