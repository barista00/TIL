# 문제 1
number = int(input('숫자입력해주세요'))
print(number + 10)

# 문제 2
food = input('좋아하는음식 입력해주세요')
print('좋아하는음식 : ' + food)

# 문제 3
name = input('이름을 입력해주세요 > ')
born = int(input('태어난 년도를 입력해주세요 > '))
years = str(2023 - born)
print('저의 이름은 ' + name +'이고, 올해 나이는', years + '살 입니다.')

# 문제 4
sen1 = input('첫번째 문장을 입력해주세요 > ')
sen2 = input('두번째 문장을 입력해주세요 > ')
print(sen1 + sen2)

# 문제 5
number1 = input('정수형 숫자를 입력해주세요 > ')
print(int('-'+ number1))

# 문제 6
num1 = int(input('첫번째 정수형 숫자를 입력해주세요 > '))
num2 = int(input('두번째 정수형 숫자를 입력해주세요 > '))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)

# 문제 7
number1 = int(input('첫번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두번째 정수형 숫자를 입력해주세요 > '))
number3 = int(input('세번째 정수형 숫자를 입력해주세요 > '))
print(int((number1 + number2 + number3)/3))

# 문제 8
list = []
int1 = int(input('첫번째 정수형 숫자를 입력해주세요 > '))
int2 = int(input('두번째 정수형 숫자를 입력해주세요 > '))
int3 = int(input('세번째 정수형 숫자를 입력해주세요 > '))
int4 = int(input('네번째 정수형 숫자를 입력해주세요 > '))
int5 = int(input('다섯번째 정수형 숫자를 입력해주세요 > '))
list.append(int1)
list.append(int2)
list.append(int3)
list.append(int4)
list.append(int5)
print(list)

# 문제 9
str = input('문자열을 입력해주세요 > ')
int = int(input('정수형 숫자를 입력해주세요 > '))
print(str * int)

# 문제 10
정수1 = int(input('첫번째 정수형 숫자를 입력해주세요 > '))
print(정수1)
정수2 = int(input('두번째 정수형 숫자를 입력해주세요 > '))
print(정수1 + 정수2)
정수3 = int(input('세번째 정수형 숫자를 입력해주세요 > '))
print(정수1 + 정수2 + 정수3)
정수4 = int(input('네번째 정수형 숫자를 입력해주세요 > '))
print(정수1 + 정수2 + 정수3 + 정수4)
정수5 = int(input('다섯번째 정수형 숫자를 입력해주세요 > '))
print(정수1 + 정수2 + 정수3 + 정수4 + 정수5)