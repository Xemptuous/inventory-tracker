from django import forms
from .models import Host

class AddHost(forms.Form):
    name = forms.CharField(label="Name", max_length=255, required=True)
    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )

class AddSubHost(forms.Form):
    name = forms.CharField(label="Name", max_length=255, required=True)
    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    # host = forms.ModelChoiceField(queryset=Host.objects.filter().order_by('name'), required=True)
