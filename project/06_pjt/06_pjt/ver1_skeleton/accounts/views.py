from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('boards:index')

@login_required
def profile(request, user_pk):
    profile_owner = User.objects.get(pk=user_pk)
    owner_boards = profile_owner.board_set.all()
    owner_comments = profile_owner.comment_set.all()
    context = {
        'profile_owner' : profile_owner,
        'owner_boards' : owner_boards,
        'owner_comments' : owner_comments,
    }
    return render(request, 'accounts/profile.html', context)


@require_http_methods(["POST"])
def follow(request, user_pk):
    profile_owner = User.objects.get(pk=user_pk)
    if request.user != profile_owner:
        if request.user in profile_owner.follower.all():
            profile_owner.follower.remove(request.user)
        else:
            profile_owner.follower.add(request.user)
    
    return redirect('accounts:profile', profile_owner.pk)