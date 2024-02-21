import sys
sys.stdin = open('sample_input.txt')

# k가 들어왔을 때
def enq(k):
    global last
    # 완전이진트리 유지
    last += 1
    # 마지막 노드에 추가
    tree[last] = k

    # 마지막 노드를 자식이라 생각하고
    child = last
    # 부모노드를 찾음
    parent = child // 2

    # 부모노드가 자식보다 크면
    while parent >= 1 and tree[parent] > tree[child]:
        # 두개 바꿈
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2



T = int(input())

for test_case in range(1, T+1):
    # 서로다른 n개의 자연수
    n = int(input())

    ls = list(map(int, input().split()))
    # print(ls)

    # 빈 트리
    tree = [0] * (n+1)

    # 마지막 노드 index
    last = 0

    for i in ls:
        enq(i)

    answer = 0
    idx = last
    while 1:
        # 부모노드 구하기
        idx //= 2
        # answer에 += 해주기
        answer += tree[idx]
        # 부모가 없으면 break
        if idx == 0:
            break

    # print(tree, last)
    print(f'#{test_case} {answer}')