# 이진 탐색

find = 30
n = 400
# --------------------

start = 1
end = 400

cnt = 0

while start <= end:
    mid = (start + end) // 2
    # print(mid)

    if mid == find:
        cnt += 1
        print(cnt)
        break

    # mid가 찾는수보다 크면 찾는수는 mid를 중심으로 그보다 작은수에 위치
    elif mid > find:
        end = mid - 1
        cnt += 1
    # mid가 찾는수보다 작으면 찾는수는 mid를 중심으로 그보다 큰 수에 위치
    else:
        start = mid + 1
        cnt += 1
