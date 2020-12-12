from django import forms

from app.models import ProgressPicture


class ProgressPictureForm(forms.ModelForm):
    class Meta:
        model = ProgressPicture
        fields = '__all__'