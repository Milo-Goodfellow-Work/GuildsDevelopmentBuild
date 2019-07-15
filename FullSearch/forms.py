#Non project imports
from django import forms

#Project imports

class SearchForm(forms.Form):
    Search = forms.CharField()
