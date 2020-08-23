"""
registration of models
"""
from django.contrib import admin
from api.models import Agenda, Session, User, Vote

# Register your models here.
admin.site.register(Agenda)
admin.site.register(Session)
admin.site.register(User)
admin.site.register(Vote)
