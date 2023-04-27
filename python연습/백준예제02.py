# 10818
N = int(input())
integer = list(map(int,input().split()))
print(min(integer), max(integer))

# 11720
N = int(input())
numbers = tuple(input())
plus = 0
for i in numbers:
    plus = plus + int(i)
print(plus)

# 2750
T = int(input())
lst = []
for t in range(1,1+T):
    num = int(input())
    lst.append(num)
lst.sort()
for i in lst:
    print(i)

# 2562
lst = []
cnt = 0
for i in range(9):
    num = int(input())
    lst.append(num)
print(max(lst))
print(lst.index(max(lst))+1)