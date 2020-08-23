"""
registration of models
"""
from django.contrib import admin
from api.models import Agenda, Session

# Register your models here.
admin.site.register(Agenda)
admin.site.register(Session)
