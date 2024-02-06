import sys
sys.stdin = open('input.txt')

'''
1. ls에서 최댓값을 찾은 후 그 전까지의 물건들을 사서 최댓값일 때 판다.
2. 최댓값의 index를 시작 index에 넣고 그 뒤에서 다시 최댓값을 찾아 반복한다.
'''

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ls = list(map(int, input().split()))
    # print(ls)

    # 시작 index
    start = 0

    # 원래 최댓값
    max_ls = max(ls)
    max_idx = ls.index(max_ls)

    total = 0
    while (0 <= start < len(ls)):
        # 시작idx부터 max_idx까지 순회하며 max값 - i를 total에 더해줌
        for i in range(start, max_idx+1):
            total += max_ls - ls[i]
            # print(total)
        # 시작 idx, max_ls, max_idx 초기화
        start = max_idx+1
        if start < len(ls):
            max_ls = max(ls[start:])
            # max_idx를 찾을 때 ls[start:]부터 찾아야 앞에서 안걸림 -> 그래서 그 뒤에서 찾고 앞의 길이만큼 더해줌
            max_idx = ls[start:].index(max_ls) + len(ls[:start])

    print(f'#{test_case} {total}')