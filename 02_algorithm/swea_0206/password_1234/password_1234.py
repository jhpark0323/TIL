import sys
sys.stdin = open('input.txt')

# 재귀 쓰고싶어서 걍 함수 씀
def password(ls):
    for i in range(len(ls) - 1):
        # 순회하며 뒤에꺼랑 앞에꺼랑 같아?
        if ls[i] == ls[i+1]:
            # 그럼 그두개 지워
            del ls[i:i+2]
            # print(ls)

            # 근데 바로 break해줘야함 안그럼 index에러남
            break

    # break가 안걸리면 더이상 할게 없으므로 걍 ls return해라.
    else:
        return ls
    # 근데 break걸려서 나왔으면 한번더 해야할 수도 있기 때문에 다시 password에 넣어라.
    return password(ls)


T = 10

for test_case in range(1, T+1):
    n, pw = map(int, input().split())

    # pw_str에 pw의 각각을 원소로하는 list를 할당
    pw_str = list(str(pw))
    # print(pw_str)

    # print(password(pw_str))

    answer = int(''.join(password(pw_str)))
    print(f'#{test_case} {answer}')
