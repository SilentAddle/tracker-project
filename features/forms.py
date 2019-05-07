from django import forms
from .models import Features

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ('title', 'description', 'image')