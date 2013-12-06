from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    page_slug = models.CharField(max_length=200)
    pub_date = models.DateField('date published', default=datetime.now())
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=500, blank=True)
    is_menu = models.BooleanField()

    def __unicode__(self):
        return self.title


class Images(models.Model):
    content = models.ForeignKey(Content)
    alt = models.CharField(max_length=200, blank=True)
    url = models.ImageField(upload_to='images/')

    def __unicode__(self):
        return self.alt


class slideshow(models.Model):
    content = models.ForeignKey(Content)
    alt = models.CharField(max_length=200, blank=True)
    url = models.ImageField(upload_to='slideshows/')

    def __unicode__(self):
        return self.alt


from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    sender = forms.EmailField()
    name = forms.CharField(max_length=100)
    cc_myself = forms.BooleanField(required=False)