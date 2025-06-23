from django import forms
from .models import SaveGotham


class BatmanForm(forms.Form):
    name = forms.ModelChoiceField(queryset=SaveGotham.objects.all(), label='Candidate Name')