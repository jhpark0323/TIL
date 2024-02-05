import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    word = input()

    # 슬라이싱 안쓰고? 근데 쓴거같은데... 이 방법이 아닝가?
    new_word = ''
    for i in word:
        new_word = i + new_word

    # print(new_word)

    answer = 0
    if word == new_word:
        answer = 1

    print(f'#{test_case} {answer}')