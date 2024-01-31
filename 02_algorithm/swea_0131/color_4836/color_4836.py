import sys
sys.stdin = open('sample_input.txt')

# import pprint
# pp = pprint.PrettyPrinter(indent=4)

T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    colors = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(colors)

    # 10 x 10 격자를 0으로 채워넣음
    arr = [[0] * 10 for _ in range(10)]
    # 보라색 색상의 갯수
    purple = 0
    # colors에 있는 원소들을 차례로 반복
    for color in colors:
        # color : 왼쪽위 좌표값(color[0], color[1]), 오른쪽 아래 좌표값(color[2], color[3]), 색이 들어있는 list(color[4])
        # row : 세로(행)길이 만큼 반복
        for row in range(color[2] - color[0] + 1):
            # col : 가로(열)길이 만큼 반복
            for col in range(color[3] - color[1] + 1):
                # arr[row][col]에 각 색상을 더해줌
                arr[color[0]+row][color[1]+col] += color[4]
                # 빨강과 파랑이 다들어 오면
                if arr[color[0]+row][color[1]+col] >= 3:
                    purple += 1
        # pp.pprint((arr))
    # 이쁘게 뽑기
    # pp.pprint((arr))
    # print(arr)
    print(f'#{test_case} {purple}')