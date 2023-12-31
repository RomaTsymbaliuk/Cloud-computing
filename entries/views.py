from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Entry
from .forms import RegisterForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer
import datetime

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


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def main_method(request, item_id = None):
    time = request.query_params.get('time_on_task')
    purpose = request.query_params.get('purpose')
    date = request.query_params.get('date')


    if request.method == "POST":
        data = {'time_on_task': time, 'purpose': purpose, 'date': date, **request.data}
        serializer = DataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        if item_id is not None:
            object = Entry.objects.get(id=item_id)
            serializer = DataSerializer(object)
            return Response(serializer.data)

        app = Entry.objects.all()

        if time is not None:
            app = app.filter(Q(time_on_task=time) | Q(time_on_task__isnull=True))
        if purpose is not None:
            app = app.filter(Q(purpose=purpose) | Q(purpose__isnull=True))
        if date is not None:
            app = app.filter(Q(date=date))

        serializer = DataSerializer(app, many=True)

        return Response(serializer.data)
    elif request.method == "DELETE":
        if item_id is not None:
            object = Entry.objects.get(id=item_id)
            object.delete()
            serializer = DataSerializer(object)
            return Response(serializer.data)
        else:
            message = "Not found item_id"
            return JsonResponse({'status': 'false', 'message': message}, status=500)

    elif request.method == "PUT":
        if item_id is not None:
            object = Entry.objects.get(id=item_id)

            serializer = DataSerializer(instance=object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = "item_id is None"
            return JsonResponse({'status': 'false', 'message': message}, status=500)