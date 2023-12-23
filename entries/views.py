from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Entry
from .forms import RegisterForm
def entries(request):
    myentries = Entry.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myentries': myentries,
    }
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print('POST method on entries')
        if form.is_valid():
            print('Form is valid')
        else:
            print('Form is not valid')
            print(form.errors)
    return HttpResponse(template.render(context, request))

def entry_add(request):
    template = loader.get_template('add_entry.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

# Create your views here.
