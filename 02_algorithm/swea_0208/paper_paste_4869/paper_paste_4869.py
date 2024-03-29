import sys
sys.stdin = open('sample_input.txt')

'''
1. n을 10으로나눈 몫을 기준으로 설명함
2. 두가지의 경우로 나눠서 그 두개를 합함
3. 함수를 f(n)이라 하자.
4. 맨앞에 가로의 길이가 1인 부분을 제외한 나머지는 총 f(n-1)개를 만들 수 있음.
-> 맨앞을 20x10짜리로 채우고 나머지를 채우는 경우의 수는 전항의 갯수와 같음
-> 맨앞 하나 빼면 나머지의 가로 길이는 n-1일것이기 때문
5. 맨앞의 가로의 길이가 2인 부분을 제외한 나머지는 총 f(n-2)개를 만들 수 있음.
-> 4번과 비슷한 이유
-> 그리고 맨앞의 가로의 길이가 2인 부분은 f(2)로 3개의 경우가 나오지만
-> 20x10을 세로로 두개 붙인건 4번의 경우의 수에서 계산을 했기 때문에 제외
-> 총 2개의 경우의수로 셈
6. 나머지는 4번과 5번으로 전부 만들수 있기에 더이상 만들게 없음
7. 그러므로 식은 f(n) = f(n-1) + 2f(n-2)로 만들 수 있따!!
'''

def f(n):
    n //= 10
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 3

    for i in range(3, n+1):
        # 이런 규칙을 가지고 있더라~ -> 그림으로 그렸었음
        f[i] = f[i-1] + 2 * f[i-2]

    return f[n]

T = int(input())

for test_case in range(1, T+1):
    # 가로의 길이 n
    n = int(input())

    print(f'#{test_case} {f(n)}')

