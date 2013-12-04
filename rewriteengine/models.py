from django.db import models


class htaccess(models.Model):
    name = models.CharField(max_length=200)
    CMS = models.CharField(max_length=200, blank=True)
    redirection = models.BooleanField()
    rewrite = models.BooleanField()
    rule = models.TextField()
    condition = models.CharField(max_length=500, blank=True)
    bulk_upload = models.BooleanField()

    def __unicode__(self):
        return self.name


