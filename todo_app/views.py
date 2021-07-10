from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ModeForm
from . models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListview(ListView):
    model = task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'i'

class UpdateView(UpdateView):
    model=task
    template_name= 'update.html'
    context_object_name='task'
    fields={'name','priority','date'}
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class TaskDeleteView(DetailView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def task_view(request):
    obj1=task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        obj = task(name=name, priority=priority,date=date)
        obj.save()

    return render(request,'task_view.html',{'obj1':obj1})
def delete(request,id):
    if request.method=='POST':
        obj=task.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    obj = task.objects.get(id=id)
    form=ModeForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

