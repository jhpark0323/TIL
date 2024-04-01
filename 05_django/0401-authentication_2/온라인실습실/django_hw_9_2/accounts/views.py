from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm

# Create your views here.
def index(request): 
  user_list = User.objects.all()
  context = {
    'user_list': user_list,
  }
  return render(request, 'accounts/index.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('accounts:index')
  
  else:
    form = AuthenticationForm()
  context = {
    'form' : form,
  }
  
  return render(request, 'accounts/login.html', context)

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('accounts:index')
  
  else:
    form = CustomUserCreationForm()
  context = {
    'form' : form,
  }
  return render(request, 'accounts/signup.html', context)