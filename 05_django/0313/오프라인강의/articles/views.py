from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def dtl_practice(request):
    lunch = [
        '타코야끼',
        '치킨하이라이스',
        '볶음우동',
        '강식당라면',
        '기사식당불백',
    ]
    empty_list = []
    context = {
        'lunch' : lunch,
        'empty_list' : empty_list,
    }

    return render(request, 'articles/dtl_practice.html', context)

def profile(request, username):
    print("=="*30)
    print(username)
    print("=="*30)
    context = {
        'username' : username
    }
    return render(request, 'articles/profile.html', context)

def numbers(request, num):
    context = {
        'num' : num
    }
    return render(request, 'articles/numbers.html', context)