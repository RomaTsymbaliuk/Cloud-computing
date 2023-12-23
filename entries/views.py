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

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context = {
        'myentries': myentries,
    }
    return HttpResponse(template.render(context, request))

def entry_add(request):
    template = loader.get_template('add_entry.html')
    context = {
        "object": None
    }
    return HttpResponse(template.render(context, request))

def entry_delete(request, item_id):
    object = Entry.objects.get(id=item_id)
    object.delete()
    context = {

    }
    return redirect('entries')

def entry_update(request, item_id):
    object = Entry.objects.get(id=item_id)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            keys = form.fields.keys()
            for key in keys:
                val = form.cleaned_data[key]
                setattr(object, key, val)
            object.save()
            return redirect('entries')
        else:
            print(form.errors)
            return redirect('entries')
    template = loader.get_template('update.html')
    context = {
        "object": object
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
