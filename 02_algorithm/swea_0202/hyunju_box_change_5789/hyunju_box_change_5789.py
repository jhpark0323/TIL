import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    # n개의 상자, q회 동안 상자 변경
    n, q = map(int, input().split())

    # 바꿀 범위의 왼쪽 오른쪽 끝값들을 담은 ls
    li_ri = [list(map(int, input().split())) for _ in range(q)]

    # box 설정 -> index 때문에 n+1개로 설정
    box = [0] * (n+1)
    
    # i번째 작업의 값을 i로 변경 하기 위해 초기값 i 설정
    i = 1
    # li_ri의 각 원소들을 start_end로 두고 start_end의 첫번째 원소를 li, 두번째 원소를 ri로 둠
    for start_end in li_ri:
        li, ri = start_end[0], start_end[1]

        # box의 li~ri까지의 index에 i를 할당
        box[li:ri+1] = [i] * (ri-li+1)
        # 다음작업시 i 1증가
        i += 1

    print(f'#{test_case}', *box[1:])




# a = [0]* 10
# a[1:5] = [3] * 4
# print(a)