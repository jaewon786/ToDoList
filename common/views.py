from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm
from todolists.models import Todo

def logout_view(request):
    logout(request)
    return redirect('todolists:index')

def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)  # 사용자 인증
      login(request, user)  # 로그인
      return redirect('todolists:index')
  else:
    form = UserForm()
  return render(request, 'common/signup.html', {'form': form})

def information(request):
  workedCount = Todo.objects.filter(author=request.user).filter(completed=True).count
  workingCount = Todo.objects.filter(author=request.user).filter(completed=False).count
  user = request.user
  info = {'user':user, 'workedCount':workedCount, 'workingCount':workingCount}
  return render(request, 'common/information.html', info)
    
