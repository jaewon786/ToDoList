from django import forms
from todolists.models import Todo

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['content']