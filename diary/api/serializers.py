from django.db import models
from django.db.models import fields
from django.db.models.expressions import Col
from diary.models import Entry, Collection
from rest_framework.serializers import ModelSerializer

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
