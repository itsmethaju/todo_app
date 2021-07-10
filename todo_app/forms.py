from .models import task
from django import forms


class ModeForm(forms.ModelForm):
    class Meta:
        model= task
        fields=['name','priority','date', ]
