from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "task_done", "tags"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'deadline': forms.DateTimeInput
            (attrs={"type": "datetime-local", "class": "form-control"}),
        }
