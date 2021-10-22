from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField(default = 'How was your day?')
    picture = models.ImageField()
    def __str__(self):
        return self.title
