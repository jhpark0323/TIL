import sys

sys.stdin = open('input.txt')

def dfs(count):
    global max_result
    if count == change_count:  # 최대 교환 횟수에 도달했을 때
        max_result = max(max_result, int(''.join(card_list)))  # 현재의 최대 상금과 비교하여 갱신
        return

    for i in range(card_len):
        for j in range(i+1, card_len):
            card_list[i], card_list[j] = card_list[j], card_list[i]  # 두 카드의 위치 교환
            temp_key = ''.join(card_list)  # 현재 숫자 카드 리스트를 문자열로 변환
            if (temp_key, count) not in visited:  # 방문 여부 확인
                visited.add((temp_key, count))
                dfs(count + 1)  # 다음 단계로 이동
            card_list[i], card_list[j] = card_list[j], card_list[i]  # 다시 원래대로 복구

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    card, change_count = input().split()  # 숫자 카드 정보와 최대 교환 횟수 입력
    card_list = list(card)  # 숫자 카드를 리스트로 변환
    visited = set()  # 방문한 상태를 저장하기 위한 집합
    max_result = 0  # 최대 상금을 저장할 변수
    card_len = len(card_list)  # 숫자 카드의 길이
    change_count = int(change_count)  # 최대 교환 횟수를 정수로 변환
    dfs(0)  # DFS 호출
    print(f"#{test_case} {max_result}")  # 결과 출력
