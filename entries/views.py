from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Entry
from .forms import RegisterForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy

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
            form.save()
            print(form.cleaned_data['date'])
            print(form.cleaned_data['purpose'])
            print(form.cleaned_data['time_on_task'])
        else:
            print('Form is not valid')
            print(form.errors)
    return HttpResponse(template.render(context, request))

def entry_add(request):
    template = loader.get_template('add_entry.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def entry_delete(request, item_id):
    print('Called entry_delete : ', item_id)

    object = Entry.objects.get(id=item_id)
    object.delete()
    context = {

    }
    return redirect('entries')
# Create your views here.
