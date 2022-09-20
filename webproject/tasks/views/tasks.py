from random import choices
from django.shortcuts import render
from tasks.models import Task
from django.shortcuts import redirect 


def add_view(request):
    if request.method == 'GET':
        choices = Task.CHOICES
        return render(request,'task_create.html',context={
            'choices': choices
        })
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date_deadline': request.POST.get('date_deadline')
    }
    Task.objects.create(**task_data)
    return redirect('/')

def del_view(request):
    if request.method == 'GET':
        id_task = request.GET.get('id')
        task = Task.objects.get(pk=id_task)
        task.delete()
        return redirect('/')


def edit_view(request):
    if request.method == 'GET':
        id_task = request.GET.get('id')
        task = Task.objects.get(pk=id_task)
        choices = Task.CHOICES
        context = {
            "task": task,
            'choices': choices
        }
        return render(request, 'task_edit.html', context=context)
    task = Task.objects.get(id=request.GET.get('id'))
    task.description = request.POST.get('description')
    task.status = request.POST.get('status')
    task.date_deadline = request.POST.get('date_deadline')
    task.save()
    
    return redirect('/')
    
