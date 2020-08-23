"""
serializers definitions
"""
from rest_framework import serializers

from api.models import Agenda, Session

class AgendaSerializer(serializers.ModelSerializer):
    """
    Agenda Serializer

    Args:
        serializers (Agenda): Serialization of Agenda Entities
    """

    class Meta:
        model = Agenda
        fields = ('id','title')


class SessionSerializer(serializers.ModelSerializer):
    """
    Session Serializer

    Args:
        serializers (Session): Serialization of Session Entities
    """

    class Meta:
        model = Session
        fields = ('id','begin', 'duration')
