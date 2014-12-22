from django.conf.urls import patterns, url

journal_urlpatterns = patterns('journal.views',
    url(r'^$', 'index'),
    url(r'^(?P<entry_id>\d+)/$', 'entry_detail'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'tag_detail'),
    url(r'^tag/(?P<tag_id>\d+)/(?P<entry_id>\d+)/$', 'tag_entry_detail'),
)
