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


