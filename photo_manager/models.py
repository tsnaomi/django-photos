from django.contrib.auth.models import User, Group
from django.db import models
from django.dispatch import receiver
from registration.signals import user_activated


class Album(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=80, default='Untitled')
    description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    public_album = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.title


class Photo(models.Model):
    creator = models.ForeignKey(User)
    image = models.ImageField(upload_to='IMAGES/')
    caption = models.CharField(max_length=40, default='Untitled',
                               blank=True, null=True)
    albums = models.ManyToManyField(Album)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.caption


@receiver(user_activated)
def activation_receiver(sender, **kwargs):
    group = Group.objects.get(name='Activated')
    group.user_set.add(kwargs['user'])
