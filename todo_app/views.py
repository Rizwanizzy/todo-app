from django.contrib import messages
from django.shortcuts import render, redirect
from .models import todo_list



# Create your views here.

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


