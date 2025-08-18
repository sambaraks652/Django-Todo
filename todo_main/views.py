from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=True)
    print(tasks)
    return render(request, 'home.html')

def addTask(request):
    return HttpResponse("Task added!")
