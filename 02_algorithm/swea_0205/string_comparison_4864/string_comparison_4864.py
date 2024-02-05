import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    answer = 0

    # # 근데 뭔가 이렇게 풀면 안되겠찌??
    # if str1 in str2:
    #     answer = 1

    # str2에서 str1의 글자수를 빼서 1 더한만큼 반복 -> 가능한거 다 봄
    for i in range(len(str2) - len(str1) + 1):
        # 기준 str2에서 str1만큼의 길이만큼의 글자를 슬라이싱해서 str1과 같은지 확인
        if str2[i:i+len(str1)] == str1:
            answer = 1

    print(f'#{test_case} {answer}')