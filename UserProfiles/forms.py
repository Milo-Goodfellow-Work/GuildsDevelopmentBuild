#Non project imports
from django.utils.safestring import mark_safe
from django.forms import ModelForm

#Project imports
from .models import UserProfileModel

class UpdateUserProfileForm(ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ['UserProfileBio', 'UserProfileWebsite', 'UserProfileImage', 'UserProfileHeader']
        labels = {
            'UserProfileBio' : 'Describe yourself',
            'UserProfileWebsite' : mark_safe('Personal link'),
            'UserProfileImage' : mark_safe('Profile image <br/> <small style="color: grey;">Recommended size <br /> 800px by 800px</small>'),
            'UserProfileHeader' : mark_safe('Header image <br /> <small style="color: grey;">Recommended size <br /> 1900px by 700px </small>')

            }
