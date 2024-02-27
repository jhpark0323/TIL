import sys
sys.stdin = open('sample_input.txt')

'''
조합으로 각 행에서 하나씩 뽑아 더함
이 때 i,i는 뽑지 않는다.
'''

def f(now, s):
    global min_s
    # 다돌면 끝
    if all(visited):
        s += arr[now][0]
        if min_s > s:
            min_s = s
        return

    elif s > min_s:
        return

    else:
        # 본인 위치는 가지 않기 때문에 1부터 시작
        for next in range(1, n):
            # 다음 갈 위치가 본인과 다르고 방문하지 않았다면
            if now != next and not visited[next]:
                # 방문표시
                visited[next] = True
                f(next, s + arr[now][next])
                visited[next] = False


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)

    # 최솟값을 담을 변수
    min_s = float('inf')

    # 방문한 곳 갱신용
    visited = [False] * n

    # 시작은 0
    visited[0] = True
    f(0, 0)
    print(f'#{test_case} {min_s}')
