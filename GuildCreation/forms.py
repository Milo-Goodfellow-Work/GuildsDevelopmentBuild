#Non project imports
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

#Project imports
from .models import GuildModel

class CreateGuildForm(ModelForm):
    class Meta():
        model = GuildModel
        fields = ['GuildName', 'GuildSize']
        labels = {
                'GuildName': 'Name your Guild!',
                'GuildSize': mark_safe('How many people get to join? <br/> <small style="color: grey;">Max of five</small>'),

        }
