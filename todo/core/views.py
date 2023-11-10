from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task


# Create your views here.
def home (request):
    # data=Task.objects.all()
    data1=Task.objects.filter(is_complted=False).order_by('-updated_at')
    completed=Task.objects.filter(is_complted=True)
    context={
        'data1': data1,
        'completed':completed
        }
    return render(request,'home.html',context)

def add(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")


def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complted = True
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complted = False
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method=="POST":
        new_task=request.POST['task']
        get_task.task=new_task   #update the task field in models
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'task.html',context)

