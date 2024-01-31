import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    # A집합 생성
    A = [i for i in range(1, 13)]
    # print(A)

    n, k = map(int, input().split())

    # 갯수를 세어줄 cnt 생성
    cnt = 0

    # 부분집합 생성
    # 집합A의 부분집합의 갯수(1 << len(A))만큼 반복문 실행
    for i in range(1<<len(A)):
        lst = []
        # 원소의 수만큼 비트를 비교함
        for j in range(len(A)):
            # i의 j번째 비트가 1인 경우 (1 << j -> j번째 자리에 1 나머지 0)
            if i & (1 << j):
                # j의 원소들을 << 연산자를 이용해 2^j으로 만든 후 2진변환 했을 때의 값들 : (1, 10, 100, 1000...)
                # i를 각각 2진변환 한 값들 : (0, 1, 10, 11, 100, 101, ...)
                # 각i마다 자릿수가 겹치면 그 j값들을 A에 넣음 (index로)
                # ex) i : 0, j : 0 -> 안겹침 X
                # ex) i : 1 -> 1_(2), j : 0 -> j : 1_(2) 겹침, j : 1 -> 안겹침, j : 2 -> 안겹침 ... -> j는 0일때만 겹침 -> lst = [A[0]]
                # ex) i : 2 -> 10_(2), j : 0 -> j : 1_(2) 겹침, 나머지 안겹침 -> lst = [A[1]]
                # ex) i : 3 -> 11_(2), j : 0 -> j : 1_(2) 겹침, j : 1 -> j : 10_(2) 겹침, 나머지 안겹침 -> lst = [A[0], A[1]]
                lst.append(A[j])
        # print(lst)
        if (len(lst) == n) & (sum(lst) == k):
            # print(lst)
            cnt += 1

    print(f'#{test_case} {cnt}')