from django.shortcuts import redirect, render
from taskapp.models import TaskModel
from .forms import TaskModelForm,TaskUpdateForm

# Create your views here.
def index(request):
    data = TaskModel.objects.all().order_by('-date')
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = TaskModelForm()
    total_task = data.count()
    completed_task = TaskModel.objects.filter(iscomplete = True).count()
    incompleted_task = total_task - completed_task
    
    context = {
        'data':data,
        'total_task':total_task,
        'completed_task':completed_task,
        'incompleted_task':incompleted_task,
        'form':form
    }
    return render(request,'taskapp/index.html',context)


def about(request):
    return render(request,'taskapp/about.html')



def delete(request,pk):
    item = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'taskapp/delete.html')



def edit(request,pk):
    item = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskUpdateForm(instance=item)
    context = {
        'form':form,
    }
    return render(request,'taskapp/edit.html',context)