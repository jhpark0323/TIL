import sys
sys.stdin = open("input.txt")

T = int(input())

def DFS(i, k, s):
    # 맨 밑에까지 더했다면 합을 추가하고 리턴
    if i == k:
        result.append(s)
        return
    # 만약 특수한 줄이라면 이미 더했으니깐
    # 다음 줄로 가고 리턴
    elif i+1 in special_line:
        DFS(i+1, k, s)
        return
    # N까지 숫자를 바꿔가면서 더해준다
    for n in range(N):
        # 이때 위에 줄에서 사용한 열은 더해주지 못한다.
        if visited[n] == 0:
            visited[n] = 1
            DFS(i+1, k, s+arr[i][n])
            # 반환되면 다시 초기화 해준다
            visited[n] = 0


for tc in range(1, T+1):
    # 배열의 크기 N, 특수한 줄의 개수 M
    N, M = map(int, input().split())
    # 특수한 줄의 번호
    special_line = list(map(int, input().split()))
    # 배열의 합 리스트
    result = []
    # 배열의 숫자
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 특수한 줄은 다른 줄에 영향을 미치지 않는다
    # 시작부터 특수한 줄의 최솟값을 더하고 시작한다.
    start = 0
    for j in special_line:
        start += min(arr[j-1])

    # 해당 줄에 숫자를 더했는지 확인하기 위한 리스트트
    visited = [0] * N
    DFS(0, N, start)
    # print(result)
    print(f'#{tc}', min(result))