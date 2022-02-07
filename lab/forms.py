from django import forms
from django.forms import ClearableFileInput
from lab.models import Lab


class LabCreationForm(forms.ModelForm):

    image = forms.ImageField(required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = Lab
        fields = ['title', 'content', 'image', 'file']
        # widgets = {
        #     'file': ClearableFileInput(attrs={'multiple': True})
        # }
