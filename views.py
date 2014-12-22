from django.template import Context, loader
from journal.models import Tag, Entry
from django.http import HttpResponse

def index(request):
    latest_post_list = Entry.objects.all().order_by('-pub_date')[:5]
    return render_to_response('journal/index.html', {'latest_post_list': latest_post_list,})
