from django.shortcuts import render_to_response, get_object_or_404
from journal.models import Tag, Entry
from django.http import Http404

def index(request):
    latest_post_list = Entry.objects.all().order_by('-pub_date')[:5]
    return render_to_response('journal/index.html', {'latest_post_list': latest_post_list,})

def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('journal/entry_detail.html', {'entry': entry})

def error_404(request):
    return render_to_response('404.html', {'request': request})

def error_500(request):
    return render_to_response('500.html', {'request': request})
