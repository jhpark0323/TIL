
alpha = {
    'A' : 1010,
    'B' : 1011,
    'C' : 1100,
    'D' : 1101,
    'E' : 1110,
    'F' : 1111,
}

def f(i):
    bin_num = bin(i)[2:]
    if len(bin_num) != 4:
        bin_num = '0' * (4-len(bin_num)) + bin_num

    return bin_num


T = int(input())

for test_case in range(1, T+1):
    n, num = list(input().split())
    n = int(n)
    # print(n, num)

    ans = ''
    # n자리수 순회
    for i in num:
        if i.isdigit():
            ans += f(int(i))

        else:
            ans += str(alpha[i])

    print(f'#{test_case} {ans}')