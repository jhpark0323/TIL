import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    a_i = input()

    # ls에 a_i의 각 자리를 list로 만듬
    ls = list(map(int, list(a_i)))
    # print(ls)

    # ls의 각 원소들이 몇개인지를 세어줄 arr 생성
    arr = [0] * 10

    # arr에 ls의 원소들의 index에 맞게 갯수 추가
    for i in ls:
        arr[i] += 1
    # print(arr)
    # print(max(arr))

    # arr을 뒤집어 제일 많은 수들 중 제일 큰 수를 찾음
    arr.reverse()
    # print(arr)

    # max(arr)로 ls의 원소 중 제일 많은 장 수를 찾음
    # 전체가 9이고 arr을 뒤집었기 때문에 arr의 index로 찾은 후 9에서 빼줌
    print(f'#{test_case} {9 - arr.index(max(arr))} {max(arr)}')