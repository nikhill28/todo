from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def home (request):
    # data=Task.objects.all()
    data1=Task.objects.filter(is_complted=False).order_by('-updated_at')
    # data2=Task.objects.filter(is_complted=True)
    context={'data1': data1}
    return render(request,'home.html',context)

def add(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")


def mark_as_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('home')