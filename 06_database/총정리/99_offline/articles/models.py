from django.db import models
from django.conf import settings

# Create your models here.
# 파이썬 기본 변수명 등의 컨벤션만 잘 지켜도 헷갈릴 일은 없다.
# Model class를 class에 상속한다.
class Article(models.Model):
    # 작성자 정보를 담기위한 1:N 관계
    # User Model -> 'accounts.User' 문자열 직접 작성해도 문제는 없음
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    # User와 M:N 관계
    # related_name을 정의해 줘야 하는 이유.
    '''
        Article class에는 user나 like_user 속성이 직접 정의가 되었다.
        반면, User class에는 정의한 적 없다.
        따라서, User class의 인스턴스는, 그런 관계 모델 정보를 받아로 방법이 없다.
        그래서, user 인스턴스도 관계 모델 정보를 받아오기 쉽게 하기 위해서
        django가 반대쪽 모델에도 매니저를 자동으로 설정을 해준다.
            -> 매니저 자동 설정의 규칙은?
            -> 참조 대상 `모델의 소문자명_set` 으로 만들어준다.
        즉, FK 만든 관계든 MTMF 만든 관계든
        User 입장에서는 article_set 이라는 이름으로 매니저가 만들어질것이다.
        그말은....
        dust = 60
        dust - 50 과 같다.
        하나의 변수에 2개 이상의 값을 할 당 할 수는 없으니...
        충돌이 발생하게 된다.
        그러므로, 둘 중 한곳의 related_name을 변경해주는 것이다.
        그럼 왜 굳이 MTMF 쪽에 만드느냐? 그건... 이유는 딱히 없다.
    '''
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                        related_name='like_articles'
                                        )
    # 컨벤션 안지킨다고 오류가 나는건 아님
    title = models.TextField()
    content = models.TextField()

# class Comment(models.Model):
#     aritlce = models.ForeignKey('article')