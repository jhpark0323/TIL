import sys
sys.stdin = open('sample_input.txt')

import pprint

code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

'''
뒤에서 부터 찾는데 처음 0이 아닌 수가 오면 거기서부터 56의 배수만큼 길이를 찾음
근데 암호코드가 두번 들어있을 수도 있어서 
'''

T = int(input())

for test_case in range(1, T+1):
    # n x m 크기의 배열
    n, m = map(int, input().split())

    arr = [list(input()) for _ in range(n)]
    # for i in range(m):
        # print(arr)

    ls = []
    # n번 돌면서 각 행을 찾음
    for row in range(n):
        # m번 돌면서 각 열을 뒤에서 부터 찾음
        for col in range(m-1, -1, -1):
            if arr[row][col] == '1':
                break

        if arr[row][col] == '1':
            break

    # print(row, col)

    # ls에 암호코드 넣음
    ls = arr[row][col-55:col+1]

    code_num_ls = []
    for i in range(0, 56, 7):
        code_num = ''.join(ls[i:i+7])
        code_num_ls.append(code_num)
    # print(code_num_ls)

    # 검증코드가 올바른 코드인지 살펴 보기
    verification_ls = []
    # 홀수자리
    verifi_odd = 0
    # 짝수자리
    verifi_even = 0
    for i in range(len(code_num_ls)):
        number = code[code_num_ls[i]]
        verification_ls.append(number)
        # 홀수자리 -> idx라서 짝수
        if i % 2 == 0:
            verifi_odd += number
        # 짝수자리
        else:
            verifi_even += number
    # print(verification_ls)
    # print(verifi_odd, verifi_even)

    # 조건을 만족하면 answer에 대입
    if (verifi_odd * 3 + verifi_even) % 10 == 0:
        answer = verifi_odd + verifi_even
    # 아니면 0
    else:
        answer = 0

    print(f'#{test_case} {answer}')