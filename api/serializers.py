from rest_framework import serializers

from api.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('title')