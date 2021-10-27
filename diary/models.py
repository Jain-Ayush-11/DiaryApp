from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField(default = '')
    picture = models.ImageField(upload_to = 'static/img/images', blank = True, null = True, 
                                default = 'static/img/images/6a63572fa8d7c63d89fb237b6e4e8bw.jpg')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    isbookmark = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['completed', '-updated', '-created']

    def __str__(self):
        return self.title

# class Bookmarks(models.Model):
#     entry = models.ForeignKey(Entry, on_delete=CASCADE)