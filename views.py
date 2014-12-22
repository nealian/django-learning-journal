from django.shortcuts import render_to_response, get_object_or_404
from journal.models import Tag, Entry
from django.http import Http404

def index(request):
    latest_entries = Entry.objects.all().order_by('-pub_date')[:5]
    return render_to_response('journal/entry_list.html', {'latest_entries': latest_entries,})

def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('journal/entry_detail.html', {'entry': entry,})

def tag_detail(request, tag_id)
    tag = get_object_or_404(Tag, pk=tag_id)
    latest_entries_for_tag = tag.entries.all().order_by('-pub_date')[:25]
    return render_to_response('journal/entry_list.html',
    {
        'tag': tag,
        'latest_entries': latest_entries_for_tag,
    })
