#Non project imports
from django.utils.safestring import mark_safe
from django.forms import ModelForm

#Project imports
from .models import GuildProfileModel

class UpdateGuildProfileModelForm(ModelForm):
    class Meta():
        model = GuildProfileModel
        fields = ['GuildProfileBio', 'GuildProfileImage', 'GuildProfileHeader']
        labels = {
        'GuildProfileBio' : 'Describe the guild',
            'GuildProfileImage' : mark_safe('Profile image <br/> <small style="color: grey;">Recommended size <br /> 800px by 800px</small>'),
            'GuildProfileHeader' : mark_safe('Header image <br /> <small style="color: grey;">Recommended size <br /> 1900px by 700px </small>')

            }
