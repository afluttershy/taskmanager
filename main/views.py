from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Task
from .forms import TaskForm
from rest_framework import viewsets, serializers
from rest_framework.parsers import json
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.views.generic.edit import UpdateView
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Список задач', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def delete(request, id):
    try:
        person = Task.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return redirect('home')


def edit(request, id):
    try:
        task = Task.objects.get(id=id)

        if request.method == "POST":
            task.title = request.POST.get("title")
            task.task = request.POST.get("task")
            task.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/edit.html", {"task": task})
    except Task.DoesNotExist:
        return redirect('home')


def gettasks(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize('json', tasks)
    return HttpResponse(tasks_json, content_type='application/json')

# serializers.serialize('json', tasks, fields=('title', 'task'))
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




