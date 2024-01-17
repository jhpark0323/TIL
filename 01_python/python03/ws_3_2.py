number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

user_info = {}

def create_user(name, age, address):
    increase_user()
    global user_info
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    
    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')
result = create_user('홍길동', 30, '서울')
print(result)
print(f'현재 가입 된 유저 수 : {number_of_people}')