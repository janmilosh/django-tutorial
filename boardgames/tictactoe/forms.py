from django.db import models
from django.forms import ModelForm
from tictactoe.models import Invitation


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ['from_user']