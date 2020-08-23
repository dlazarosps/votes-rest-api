from rest_framework import viewsets

from api.models import Agenda
from api.serializers import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()
    