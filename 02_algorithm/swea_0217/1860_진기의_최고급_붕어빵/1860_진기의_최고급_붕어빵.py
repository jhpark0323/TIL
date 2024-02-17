import sys
sys.stdin = open('input.txt')

'''
손님이 들어온 시간에 남아있는 붕어빵 갯수
ex) 1번 test_case : 2명의 손님이 각각 3, 4초에 들어옴    2초에 2개씩 붕어빵을 만들수 있음
손님이 3에 들어왔으면  (3 // 2) * 2 만큼의 붕어빵을 만들어 놓을 수 있음
손님이 들어오면 붕어빵 갯수 -1 -> 다음 붕어빵의 갯수는 얼마나 더 채워야 함?
(4 // 2) * 2 - (3 // 2) * 2 이만큼 채워지나?

그럼 반복문을 사람수만큼 돌리고 사람이 들어왔을 때 붕어빵 채우고 줄수있는지 비교
'''

T = int(input())

for test_case in range(1, T+1):
    # n명의 손님, m초후 k개를 만들수 있음
    n, m, k = map(int, input().split())
    # 손님이 도착하는 시간 list
    ls = list(map(int, input().split()))

    # 손님이 오는 시간 순서대로 정렬
    ls.sort()

    bungeo = 0
    answer = 'Possible'
    # 손님 한명씩 옴
    for i in range(len(ls)):
        # i초후에 손님이 왔을 때 그 때까지 붕어빵은 m초마다 k개씩 만드므로 저만큼 만들수 있음
        bungeo += (ls[i] // m) * k - (i+1)

        # 붕어빵이 음수가 되면 실패
        if bungeo < 0:
            answer = 'Impossible'
            break

    # 반복문 종료 후 answer의 변화 보기
    print(f'#{test_case} {answer}')
