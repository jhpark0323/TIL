from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    todo_list = Todo.objects.all()
    context = {
        # 'work': work
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def new(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    is_completed = False
    created_at = request.POST.get('created_at')
    todo = Todo(work=work, content=content, is_completed=is_completed, created_at=created_at)
    todo.save()

    return redirect('todos:detail', todo.pk)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')