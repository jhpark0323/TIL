import sys
sys.stdin = open('GNS_test_input.txt')

# num_dict를 만듬
num_dict = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

'''
아 딴걸로 할걸...
시간복잡도 O(n^2)이라 개오래 걸림
'''

T = int(input())

for test_case in range(1, T+1):
    tc, num = input().split()
    num = int(num)
    ls = list(input().split())
    # print(tc, num)
    # print(ls)

    # bubble sort
    # 비교할 첫번째 -> 마지막꺼 보다 1개 적음
    for i in range(num - 1):
        # 비교할 두번째 대상 -> i+1부터 마지막
        for j in range(i+1, num):
            # 비교는 dict에 넣어서 진행
            if num_dict[ls[i]] > num_dict[ls[j]]:
                ls[i], ls[j] = ls[j], ls[i]
    print(tc)
    print(*ls)