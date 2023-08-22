from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_web.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "todo_web/index.html", context=context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_web:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    fields = "__all__"
    model = Task
    success_url = reverse_lazy("todo_web:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_web:index")
    template_name = "todo_web/task_delete_confirm_delete.html"


class TagsListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagsCreateView(LoginRequiredMixin, generic.CreateView):
    fields = "__all__"
    model = Tag
    success_url = reverse_lazy("todo_web:tags-list")


class TagsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_web:tags-list")


class TagsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_web:tags-list")
    template_name = "todo_web/tag_delete_confirm_delete.html"


def task_complete(request, pk):
    task = Task.objects.get(id=pk)

    if not task.is_completed:
        task.is_completed = True
    else:
        task.is_completed = False
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("todo_web:index")
    )
