def recur_example(number):
    '''
        함수(2) 실행
            number에 2 할당
            if 2 == 1 조건문 만족하지 않음
            else문 2 + 함수(2-1) 
                결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

                함수(2-1) 실행
                    number에 1 할당
                    if 1 == 1 조건문 만족하므로 1 반환
            
            else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
            2 + 1 반환
        결과 : 3  
    '''
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if number < 10:
        return number
    else:
        remainder = number % 10
        number //= 10
        return remainder + sum_of_digits(number)
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6