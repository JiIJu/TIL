from django.shortcuts import render , redirect , get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .forms import TodoForm 
from .models import Todo

# Create your views here.
@require_safe
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request,'todos/index.html',context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context={
        'form':form,
    }
    return render(request,'todos/create.html',context)


def update(request,pk):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    todo = get_object_or_404(Todo,pk=pk)
    if request.user == todo.author:
        todo.completed = not todo.completed
    # if todo.completed == True:
    #     todo.completed = False
    # else:
    #     todo.completed = True
        todo.save()
    return redirect('todos:index')

def delete(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index',todo.pk)