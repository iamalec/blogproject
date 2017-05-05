from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BBS(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='This guy is too lazy!')
    photo = models.ImageField(upload_to="upload_img", default='upload_img/user-1.jpg')
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator =models.ForeignKey(BBS_user)
    def __unicode__(self):
        return self.name
