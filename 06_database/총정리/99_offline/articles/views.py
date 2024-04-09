from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
# articles 전체 정보를 pk기준 내림차순 정렬 (최신글)
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article 객체에 user_id 넣어야 하는데 article 객체 어딨음?
            article = form.save(commit=False)   # DB에 commit 하면안됨
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # article = form.save(commit=False)
            # article.user = request.user
            # article.save()
            return redirect('articles:index')
    else:
        # 기존에 있었던 데이터를 수정할 것이다.
        # 그럼 form을 구성할때도, 기존정보를 넣어주자
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)