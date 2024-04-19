# 0. Admin
- User model의 admin 등록
```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```

# A. 유저 기능
## 1. 회원 가입
```py
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

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
```
## 2. 로그인 & 로그아웃
```py
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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
```

# B. Boards 앱 기능
- 본인이 작성한 게시글만 수정 및 삭제가 가능하도록: `{% if board.author == request.user %}`
- 인증된 사용자에게만: `{% if request.user.is_authenticated %}`

# C. M:N relationship
## 1. 유저 팔로우 기능
```py
@require_http_methods(["POST"])
def follow(request, user_pk):
    profile_owner = User.objects.get(pk=user_pk)
    if request.user != profile_owner:
        if request.user in profile_owner.follower.all():
            profile_owner.follower.remove(request.user)
        else:
            profile_owner.follower.add(request.user)
    
    return redirect('accounts:profile', profile_owner.pk)
```

## 2. 게시글 좋아요 기능
```py
# model.py
class Board(models.Model):
    title = models.CharField(max_length=20)
    ...
    likes = models.ManyToManyField(User, symmetrical=False, related_name='liked_board')
    # related_name에 유의
```
```py
# views.py
@require_http_methods(['POST'])
def likes(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.user in board.likes.all():
        board.likes.remove(request.user)
    else:
        board.likes.add(request.user)

    return redirect('boards:detail', board.pk)
```