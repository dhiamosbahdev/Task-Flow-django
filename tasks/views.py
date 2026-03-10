from django.shortcuts import render
from  .models import Task


def home(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks})

