# 문제 1
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.
num = int(input('정수를 입력하세요 > '))
if num < 0:
    print(num * -1)
else:
    print(num)

# 문제 2
# 리스트 요소의 개수를 출력하세요
# len() 함수는 사용하지 마세요
list = [1, 3, -1, 6, 0]
a = 0
if list == []:
    print(0)
elif True :
    for i in list:
        a += 1
        continue
    print(a)

# 문제 3
# 리스트에 저장된 정수들의 합을 출력하세요
# sum() 함수는 사용하지 마세요
list = [1, 2, 3, 4, 5]
a = 0
for i in list:
    a = a + i
    continue
print(a)

# 문제 4
# 리스트에 저장된 정수들의 평균을 출력하세요
# len() / sum() 함수는 사용하지 마세요
list = [2, 3, 5, 7]
a = 0
b = 0
for i in list:
    a = a + i
    continue
for i in list: 
    b = b + 1
    continue
print(a/b)

# 문제 5
# 리스트에 저장된 정수들의 곱을 출력하세요
list = [-11, -21, 3]
a = 1
for i in list:
    a = a * i
    continue
print(a)

# 문제 6
# 양의 정수만 저장한 리스트가 주어집니다
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요
# max() 함수는 사용하지 마세요
list = [1, 10, 21, 11]
list.sort()
print(list[-1])

# 문제 7
# 양의 정수만 저장한 리스트가 주어집니다
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요
# max() 함수는 사용하지 마세요
list = [5, 5, 5, 2]
list.sort()
print(list[0])