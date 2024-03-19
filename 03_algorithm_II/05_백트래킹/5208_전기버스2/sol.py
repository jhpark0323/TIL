import sys
sys.stdin = open('input.txt')

def back(level, cnt, battery):
    global min_cnt

    if min_cnt <= cnt:
        return

    if level == n-1:
        if battery <= 0:
            return
        else:
            if min_cnt > cnt:
                min_cnt = cnt
            return

    if level < n-1 and battery > 0:
        # battery교체한 경우
        back(level+1, cnt+1, ls[level])
        # 교체 안한경우
        back(level+1, cnt, battery-1)



T = int(input())

for test_case in range(1, T+1):
    n, *ls = list(map(int, input().split()))
    # print(n)
    # print(ls)

    # cnt_ls = []
    min_cnt = float('inf')

    back(1, 0, ls[0])
    # print(cnt_ls)
    print(f'#{test_case} {min_cnt}')
