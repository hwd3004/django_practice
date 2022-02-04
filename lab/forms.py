from django.forms import ModelForm

from lab.models import Lab


class LabCreationForm(ModelForm):
    class Meta:
        model = Lab
        fields = ['title', 'author', 'image', 'file', 'content']
