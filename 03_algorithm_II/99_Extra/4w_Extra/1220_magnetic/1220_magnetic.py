import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    # 한변의 길이 : 100
    length = int(input())

    # 테이블 초기모습
    # 1 : N극, 2 : S극
    arr = [list(map(int, input().split())) for _ in range(100)]

    # arr을 순회하며 N극(1)을 찾음

    cnt = 0
    # 그 후 내려가며 S극(2)을 찾고 만났을 때 cnt += 1 해줌
    for col in range(100):
        find = False
        for row in range(100):
            if arr[row][col] == 1:
                find = True

            elif arr[row][col] == 2 and find:
                cnt += 1
                find = False

    print(f'#{test_case} {cnt}')
