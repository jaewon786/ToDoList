from django.urls import path

from . import views

app_name = 'todolists'

urlpatterns = [
  path('', views.index, name='index'),
  path('todo_delete/<int:todo_id>', views.todo_delete, name='todo_delete'),
  path('todo_complete/<int:todo_id>', views.todo_complete, name='todo_complete'),
]