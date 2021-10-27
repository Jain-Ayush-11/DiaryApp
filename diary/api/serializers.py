from django.db import models
from django.db.models import fields
from diary.models import Entry
from rest_framework.serializers import ModelSerializer

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'