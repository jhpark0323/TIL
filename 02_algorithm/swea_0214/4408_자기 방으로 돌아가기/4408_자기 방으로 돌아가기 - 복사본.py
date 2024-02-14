import sys
sys.stdin = open('sample_input.txt')

'''
하나씩 빼서 계산 하는데 다른 경우들 중 현재방과 돌아갈 방이 빼서 계산할거에 포함 안되면 같이 빼면 될듯
근데 그 때 하나 더 빠질때마다 못움직이는 복도 update 해야할듯 -> 이걸 어케하지 -> 매번 배열 만들어서 visited로 만들까
while stack: 으로 푸는게 편할듯? -> list로 해서 하나씩 for문 돌리면 index 에러날듯
'''

def f(arr, n):
    # arr에 원소가 담겨있으면 계속 진행
    while arr:
        # 배열 바뀔때마다 새로 할당하고 방문해야할 곳 나타내기
        visited = [False] * (n)
        # 처음 나올 학생 (list로 이루어짐, 첫번째 원소는 현재방, 두번째 원소는 돌아가야할 방)
        first = arr.pop()
        # 처음 나온 학생이 가야할 복도의 위치 전부 update
        visited[first[0]:first[1] + 1] = True

        # 다음 학생들
        for next_stu in arr:
            # 다음 학생이 복도의 방문하지 않은 곳으로 간다면 그 학생도 같이 출발
            if not visited[next_stu[0]] and not visited[next_stu[1]]:

                go_with = arr.pop(next_stu)



T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

