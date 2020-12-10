from django import forms
from app.models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'


class DeleteRecipe(WorkoutForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
