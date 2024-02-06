import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1, str2 = input().split()

    # str1안에 str2가 몇개 있는지 세기
    cnt = str1.count(str2)

    # str1길이 - cnt x (str2길이 - 1)
    print(f'#{test_case} {len(str1) - cnt * (len(str2)-1)}')
