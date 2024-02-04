arr = [1, 6, 11, 5, 7, 4, 2, 6, 8]
n = len(arr)

# 비교할 대상중 앞 index는 처음부터 n-1번째 까지
for i in range(n-1):
    # 비교할 대상중 뒤 index는 i+1부터 n번째 까지
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)