from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
def home(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'tasks/task_list.html', context)