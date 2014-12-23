from django.shortcuts import render_to_response, get_object_or_404
from journal.models import Tag, Entry
from django.http import Http404
from django.contrib.sites.models import Site

test_sidebar_contents = [
    {
        'h2': 'Test',
        'h3': 'Testing, testing, 1-2-3',
        'content': 'Lorem ipsum dolor sit amet.',
    },
    {
        'h3': 'Testing, testing, 2-3-4',
        'content': 'Interdum et malesuada fames ac.',
    },
    {
        'h2': 'More test',
        'content': 'Curabitur aliquet, libero ultrices dapibus.',
    },
]

def index(request):
    current_site = Site.objects.get_current()
    latest_entries = Entry.objects.all().order_by('-pub_date')[:5]
    return render_to_response('journal/entry_list.html',
    {
        'site_name': current_site.name,
        'latest_entries': latest_entries,
        'sidebar_contents': test_sidebar_contents,
    })

def entry_detail(request, entry_id):
    current_site = Site.objects.get_current()
    entry = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('journal/entry_detail.html',
    {
        'site_name': current_site.name,
        'entry': entry,
        'sidebar_contents': test_sidebar_contents,
    })

def tag_detail(request, tag_id):
    current_site = Site.objects.get_current()
    tag = get_object_or_404(Tag, pk=tag_id)
    latest_entries_for_tag = tag.entries.all().order_by('-pub_date')[:25]
    return render_to_response('journal/entry_list.html',
    {
        'site_name': current_site.name,
        'tag': tag,
        'latest_entries': latest_entries_for_tag,
        'sidebar_contents': test_sidebar_contents,
    })
