from django import forms
from . import models


class TrainingForm(forms.ModelForm):
    class Meta:
        model = models.Training
        fields = [
            'content'
        ]
        # exclude = [
        #     'user',
        # ]
