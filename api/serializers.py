"""
serializers definitions
"""
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from rest_framework.validators import UniqueTogetherValidator

from api.models import Agenda, Session, User, Vote

class AgendaSerializer(serializers.ModelSerializer):
    """
    Agenda Serializer

    Args:
        serializers (Agenda): Serialization of Agenda Entities
    """

    class Meta:
        model = Agenda
        fields = ('id','title', 'description')


class SessionSerializer(serializers.ModelSerializer):
    """
    Session Serializer

    Args:
        serializers (Session): Serialization of Session Entities
    """

    class Meta:
        model = Session
        fields = ('id','begin', 'end', 'agenda')


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer

    Args:
        serializers (User): Serialization of User Entities
    """

    class Meta:
        model = User
        fields = ('id','name', 'cpf', 'email')


class VoteSerializer(serializers.ModelSerializer):
    """
    Vote Serializer

    Args:
        serializers (Vote): Serialization of Vote Entities
    """

    class Meta:
        model = Vote
        fields = ('id','opinion', 'session', 'user')
        validators = [
            UniqueTogetherValidator(
                queryset=Vote.objects.all(),
                fields=['session', 'user']
            )
        ]

    def create(self, validated_data):
        if self.is_valid():
            session = Session.objects.get(id=int(self['session'].value))

            now = timezone.now()

            if now < session.begin or now > session.end:
                raise NotAcceptable(detail="Vote outside of session time")
            else:
                vote = Vote.objects.create(**validated_data)
                return vote
