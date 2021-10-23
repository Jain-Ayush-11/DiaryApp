from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField(default = 'How was your day?')
    picture = models.ImageField(upload_to = 'static/img/images')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title
