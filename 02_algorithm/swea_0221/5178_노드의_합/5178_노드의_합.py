import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # n : 노드의 갯수, m : 리프 노드의 갯수, l : 값을 출력할 노드 번호
    n, m, l = map(int, input().split())

    # 리프 노드의 번호와 숫자
    leaf = [list(map(int, input().split())) for _ in range(m)]

    # tree 만들기
    tree = [0] * (n+1)
    for i in range(m):
        idx, leaf_num = leaf[i][0], leaf[i][1]
        tree[idx] = leaf_num

    # print(tree)

    # 리프노드를 제외한 나머지 노드의 idx
    else_node_idx = n-m
    # print(else_node_idx)

    # else_node_idx가 0이 아닐때 까지
    while else_node_idx:
        # 좌우 자식들의 idx
        left_child = else_node_idx * 2
        right_child = else_node_idx * 2 + 1
        # 왼쪽 자식이 있을 때
        if left_child <= n:
            # 근데 오른쪽 자식도 있을 때
            if right_child <= n:
                tree[else_node_idx] = tree[left_child] + tree[right_child]
            # 왼쪽만 있을 때
            else:
                tree[else_node_idx] = tree[left_child]
        # 다하고 나서 마지막노드 1 빼주기
        else_node_idx -= 1

    # print(tree)
    print(f'#{test_case} {tree[l]}')
