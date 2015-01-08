from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    public = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='entries_authored')
    modifier = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='entries_modified')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'entries'
        verbose_name = 'entry'
        permissions = (
            ("view_private", "Can view entries not marked as public"),
            ("edit_others", "Can edit entries authored by other users"),
        )

class Tag(models.Model):
    name = models.CharField(max_length=200)
    entries = models.ManyToManyField(Entry)
    def __unicode__(self):
        return self.name
