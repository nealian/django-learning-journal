from django.conf.urls import patterns, url

urlpatterns = patterns('journal.views',
    url(r'^$', 'index'),
    url(r'^(?P<entry_id>\d+)/$', 'entry_detail'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'tag_detail'),
)
