from django.shortcuts import render, get_object_or_404
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

common_params = {
    'site_name': Site.objects.get_current().name,
    'sidebar_contents': test_sidebar_contents,
}

def index(request):
    latest_entries = Entry.objects.filter(public=True).order_by('-pub_date')[:5]
    return render(request, 'journal/entry_list.html', 
                  dict(common_params.items() + {
                      'latest_entries': latest_entries,
                  }.items()))

def entry_detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=endry_id)
        if not entry.public:
            raise Http404
    except Entry.DoesNotExist:
        raise Http404
    return render(request, 'journal/entry_detail.html',
                  dict(common_params.items() + {
                      'entry': entry,
                  }.items()))

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    latest_entries_for_tag = tag.entries.filter(public=True).order_by('-pub_date')[:25]
    return render(request, 'journal/entry_list.html',
                  dict(common_params.items() + {
                      'tag': tag,
                      'latest_entries': latest_entries_for_tag,
                  }.items()))
