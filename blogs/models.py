from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    page_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    pub_date = models.DateField('date published', default=datetime.now())
    is_comment = models.BooleanField()
    category = models.ForeignKey(Category)
    page_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    comment = models.TextField()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class FileUpload(models.Model):
    blog = models.ForeignKey(Blog)
    alt = models.CharField(max_length=200)
    url = models.FileField(upload_to='uploads/')

    def __unicode__(self):
        return self.alt





