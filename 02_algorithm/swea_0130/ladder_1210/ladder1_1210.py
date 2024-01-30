import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):

    testcase = int(input())

    # arr 만들 때 첫번째와 마지막열에 (1x100)인 0행렬 추가 -> index out of range 뜰까봐
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    '''
    1. 2차원 행렬 arr의 첫번째 원소 즉, 맨 첫줄을 모두 순회한다.
    2. 시작시 현재위치를 한칸 내린다.
    3. 현재위치의 좌우를 확인 후 1이 있는곳으로 현재위치를 이동 시킨다.
    4. 이때 좌 또는 우측으로 한번에 끝까지 이동한다 -> 안그러면 다음 반복문 돌때 조건문에서 이상하게 걸릴수 있음.
    5. 끝까지 이동 후 현재위치를 한칸 내린다.
    6. 좌우에 1이 없을 경우 현재위치를 한칸 내린다.
    '''



    # arr의 첫번째 원소를 모두 한번씩 확인한다.

    current = arr[0][0]
    for start in range(1, 101):
        # arr을 좌우로 한칸씩 늘렸기에 답을 구할 때는 start에서 1 빼준다.
        answer = start - 1
        if arr[0][start] == 1:
            current = arr[1][start]
            row = 1
            # start열에서 부터 반복문 시작
            while 1:
                # 왼쪽이 1일 때
                if arr[row][start-1] == 1:
                    # start를 1 뺌
                    start -= 1
                    # current = arr[row][start]
                    # left_col = start-2
                    while 1:
                        # 현재 위치를 원래의 왼쪽으로 바꿈
                        current = arr[row][start]
                        # 다시 왼쪽이 1인지 확인
                        if arr[row][start-1] == 1:
                            # 1이면 start를 1뺌
                            start -= 1
                        # 왼쪽이 1이 아닐 경우 현재 위치를 한칸 내리고 왼쪽으로 가는 조건문 나감
                        else:
                            row += 1
                            current = arr[row][start]
                            break

                # 오른쪽이 1일 때
                elif arr[row][start+1] == 1:
                    # 현재 위치를 원래의 오른쪽으로 바꿈
                    # 조건문의 시작이 왼쪽부터 확인하기 때문에 오른쪽으로 들어왔으면 오른쪽부터 쭉 검사함
                    start += 1
                    # current = arr[row][start+1]
                    # right_col = start+2
                    while 1:
                        # 현재위치를 원래의 오른쪽으로 바꿈
                        current = arr[row][start]
                        # 다시 오른쪽이 1인지 확인
                        if arr[row][start+1] == 1:
                            # 1이면 start를 1뺌
                            start += 1
                        # 오른쪽이 1이 아닐경우 현재위치를 한칸 내리고 오른쪽으로 가는 조건문 나감
                        else:
                            row += 1
                            current = arr[row][start]
                            break
                # 좌우가 1이 아닐 때
                else:
                    row += 1
                    current = arr[row][start]

                # 도착
                if current == 2:
                    break

                # 맨 아래까지 왔지만 2가 아니므로 다음 start로 반복문 시작
                if row+1 == 100:
                    break
        if current == 2:
            break

    print(f'#{testcase} {answer}')