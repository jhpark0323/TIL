import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    # 정수의 갯수
    n = int(input())

    # 수열
    a_i = list(map(int, input().split()))

    cnt = 0
    # 앞에서 부터 선택할 원소의 인덱스 i, 총 길이이보다 하나 전까지만 돌림
    for i in range(n-1):
        # 기준을 잡을 index변수를 i로 설정
        max_min_idx = i
        # 비교할 원소의 인덱스 j, i보다 1 큰수부터 끝까지
        for j in range(i+1, n):
            # 짝수번째 index에는 max값이 들어와야하므로 max값을 돌아다니면서 찾음
            if i % 2 == 0:
                if a_i[max_min_idx] < a_i[j]:
                    max_min_idx = j

            # 홀수번째 index에는 min값이 들어와야하므로 min값을 돌아다니면서 찾음
            else:
                if a_i[max_min_idx] > a_i[j]:
                    max_min_idx = j
                # min값을 찾고 나서 둘의 자리를 바꿈

        # max_min_idx를 설정한 후 위치 바꾸기
        a_i[i], a_i[max_min_idx] = a_i[max_min_idx], a_i[i]
        # print(a_i)

        cnt += 1
        if cnt == 10:
            break

    print(f'#{test_case}', *a_i[:10])