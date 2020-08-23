"""
models definitions
"""
from django.db import models

# Create your models here.
class Agenda(models.Model):
    """
    Agenda Model

    Args:
        models (Agenda): Agenda Entity ORM definition

    Returns:
        Agenda: Agenda Obj
    """

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title
