T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = input()
    result = 0
    cnt = 0
    for char in data:
        if char == '1':
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            cnt = 0
    if result < cnt:
        result = cnt
    print(f'#{tc} {result}')