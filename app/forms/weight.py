from django import forms
from app.models import Weight

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'

        exclude = ('user',)