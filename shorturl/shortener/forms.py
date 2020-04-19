from django import forms

from .models import Link


class CreateLinkForm(forms.ModelForm):
    original_url = forms.CharField(label="URL to shorten")

    class Meta:
        model = Link
        fields = ("original_url",)
