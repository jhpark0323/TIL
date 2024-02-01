import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # p : 전체 쪽 수, a : 찾을 쪽번호 Pa, b : 찾을 쪽 번호 Pb
    p, a, b = map(int, input().split())

    def binary_search(key):

        # 시작, 끝 인덱스 지정
        start = 1
        end = p

        cnt = 1

        # 시작 인덱스와 끝 인덱스를 조정하며 진행하다가 start >= end가 나올시 반복 종료
        while start <= end:

            # 중앙값 인덱스 지정
            middle = int((start + end) / 2)

            # middle과 key가 같으면 cnt바로 return
            if middle == key:
                return cnt

            # middle이 key보다 크면 middle보다 작은 부분을 다시 조사해야하므로 end값을 middle-1로 바꿈
            elif middle > key:
                end = middle

            # middle이 key보다 작으면 middle보다 큰 부분을 다시 조사해야하므로 start값을 middle+1로 바꿈
            else:
                start = middle

            cnt += 1
        # 못찾는 일은 없을듯 -> input값은 정수겟지? 전체쪽수가 나머지 두개 보다 크겠지?
        # 아니면 조건 다시 달면 됨

    a_cnt = binary_search(a)
    b_cnt = binary_search(b)

    if a_cnt < b_cnt:
        answer = 'A'
    elif a_cnt == b_cnt:
        answer = 0
    else:
        answer = 'B'

    print(f'#{test_case} {answer}')

