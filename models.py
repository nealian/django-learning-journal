from django.db import models
from django.utils import timezone

class Entry(models.Model):
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    def should_be_published(self):
        return self.pub_date <= timezone.now()
    should_be_published.admin_order_field = 'pub_date'
    should_be_published.boolean = True
    should_be_published.short_description = 'Publish time?'
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200)
    entries = models.ManyToManyField(Entry)
    def __unicode__(self):
        return self.name
