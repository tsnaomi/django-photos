from django.db import models
from django.contrib.auth.models import User
# from sorl.thumbnail import ImageField

# Create your models here.


class Photo(models.Model):
    creator = models.ForeignKey(User)
    image = models.ImageField(upload_to='IMAGES/')
    caption = models.CharField(max_length=40, default='Untitled')
    # albums = models.ManyToManyField(Album)
    # tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.caption


class Album(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=80, default='Untitled')
    photos = models.ManyToManyField(Photo, blank=True, null=True)
    description = models.TextField(default='')
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


# class Tag(models.Model):
#     creator = models.ForeignKey(User)
#     name = models.CharField(max_length=40, blank=False, null=False)

#     def __unicode__(self):
#         return self.name
