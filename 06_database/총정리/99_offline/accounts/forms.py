from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    # UserCreationForm.Meta 클래스를 상속 받는다.
    class Meta(UserCreationForm.Meta):
         # 현재 활성화 되어 있는 User 모델로 변경
         model = get_user_model()
         # 필드는... 현재로서는 수정할게 없으므로 상속 받은 그대로 쓴다.
         # 만약, 회원 가입시 다른 필드 정보도 받고 싶다면 내가 바꾸면된다.