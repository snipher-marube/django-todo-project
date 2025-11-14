from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, created=timezone.now())
        return redirect('task_list')
    
    tasks = Task.objects.all().order_by('-created')
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/task_list.html', context)

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

