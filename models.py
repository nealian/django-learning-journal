from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    public = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    modifier = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'entries'
        permissions = (
            ("view_private", "Can view entries that haven't been marked as public"),
        )

class Tag(models.Model):
    name = models.CharField(max_length=200)
    entries = models.ManyToManyField(Entry)
    def __unicode__(self):
        return self.name
