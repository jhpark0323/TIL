# 1~6번까지 노드가 존재.

# 1. make_set
def make_set(n):
    # 각 숫자는 대표자의 index임
    # 자기자신이 대표자임 -> 현재는 n개의 집합을 가지고 있음
    return [i for i in range(n)]

# 1~6번까지를 사용하기 위해 7개 생성 (0은 버림)
parents = make_set(7)

# 2. find_set: 대표자를 찾아보자
# - 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# - 언제까지? 자기 자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
    # 자기 자신이 대표네? 끝
    if parents[x] == x:
        return x

    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    return find_set(parents[x])

# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은집합에 속해 있다면 continue
    if x == y:
        return

    # 다른집합이라면 합침
    # ex) 더 작은 루트노드에 합쳐라~
    if x < y:
        parents[y] = x

    else:
        parents[x] = y

union(1, 3)
union(2, 3)
union(5, 6)