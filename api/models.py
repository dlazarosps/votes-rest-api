"""
models definitions
"""
from datetime import timedelta
from django.core.validators import RegexValidator
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


class Session(models.Model):
    """
    Session Model

    Args:
        models (Session): Session Entity ORM definition

    Returns:
        Session: Session Obj
    """

    begin = models.DateTimeField(null=False)
    duration = models.DurationField(null=False, default=timedelta(minutes=1))
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.id)


class User(models.Model):
    """
    User Model

    Args:
        models (User): User Entity ORM definition

    Returns:
        User: User Obj
    """

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=254, null=False)
    cpf = models.IntegerField(validators=[RegexValidator(r'^\d{1,11}$')])

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """
    Vote Model

    Args:
        models (Vote): Vote Entity ORM definition

    Returns:
        Vote: Vote Obj
    """

    opinion = models.BooleanField(null=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.id)
