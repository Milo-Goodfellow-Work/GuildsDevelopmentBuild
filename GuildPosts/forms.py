#Non project imports
from django.utils.safestring import mark_safe
from django.forms import ModelForm

#Project imports
from .models import PostModel

class GuildPostModelForm(ModelForm):
    class Meta():
        model = PostModel
        fields = ['PostBody']
        labels = {
            'PostBody':mark_safe('What is going on? <br/> <small style="color: grey;">500 character limit</small>'),


        }
