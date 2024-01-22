from unittest import result


number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


user_info = {}
def create_user(name, age, address):
    increase_user()
    global user_info
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    
    return user_info


many_user = list(map(create_user, name, age, address))

# print(many_user)

number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수 : {number_of_book}')


info = list(map(lambda x: {'name' : x['name'], 'age' : x['age']}, many_user))
# print(info)


def rental_book(info):
    decrease_book(info['age'] // 10)
    print(f"{info['name']}님이 {info['age'] // 10}권의 책을 대여하였습니다.")


a = map(rental_book, info)
b = list(a)
# print(b) -> 이게 없어야 되네 이걸몰랐네