from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
        # else:
            # print(1)
    else:
        # print(2)
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)

# def new_todo(request):
#     form = TodoForm(request.POST)
#     if form.is_valid():
#         todo = form.save()
#         return redirect('todos:detail', todo.pk)
#     context = {
#         'form': form
#     }
#     return render(request, 'todos/create.html', context)

    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todos/update_todo.html', context)

# def edit_todo(request, todo_pk):
#     todo = Todo.objects.get(pk=todo_pk)
#     form = TodoForm(request.POST, instance=todo)
#     if form.is_valid():
#         todo = form.save()
#         return redirect('todos:detail', todo.pk)
#     context = {
#         'todo': todo,
#         'form': form
#     }
#     return render(request, 'todos/update_todo.html', context)