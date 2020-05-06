from django import forms
from .models import FileModel
from .models import ImageModel


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('title', 'fileup')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('imgTitle', 'image')
