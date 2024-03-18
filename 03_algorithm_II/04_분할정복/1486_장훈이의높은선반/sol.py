import sys
sys.stdin = open('input.txt')

def back(key, result = 0):
    if key == n:
        return

    elif result >= b:
        ls.append(result)
        return

    for i in range(n):
        back(key+1, result+hi[i])
        back(key+1, result)

# def f(i, height):
#     if i == n:
#         return
#
#     elif height >= b:
#         ls.append(height)
#         return

    # for first in range(n):
    #     for second in range(first, n):
    #         p[first], p[second] = p[second], p[first]
    #         f(i+1, height+hi[second])
    #         p[first], p[second] = p[second], p[first]

T = int(input())

for test_case in range(1, T+1):
    n, b = map(int, input().split())
    hi = list(map(int, input().split()))

    p = [i for i in range(n)]

    ls = []
    back(0, 0)
    print(ls)