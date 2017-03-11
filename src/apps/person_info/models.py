# -*- coding: utf-8 -*-*
from PIL import Image
from django.db import models


class Person(models.Model):
    """Person model"""

    first_name = models.CharField(
        max_length=50,
        blank=False,
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
    )
    date_of_birth = models.DateField(
        blank=False,
    )
    bio = models.TextField(
        blank=True,
        max_length=250,
    )
    photo = models.ImageField(
        upload_to='photo/',
        blank=True,
        null=True
    )
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(
        max_length=50,
    )
    other_contacts = models.TextField(
        max_length=250,
    )

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo)
            image.thumbnail((200, 200), Image.ANTIALIAS)
            image.save(self.photo.path, 'JPEG', quality=100)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class RequestLogger(models.Model):
    """Request Logger Model"""
    PRIORITIES = [(i, i) for i in range(5)]
    time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Request time'
    )
    request_method = models.CharField(
        max_length=15,
        verbose_name=u'Method'
    )
    ip_addr = models.IPAddressField(
        blank=True
    )
    full_path = models.CharField(
        max_length=100,
        verbose_name=u'Full request path'
    )
    priority = models.IntegerField(
        max_length=1,
        default=0,
        choices=PRIORITIES,
        blank=True
    )

    def __unicode__(self):
        return '%s %s' % (self.time, self.full_path)


class ModelActionLog(models.Model):
    ACTIONS = (
        (0, 'create'),
        (1, 'edit'),
        (2, 'delete')
    )
    time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Action Time'
    )
    inst = models.CharField(
        max_length=200,
        verbose_name=u'Instance'
    )
    action = models.IntegerField(
        max_length=1,
        choices=ACTIONS,
        verbose_name=u'Object actions'
    )

    def __unicode__(self):
        return '%s: %s %s' % (self.time, self.inst, self.action)
