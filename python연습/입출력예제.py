# 문제 1
num = int(input())
print(num)

# 문제 2
sen = input()
print(sen)

# 문제 3
number = int(input())
for i in range(1, 1+number):
    print(i)

# 문제 4
numbers = list(map(int, input().split()))
print(numbers)

# 문제 5
a, b = map(int, input().split())
print(a, b)

# 문제 6
sen = input().split()
for i in sen:
    print(i, end =" ")

# 문제 7 
numbers = int(input())
for i in range(1, 1+numbers):
    print(i, end=" ")