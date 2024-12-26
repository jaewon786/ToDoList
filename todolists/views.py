from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request): 
  cur_user = request.user
  if request.method == 'POST':
    if cur_user.is_authenticated:
      form = TodoForm(request.POST)
      if form.is_valid():
        todo = form.save(commit=False)
        todo.create_date = timezone.now()
        todo.author = request.user
        todo.save()
        return redirect('todolists:index')
      else:
        return redirect('todolists:index')
    return redirect('common:login')
  else:
    if cur_user.is_authenticated:
      todo_list = Todo.objects.order_by('create_date').filter(author=request.user)
      context = { 'todo_list':todo_list }
      return render(request, 'todolists/todo_list.html', context)
    else:
      todo_list = []
      context = { 'todo_list':todo_list }
      return render(request, 'todolists/todo_list.html', context)


def todo_delete(request, todo_id):
  todo = get_object_or_404(Todo, pk=todo_id)
  todo.delete()
  return redirect('todolists:index')