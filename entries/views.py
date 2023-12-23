from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Entry
def entries(request):
    myentries = Entry.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myentries': myentries,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
