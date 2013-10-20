from list_view.models import ListItem
from django.shortcuts import render
from django.template import RequestContext

def index(request):
    items = ListItem.objects.all()
    context = RequestContext(request, {'items': items})
    return render(request, 'index.html', context)
