# import sys
# sys.stdin = open('sample_input.txt')
#
# hexadecimal = {
#     'A' : 10,
#     'B' : 11,
#     'C' : 12,
#     'D' : 13,
#     'E' : 14,
#     'F' : 15
# }
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     # n : 자리수, n자리 16진수
#     ls = list(input().split())
#     n = ls[0] = int(ls[0])
#     # print(ls)
#
#     # 16진수 거꾸로 뒤집기
#     hexa_num = ls[1][::-1]
#
#     answer = 0
#     for i in range(n):
#         # hexadecimal에 있는 문자면
#         if hexa_num[i] in hexadecimal:
#             # dict에서 꺼내서 16의 i승만큼 곱해라
#             answer += hexadecimal[hexa_num[i]] * (16 ** i)
#         else:
#             answer += int(hexa_num[i]) * (16 ** i)
#
#     # print(answer)
#
#     bin_answer = []
#
#     while answer:
#         bin_answer.append(str(answer % 2))
#         answer //= 2
#
#     while len(bin_answer) % 4 != 0:
#         bin_answer.append('0')
#
#     # print(bin_answer[::-1])
#     print(f'#{test_case}', ''.join(bin_answer[::-1]))



import sys
sys.stdin = open('sample_input.txt')

hexadecimal = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
}

# 이진수 변환 코드
def bin_num(k):
    # 여기에 담음
    bin_answer = []

    # k를 숫자로 바꿈
    if k in hexadecimal:
        k = hexadecimal[k]
    else:
        k = int(k)

    # k가 0이면 0000 반환
    if k == 0:
        return '0000'

    # 2진수 변환 코드
    while k:
        bin_answer.append(str(k % 2))
        k //= 2
    # 4칸 맞춰서 0채우기
    while len(bin_answer) % 4 != 0:
        bin_answer.append('0')
    return ''.join(bin_answer[::-1])

T = int(input())

for test_case in range(1, T+1):
# n : 자리수, n자리 16진수
    ls = list(input().split())
    n = ls[0] = int(ls[0])
    # print(ls)

    hexa_num = ls[1]

    # 16진수에서 2진수로 바꿀때 각 자리를 2진수로 바꿔서 붙이면 됨
    answer = ''
    for i in hexa_num:
        answer += bin_num(i)

    print(f'#{test_case} {answer}')

