from .models import todo_list
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_list
        fields = '__all__'
