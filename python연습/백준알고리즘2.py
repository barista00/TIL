# 더하기(9085)
T = int(input())
plus = 0
for t in range(1,1+T):
    num = int(input())
    numbers = list(map(int,input().split()))
    for i in numbers:
        plus += i
    print(plus)
    plus = 0

# 네 수(10824)
str_num = input().split()
front = str_num[0]+str_num[1]
back = str_num[2]+str_num[3]
print(int(front)+int(back))

# 네 번째 점(3009)
xlst = []
ylst = []
for i in range(3):
    x, y = map(int,input().split())
    xlst.append(x)
    ylst.append(y)
def one(a):
    for i in a:
        if a.count(i) == 1:
            print(i, end=" ")
one(xlst)
one(ylst)

# A + B - 5(10952)
while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)

# 더하기 사이클(1110)
N = input()
N_int = int(N)
count = 0
while True:
    a = N_int % 10
    b = N_int // 10 + N_int % 10
    compare = (a * 10) + (b % 10)
    count += 1
    if str(compare) == N:
        break
    else:
        N_int = compare
print(count)