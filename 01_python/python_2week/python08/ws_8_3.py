class Animal:
    num_of_animal = 0

# 아래 클래스를 수정하시오.
class Cat(Animal):
    def __init__(self, yaong):
        self.yaong = yaong

    def meow(self):
        print(f'{self.yaong} !')


cat1 = Cat("야옹")
cat1.meow()
