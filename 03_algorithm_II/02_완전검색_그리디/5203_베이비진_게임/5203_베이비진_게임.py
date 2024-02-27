import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    ls = list(map(int, input().split()))
    # print(ls)

    # 플레이어 별로 나누기
    player1 = ls[:6]
    player2 = ls[6:]

