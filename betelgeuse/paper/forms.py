from django import forms
from .models import *


class AddPaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = "__all__"
