from django.shortcuts import render_to_response, get_object_or_404
from journal.models import Tag, Entry
from django.http import Http404
from django.contrib.sites.shortcuts import get_current_site

def index(request):
    current_site = get_current_site(request)
    latest_entries = Entry.objects.all().order_by('-pub_date')[:5]
    return render_to_response('journal/entry_list.html',
    {
        'site_name': current_site.name,
        'latest_entries': latest_entries,
    })

def entry_detail(request, entry_id):
    current_site = get_current_site(request)
    entry = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('journal/entry_detail.html',
    {
        'site_name': current_site.name,
        'entry': entry,
    })

def tag_detail(request, tag_id):
    current_site = get_current_site(request)
    tag = get_object_or_404(Tag, pk=tag_id)
    latest_entries_for_tag = tag.entries.all().order_by('-pub_date')[:25]
    return render_to_response('journal/entry_list.html',
    {
        'site_name': current_site.name,
        'tag': tag,
        'latest_entries': latest_entries_for_tag,
    })
