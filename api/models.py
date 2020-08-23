"""
models definitions
"""
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

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
    description = models.TextField(null=True)

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
    end = models.DateTimeField(null=False, default=timezone.now()+timezone.timedelta(minutes=1))
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        id_str = str(self.id)
        agenda_str = str(self.agenda)
        begin_str = self.begin.strftime('%d/%m/%Y %H:%M')
        end_str = self.end.strftime('%d/%m/%Y %H:%M')

        return  "Agenda {} - Sessão {} - de {} até {}"\
            .format(agenda_str, id_str, begin_str, end_str)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['session', 'user'], name='unique vote for session user')
        ]

    def __str__(self):
        return str(self.id)
