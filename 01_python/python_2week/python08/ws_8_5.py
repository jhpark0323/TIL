class Dog():
    sound = '멍멍'
    

class Cat():
    sound = '야옹'
    

class Pet(Dog, Cat):
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

# class Pet(Cat, Dog):
#     def __str__(self):
#         return f'애완동물은 {self.sound} 소리를 냅니다.'

dog1 = Pet()
print(dog1)