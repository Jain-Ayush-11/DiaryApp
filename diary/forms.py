from django.db import models
from django.forms import ModelForm, fields
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'