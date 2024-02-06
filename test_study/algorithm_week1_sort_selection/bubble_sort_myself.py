# 버블정렬

arr = [1, 6, 3, 5, 7, 4, 2, 6, 8]
n = len(arr)

# 마지막 index를 기준으로 반복문 진행
for end in range(n - 1, -1, -1):
    # 매 반복문 돌때 마다 0번 index부터 end번 index까지 순회
    for start in range(end):
        # 앞뒤 두개씩 비교하며 전항이 더 크면 두개의 자리를 바꿈
        if arr[start] >= arr[start+1]:
            arr[start], arr[start+1] = arr[start+1], arr[start]

print(arr)