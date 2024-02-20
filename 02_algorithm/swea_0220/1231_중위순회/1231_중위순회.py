import sys
sys.stdin = open('input.txt')

def inorder(t):
    global answer
    if t:
        inorder(left[t])
        # print(arr[t][1], end = '')
        answer += arr[t][1]
        inorder(right[t])

try:
    tc = 1
    while 1:
        n = int(input())
        # arr에 숫자는 int로, 문자는 str로 넣기
        arr = [[]]
        for i in range(n):
            a = list(input().split())
            for j in range(len(a)):
                if a[j].isdigit():
                    a[j] = int(a[j])
            arr.append(a)
        # print(arr)

        left = [0] * (n+1)
        right = [0] * (n+1)

        # left, right에 각각 넣기
        for i in range(1, n+1):
            # 길이가 3이상이면 자식 노드가 있음
            if len(arr[i]) >= 3:
                # 길이가 4면 left, right 다있음
                if len(arr[i]) == 4:
                    left[arr[i][0]] = arr[i][2]
                    right[arr[i][0]] = arr[i][3]
                # 길이가 3이면 left만 있음
                elif len(arr[i]) == 3:
                    left[arr[i][0]] = arr[i][2]

        # print('left :', left)
        # print('right :', right)
        answer = ''
        inorder(1)
        print(f'#{tc} {answer}')

        tc += 1

except:
    pass
