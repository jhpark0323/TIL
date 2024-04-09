from django.shortcuts import render, redirect
# 근데, 내 view함수 login이랑 이름 겹침... -> as 별칭 만들기
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 인증 여부를 판별하는 데코레이터
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
def signup(request):
    # GET 요청, POST요청 조건 분기
    if request.method == 'POST':
        # 사용자가 POST 방식으로 보낸 데이터를 포함해서.
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # 사용자가 보낸 정보로 user 생성
            print('저장 완료되었음.')
            # 함수로 한번에 하나의 요청에 대한 응답
            return redirect('accounts:login')
    else:
        # 사용자가 회원가입을 위한 
        # 데이터를 입력할 form을 렌더링
        # django가 기존에 제공하는 UserCreationForm은 auth.User를 기준으로 만들어졌다.
        # 그래서 Meta class에 있는 model 정보가 auth.User에서 accounts.User로 바꿔야함.
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # DB에 저장 하는것 아님!!! -> 애초에 ModelForm도 아님!!
            # 로그인 이라는 행위를 하고 싶다. -> 이미 장고가 만들어둠
            # 로그인을 하기위해, form에 user에 대한정보를 받았음.
            # auth_login 함수에 넘겨줘야할 user 객체는? 당연히 form에있음
            auth_login(request, form.get_user())
            # 기획서에 보니까 profile은 username 필요로함...
            # <form action="{% url 'accounts:profile' user.username %}">
            return redirect('accounts:profile', form.get_user().username)
    else:
        # 로그인을 위한 정보 입력할 수 있는 form을 렌더링
        '''
            회원 가입은.. User Model과 관계된 작업
            auth.User - > accounts.User로 대체 되었으므로,
            django가 제공해주는 ModelForm도 model 정보 수정해야했다.
            근데, 로그인은? User Model이랑 사실 관계가 없다.
            하지만, 인증을 위해 username, password 입력할 form은 필요하다.
            이것도 마찬가지로 djangor가 이미 만들어둠.
        '''
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def profile(request, username):
    '''
        아니.. User 모델은 뭐 어쩌구 저쩌구 해서
        settings.AUTH_USER_MODEL 을 쓴다거나
        get_user_model() 한 이거 쓰고 뭐 어쩌구 하더니...
        왜 여기서는 그냥 User 가져다 씀?
        왜냐면 이 프로젝트는 오늘 이후로 영원히 켜볼 일이 없으므로
        User 모델이 바뀔 리가 없다.
    '''
    profile_owner = User.objects.get(username=username)
    context = {
        'profile_owner': profile_owner
    }
    return render(request, 'accounts/profile.html', context)

# 데코레이터를 통해서 함수를 꾸며준다.
@login_required
def follow(request, profile_owner_pk):
    # 인증 되었는지 확인이 가능하다.
    # if request.user.is_authenticated:
    profile_owner = User.objects.get(pk=profile_owner_pk)
    # me = request.user
    # form태그에 작성했던 조건분기랑 똑같이 적으면됨.
    if request.user in profile_owner.followers.all():
        # request.user.followings.remove(profile_owner)
        profile_owner.followers.remove(request.user)
    else:
        # request.user.followings.add(profile_owner)
        profile_owner.followers.add(request.user)
    return redirect('accounts:profile', profile_owner.username)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')