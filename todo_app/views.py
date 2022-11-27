from django.contrib import messages
from django.shortcuts import render
from .models import todo_list
from .forms import TodoForm
from django.views.generic import ListView


# Create your views here.
class HomeListView(ListView):
    model = todo_list
    context_object_name = 'obj'
    template_name = 'home.html'


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
