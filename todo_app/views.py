from django.contrib import messages
from django.shortcuts import render
from .models import todo_list
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# Create your views here.
class HomeDetailView(DetailView):
    model = todo_list
    template_name = 'details.html'
    context_object_name = 'obj'


class HomeDeleteView(DeleteView):
    model = todo_list
    template_name = 'delete.html'
    success_url = reverse_lazy('homelistview')



class HomeListView(ListView):
    model = todo_list
    context_object_name = 'obj'
    template_name = 'home.html'


class HomeUpdateView(UpdateView):
    model = todo_list
    template_name = 'update.html'
    context_object_name = 'obj'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('homedetailview', kwargs={'pk': self.object.id})


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        if name == "" or priority == "" or date == "":
            messages.info(request, 'please fill the fields')
        else:
            obj = todo_list(name=name, priority=priority, date=date)
            obj.save()
            messages.info(request, 'added successfully')
            print('added successfully')
    obj = todo_list.objects.all()
    return render(request, 'home.html', {'obj': obj})
