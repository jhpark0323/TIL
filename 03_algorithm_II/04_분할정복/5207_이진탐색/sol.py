import sys
sys.stdin = open('sample_input.txt')

def binary_search(target):
    global cnt
    low = 0
    high = n-1

    ls = []

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == target:
            cnt += 1
            # print(target)
            return

        elif a[mid] < target:
            # 처음에는 그냥 더해줌
            if not ls:
                pass
            else:
                if ls[-1] == 0:
                    return
            ls.append(0)
            low = mid +1
            # print('right', target)

        else:
            # 처음에는 그냥 더해줌
            if not ls:
                pass
            else:
                if ls[-1] == 1:
                    return
            ls.append(1)
            high = mid - 1
            # print('left', target)

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    # 정렬해야할 ls
    a = list(map(int, input().split()))
    # b안의 원소들을 a에 이진탐색함
    b = list(map(int, input().split()))

    a.sort()

    cnt = 0
    for i in b:
        binary_search(i)


    print(f'#{test_case} {cnt}')