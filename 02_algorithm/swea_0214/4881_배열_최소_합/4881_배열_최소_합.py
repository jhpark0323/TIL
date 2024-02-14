import sys
sys.stdin = open('sample_input.txt')

def f(i, k, s):
    global min_sum

    # 끝까지 다 돌았을 때
    if i == k:
        # min_sum 갱신
        if min_sum > s:
            min_sum = s

    # 도는 중간에 이미 s가 min_sum을 넘어버리면 실행중단 -> 굳이 할 필요없음
    elif s >= min_sum:
        return

    # 끝까지 돌며 배열의 순서를 건드림
    else:
        # i번째 부터 마지막까지 순차적으로 -> i번째 포함하는 이유 -> 본인과 본인자리 바꾸는것 -> 자리 안바꾸는 경우
        for j in range(i, k):
            # 두개를 바꾼다
            p[i], p[j] = p[j], p[i]
            # 다음으로 넘어가며 s에 자리바꾼 배열을 더해줌 -> 재귀가 다 돌고나면 원래대로 바꿈
            f(i+1, k, s + arr[i][p[i]])
            # 다시 원래대로
            p[i], p[j] = p[j], p[i]



T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    p = [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    min_sum = 100
    f(0, n, 0)
    print(f'#{test_case} {min_sum}')
