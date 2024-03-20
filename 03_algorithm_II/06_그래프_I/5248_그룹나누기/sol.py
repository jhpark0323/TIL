import sys
sys.stdin = open('input.txt')

def make_set(x):
    # x번까지의 출석 번호, 0번안씀
    parent = [i for i in range(x+1)]
    rank = [0] * (x+1)
    return parent, rank

def find_set(x):
    # 부모가 자기자신이 아니면
    if parent[x] != x:
        # 부모를 find_set에 자신의 부모를 재귀적으로 넣어 찾아라
        parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x, y):
    # 부모 찾기
    root_x = find_set(x)
    root_y = find_set(y)

    # 부모가 다르면 합침
    if root_x != root_y:
        # rank로 비교해서 더 큰쪽으로 합침
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        # 둘의 rank가 같으면 그냥 앞에껄로 합치자 -> 딱히 이유는 없음
        # -> 이문제에서는 대표가 그리 중요하진 않은듯
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))

    parent, rank = make_set(n)

    # 2개씩 묶어주기
    new_ls = []
    for i in range(0, len(ls), 2):
        new_ls.append([ls[i], ls[i+1]])
    # print(new_ls)

    # 합치기
    for i in new_ls:
        union_set(i[0], i[1])

    print(parent)
    # 평탄화
    for i in range(1, n+1):
        find_set(i)

    parent = parent[1:]
    print(parent)

    # cnt = []
    # ans = 0
    # for i in range(n):
    #     if parent[i] not in cnt:
    #         cnt.append(parent[i])
    #         ans += 1

    print(f'#{test_case} {len(set(parent))}')