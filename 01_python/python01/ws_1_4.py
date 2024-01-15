# 원주율
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
radius = 15

pi_str = '원주율 : '
radius_str = '반지름 : '
round_str = '원의 둘레 : '
area_str = '원의 넓이 : '

round = radius * 2 * pi
area = (radius ** 2) * pi
print(f'{pi_str}{pi}')
print(f'{radius_str}{radius}')
print(f'{round_str}{round}')
print(f'{area_str}{area}')