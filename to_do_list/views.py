from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from to_do_list.models import Task, Tag

from .forms import TaskForm


# Create your views here.

class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy('to_do_list:task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy('to_do_list:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_list/task_confirm_delete.html"
    success_url = reverse_lazy('to_do_list:task-list')


class TaskStatusView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.task_done = not task.task_done
        task.save()
        return redirect(reverse_lazy("to_do_list:task-list"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "to_do_list/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy('to_do_list:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name']
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy('to_do_list:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do_list/tag_delete.html"
    success_url = reverse_lazy('to_do_list:tag-list')
