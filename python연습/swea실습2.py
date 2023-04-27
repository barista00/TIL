# 문제 1
a = input()
print(a.upper())

# 문제 2
T = int(input())
a = 0
for i in range(1,1+T):
    a = a + i
print(a)

# 문제 3
# 가위 1 바위 2 보 3 A, B두명이 숫자를 내고 이긴사람출력
T, N = list(map(int,input().split()))
if T - N == -2 or T - N == 1:
    print('A')
else :
    print('B')

# 문제 4
a = ['#++++','+#+++','++#++','+++#+','++++#']
for i in a:
    print(i)


# 문제 5
num = input()
a = 0
for i in tuple(num):
    a = a + int(i)
print(a)

# 문제 6
a = int(input())
b = 2
for i in range(a+1):
    print(b ** i, end=" ")