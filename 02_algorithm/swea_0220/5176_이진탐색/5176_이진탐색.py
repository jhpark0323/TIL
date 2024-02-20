import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def inorder(t):
    global cnt
    # t가 0이아니고 n보다 작아야 트리안에 넣을 수 있음
    if t and t <= n:
        # 중위순회에 따라 왼쪽 자식부터 방문
        inorder(2 * t)
        # 왼쪽 자식을 다 돌고 난 후 본인 자리에 cnt
        ls[t] = cnt
        # 본인자리에 cnt넣고 1 증가
        cnt += 1
        # 중위 순회에 따라 마지막에 오른쪽 자식 방문
        inorder(2 * t + 1)


for test_case in range(1, T+1):
    n = int(input())

    # 빈 트리에 들어갈 숫자 -> 1부터
    cnt = 1

    # 교재 27page?
    # 빈 트리를 1차원 배열로 나타냄 -> 각 index는 완전 이진 트리의 노드 번호 (위에서부터 내려오면서 1~n까지)
    ls = [0 for _ in range(n+1)]
    # ls = [0] * (n+1)
    # print(ls)

    inorder(1)

    # print(ls)
    print(f'#{test_case} {ls[1]} {ls[n//2]}')