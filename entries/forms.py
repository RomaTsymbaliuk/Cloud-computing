from django import forms

from django.forms import ModelForm
from .models import Entry

class RegisterForm(ModelForm):
    class Meta:
        model = Entry
        fields = ["date", "purpose", "time_on_task"]