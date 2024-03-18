import sys
sys.stdin = open('input.txt')

def quicksort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quicksort(a, l, s-1)
        quicksort(a, s+1, r)


def partition(a, l, r):
    pivot = a[l]
    i, j = l, r

    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] >= pivot:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ai = list(map(int, input().split()))

    quicksort(ai, 0, n-1)

    print(f'#{test_case} {ai[n//2]}')