from django.conf.urls import patterns, url

urlpatterns = patterns('journal.views',
    url(r'^$', 'index', name="journal-index"),
    url(r'^(?P<entry_id>\d+)/$', 'entry_detail', name="journal-entry"),
    url(r'^tag/(?P<tag_id>\d+)/$', 'tag_detail', name="journal-tag"),
)
