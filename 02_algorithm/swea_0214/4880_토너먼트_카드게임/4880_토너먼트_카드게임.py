import sys
sys.stdin = open('sample_input.txt')

'''
숫자 1은 가위, 2는 바위, 3은 보

함수에서 return 값은 index로! -> 맞는지 모르겠긴함
'''

# 가위 바위 보 함수
def rock_scissor_paper(front, back):
    # 가위, 보가 나오면 따로 계산해줌
    if card[front] == 3 and card[back] == 1:
        return back

    elif card[front] == 1 and card[back] == 3:
        return front

    # 비길경우 앞에꺼 return
    elif card[front] == card[back]:
        return front

    # 다른 경우 숫자가 큰게 이김
    elif card[front] > card[back]:
        return front

    elif card[back] > card[front]:
        return back

# 2개씩 나눠서 계산
def f(start, end):
    # 나누다가 한명만 남으면 그사람 올리기
    if start == end:
        # 가위 바위 보 하기
        return start

    # 나누기
    else:
        mid = (start + end) // 2
        front = f(start, mid)
        back = f(mid+1, end)

        return rock_scissor_paper(front, back)



T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    card = list(map(int, input().split()))
    # print(card)
    print(f'#{test_case} {f(0, n-1)+1}')
