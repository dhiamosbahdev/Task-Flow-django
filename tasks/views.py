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

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, 'tasks/delete_task.html', {'task': task})