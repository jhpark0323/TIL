import sys
sys.stdin = open('sample_input.txt')

'''
조합으로 각 행에서 하나씩 뽑아 더함
이 때 i,i는 뽑지 않는다.
'''

def f(i, k, s):
    global min_s
    # 다돌면 끝
    if i == k:
        if min_s > s:
            min_s = s
        return



    else:
        for j in range(i, k-1):

            path[i], path[j] = path[j], path[i]
            if i != path[i]:
                f(i+1, k, s+arr[path[j]][path[j+1]])
            path[i], path[j] = path[j], path[i]


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)

    # 최솟값을 담을 변수
    min_s = float('inf')
    # 조합을 만들 ls
    path = [i for i in range(2, n+1)]

    f(0, n, 0)
    print(min_s)


# import sys
# sys.stdin = open('sample_input.txt')
#
# # 현재 위치치
# def searc(now, cnt):
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
