from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from todolist.forms import TaskForm
from todolist.models import Task


class TodoView(View):
    def get(self, request):
        tasks_todo = Task.objects.filter(status='todo').order_by('-id')
        tasks_done = Task.objects.filter(status='done').order_by('-id')

        return render(
            request,
            'todolist.html',
            {
                'form': TaskForm(),
                'tasks_todo': tasks_todo,
                'tasks_done': tasks_done,
            },
        )

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        return render(request, 'todolist.html', {'form': form})


class TaskDone(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.status == 'todo':
            task.status = 'done'
            task.save()
        return redirect('todo')


class TaskTurnBack(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.status == 'done':
            task.status = 'todo'
            task.save()
        return redirect('todo')
