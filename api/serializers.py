"""
serializers definitions
"""
from rest_framework import serializers

from api.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    """
    Agenda Serializer

    Args:
        serializers (Agenda): Serialization of Agenda Entities
    """

    class Meta:
        model = Agenda
        fields = ('id','title')
