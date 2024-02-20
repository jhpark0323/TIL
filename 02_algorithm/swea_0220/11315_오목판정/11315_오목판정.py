import sys
sys.stdin = open('sample_input.txt')

'''
대각선 확인
각 행별로 확인
각 열별로 확인
이러면 시간초과 나나?
아 5x5가 아니구나
-> 그래도 걍 찾는거 함수로 만들고 돌리면 안되냐
'''

def find_omok(row, col):
    global answer
    # 대각선
    cnt_1 = 0
    cnt_2 = 0
    # 대각선1
    for ii in range(5):
        if arr[row+ii][col+ii] == 'o':
            cnt_1 += 1
    if cnt_1 == 5:
        answer = 'YES'
        return

    # 대각선2
    for ii in range(5):
        if arr[row+4-ii][col+ii] == 'o':
            cnt_2 += 1
    if cnt_2 == 5:
        answer = 'YES'
        return

    # 각행
    for _ in range(5):
        cnt_3 = 0
        for ii in range(5):
            if arr[row][col + ii] == 'o':
                cnt_3 += 1
        if cnt_3 == 5:
            answer = 'YES'
            return
        row += 1

    row -= 5

    # 각열
    for _ in range(5):
        cnt_4 = 0
        for ii in range(5):
            if arr[row+ii][col] == 'o':
                cnt_4 += 1
        if cnt_4 == 5:
            answer = 'YES'
            return
        col += 1

    col -= 5






T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # print(arr)

    answer = 'NO'
    for i in range(n-4):
        for j in range(n-4):
            find_omok(i, j)
            if answer == 'YES':
                break
        if answer == 'YES':
            break

    print(f'#{test_case} {answer}')