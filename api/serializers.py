"""
serializers definitions
"""
import requests


from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable, ValidationError
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from api.models import Agenda, Session, User, Vote

# constants
CPF_VALIDADE_URL = 'https://user-info.herokuapp.com/users/'

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
    cpf = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('id','name', 'cpf', 'email')

    def create(self, validated_data):
        if self.is_valid():
            try:
                cpf = str(self['cpf'].value).zfill(11)
                response = requests.get(CPF_VALIDADE_URL + cpf)

                if response.status_code in range(200, 299):
                    status = response.json()

                    if status['status'] != 'UNABLE_TO_VOTE':
                        user = User.objects.create(**validated_data)
                        return user
                    else:
                        raise NotAcceptable(detail="CPF unable to vote")

                else:
                    raise NotAcceptable(detail="CPF invalid")

            except requests.exceptions.RequestException:
                return ValidationError(detail='Validate CPF service unavailable', code=503)



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

            if now > session.begin or now < session.end:
                vote = Vote.objects.create(**validated_data)
                return vote
            else:
                raise NotAcceptable(detail="Vote outside of session time")
