# 문제 1
int = int(input('정수를 입력하세요 > '))
if int > 0:
    print('True')
else:
    print('False')

# 문제 2
first = int(input('첫번째 정수입력하세요 > '))
second = int(input('두번째 정수입력하세요 > '))

if first > second:
    print(first)
elif first < second:
    print(second)
else :
    print('False')

# 문제 3
num = int(input('정수를 입력하세요 > '))
if num > 1 and num < 10:
    print('True')
else :
    print('False')

# 문제 4
num = int(input('정수를 입력하세요 > '))
if num > 0 and (num % 2 == 0):
    print('True')
else :
    print('False')

# 문제 5
num = int(input('정수를 입력하세요 > '))
if num > 100 or num < 0:
    print('error')
elif num > 60:
    print('합격')
else:
    print('불합격')

# 문제 6 
text = input('문자열을 입력하세요 > ')
text1 = text[::-1]
for i in text1:
    print(i)

# 문제 7
num1 = int(input('첫번째 정수 입력하세요 > '))
num2 = int(input('두번째 정수 입력하세요 > '))
if num1 < num2 :
    for i in range(num1+1,num2):
        print(i)
elif num1 > num2 :
    for i in range(num2+1, num1):
        print(i)
else :
    print('False')

# 문제 8 
num1 = int(input('첫번째 정수 입력하세요 > '))
num2 = int(input('두번째 정수 입력하세요 > '))
renum1 = range(num1+1, num2)[::-1]
renum2 = range(num2+1, num1)[::-1]
if num1 < num2 :
    for i in renum1:
        print(i,end='')
elif num1 > num2 :
    for i in renum2:
        print(i,end='')
else :
    print('False')

# 문제 9
num = int(input('정수를 입력하세요 > '))
if num < 0:
    print('False')
for i in range(1, num):
    if i % 2 == 0:
        continue
    print(i)

# 문제 10
단수 = 2
곱하기수 = 1
for a in range(8):
    for i in range(1,9):
        print(f'{단수+a} X {곱하기수+i} = {(단수+a)*(곱하기수+i)}')