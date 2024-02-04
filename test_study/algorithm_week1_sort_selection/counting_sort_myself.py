arr = [1, 6, 11, 5, 7, 4, 2, 6, 8]
n = len(arr)

max_arr = max(arr)

# arr의 최댓값보다 1큰 0으로 이루어진 배열을 만들어 각 index에 arr의 원소들이 몇개 들어가있는지 센다.
counts = [0] * (max_arr + 1)

for i in arr:
    counts[i] += 1

print(counts)

for i in range(len(counts)):
    if i >1:
        counts[i] = counts[i-1] + counts[i]

print(counts)
# [0, 1, 2, 2, 3, 4, 6, 7, 8, 8, 8, 9]

# 정렬할 새로운 배열 temp
temp = [0] * (n+1)

# counts에서 arr[i]가 있는 index -> temp의 그 index에도 arr[i]가 위치해있을 것
for i in range(n-1, -1, -1):
    temp[counts[arr[i]]] = arr[i]
    counts[arr[i]] -= 1  # counts의 arr[i]라는 원소가 있는 위치에 1을 뺸다
    print(counts)

print(temp[1:])