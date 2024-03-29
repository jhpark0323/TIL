def make_set(x):
    # 노드 번호 수 만큼 parent list 작성
    parent = [i for i in range(x)]
    # 첫 make_set 시행시, 본인을 루트로 하는 노드만 있으므로
    rank = [0] * x
    # parent, rank 반환
    return parent, rank

# 1~6번까지의 노드가
# 0번 노드 안씀
parent, rank = make_set(7)
print(parent)
print(rank)

def find_set(x):
    # 자기 자신을 부모로 하는 루트 노드를 찾을 때 까지 탐색
    if parent[x] == x:
        return x

    return find_set(parent[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 집단의 루트 노드가 서로 다르면 합치는 과정
    if root_x != root_y:
        # 합칠 때, 기준은 rank를 기준으로 작업한다.
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        # 두 집단의 rank가 동일 하다면
        # 둘중에 하나 정해서 거기에 붙이고,
        # 해당 집단의 rank를 1 상승 시킨다.
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

union(1, 3)
print(parent)
print(rank)
union(2, 3)
print(parent)
print(rank)
union(5, 6)
print(parent)
print(rank)
union(6, 3)
print(parent)
print(rank)
