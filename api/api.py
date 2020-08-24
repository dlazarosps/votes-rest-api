"""
viewsets definitions
"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Agenda, Session, User, Vote
from api.serializers import AgendaSerializer, SessionSerializer, UserSerializer, VoteSerializer

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

    @action(methods=['get'], detail=True)
    def count(self, request, pk=None):
        """
        Count Opinios of Session

        Return:
            Count of votes
        """
        votes_yes = Vote.objects.filter(session_id=pk, opinion=1).count()
        votes_no = Vote.objects.filter(session_id=pk, opinion=0).count()
        content = {'yes': votes_yes, 'no': votes_no}
        return Response(content)



class UserViewSet(viewsets.ModelViewSet):
    """
    User Model Viewset (resource / controller)

    Args:
        viewsets (User): as_view
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class VoteViewSet(viewsets.ModelViewSet):
    """
    Vote Model Viewset (resource / controller)

    Args:
        viewsets (Vote): as_view
    """

    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
