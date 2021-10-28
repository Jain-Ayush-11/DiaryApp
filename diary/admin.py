from django.contrib import admin

from diary.models import Entry, Collection

# Register your models here.
admin.site.register(Entry)
admin.site.register(Collection)