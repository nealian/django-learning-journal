from django.db import models
from django.utils import timezone

class Entry(models.Model):
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    public = models.BooleanField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'entries'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    entries = models.ManyToManyField(Entry)
    def __unicode__(self):
        return self.name
