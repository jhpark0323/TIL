import sys

sys.stdin = open('input.txt')

'''
1. ls_num에서 정렬하지 않은 수 중 제일 큰 수 찾기
2. ls_num의 처음 부터 돌면서 제일 큰 수 인지 확인
3. 맞으면 다음거 확인
4. 제일 큰 수가 안나오면 바꿈
5. 이렇게 돌며 맨 앞부터 정렬
'''

T = int(input())

for test_case in range(1, T + 1):
    # num : 숫자판의 정보, change : 교환 횟수
    num, change = input().split()
    ls_num = list(num)
    change = int(change)

    best = sorted(ls_num, reverse=True)

    # print(best)
    # print(ls_num)
    # print(change)

    # 교환 횟수 만큼 반복
    for i in range(change):
        # 이미 제일 좋은 경우를 발견 했으면
        if ls_num == best:
            max_num = max(ls_num)
            # 최댓값이 2개이상이면 그 두개만 바꿀 것이기 때문에 그대로 끝임
            if ls_num.count(max_num) >= 2:
                break

            # 끝에 두개만 계속 바꿔라
            ls_num[-1], ls_num[-2] = ls_num[-2], ls_num[-1]
            # print('best :', ls_num)

        else:
            # 돌면서 제일 큰수인지 확인 후 아니면 바꿈
            while 1:
                # i가 범위안에 있을 때
                if i < len(ls_num):
                    # 정렬 되지 않은 곳 부터 제일 큰 수를 찾음
                    max_num = max(ls_num[i:])
                    # 그 index는 뒤에서 부터 찾아야 함
                    max_index = len(ls_num) - 1 - ls_num[::-1].index(max_num)

                    # 제일 큰수 이면 다음 항 조사
                    if ls_num[i] == max_num:
                        i += 1
                    # 제일 큰 수가 아니면
                    else:
                        # 둘이 자리 바꿈
                        ls_num[i], ls_num[max_index] = ls_num[max_index], ls_num[i]
                        # print(ls_num)
                        break
                else:
                    # 끝에 두개만 계속 바꿔라
                    ls_num[-1], ls_num[-2] = ls_num[-2], ls_num[-1]
                    # print('yes')
                    break
            # print('else :', ls_num)


    print(f'#{test_case}', ''.join(ls_num))
