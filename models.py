from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    def __unicode__(self):
        return self.title
