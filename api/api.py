"""
viewsets definitions
"""
from rest_framework import viewsets

from api.models import Agenda, Session, User
from api.serializers import AgendaSerializer, SessionSerializer, UserSerializer

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


class UserViewSet(viewsets.ModelViewSet):
    """
    User Model Viewset (resource / controller)

    Args:
        viewsets (User): as_view
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
