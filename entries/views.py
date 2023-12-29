from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Entry
from .forms import RegisterForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer

def entries(request):
    myentries = Entry.objects.all().values()
    template = loader.get_template('index.html')
    context = {}

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    if myentries is not None:
        context = {
            'myentries': myentries
        }
    else:
        context = {
            'myentries': None,
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

@api_view(['GET'])
def get_data(request):
    time = request.query_params.get('time_on_task')
    purpose = request.query_params.get('purpose')
    date = request.query_params.get('date')
    if time != None:
        app = Entry.objects.get(time_on_task=time)
        if len(app) > 1:
            serializer = DataSerializer(app, many=True)
        else:
            serializer = DataSerializer(app)
    elif purpose != None:
        app = Entry.objects.get(purpose=purpose)
        if len(app) > 1:
            serializer = DataSerializer(app, many=True)
        else:
            serializer = DataSerializer(app)
    elif date != None:
        app = Entry.objects.get(date=date)
        if len(app) > 1:
            serializer = DataSerializer(app, many=True)
        else:
            serializer = DataSerializer(app)
        serializer = DataSerializer(app)
    else:
        app = Entry.objects.all()
        serializer = DataSerializer(app, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def post_data(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)