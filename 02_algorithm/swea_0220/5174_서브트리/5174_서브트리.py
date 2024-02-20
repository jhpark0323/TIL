import sys
sys.stdin = open('sample_input.txt')

def pre_order(t):
    global cnt
    if t:
        cnt += 1
        # print(t, end = ' ')
        pre_order(left[t])
        pre_order(right[t])

T = int(input())

for test_case in range(1, T+1):
    # e : 간선의 개수, n : n을 루트로 하는 서브노드 찾기
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in range(e):
        parent, child = arr[2*i], arr[2*i+1]
        # 왼쪽 오른쪽 자식노드에 대한 기준이 없기 때문에 먼저 들어오는걸 욀쪽 자식으로 구성
        if not left[parent]:
            left[parent] = child
        # 왼쪽 자식이 있으면 오른쪽 자식으로 구성
        else:
            right[parent] = child

    # print('left :',left)
    # print('right :', right)

    cnt = 0
    pre_order(n)
    print(f'#{test_case} {cnt}')