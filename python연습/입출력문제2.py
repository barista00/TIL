# 문제 1
a = list(map(int,input().split()))
for i in a:
    print(i, end=" ")

# 문제 2
text = input().split()
for i in text:
    print(i, end=" ")

# 문제 3
T = int(input())
for t in range(1, 1+T):
    a = int(input())
    for i in range(a):
        b = int(input())
        print(b)

# 문제 4
T = int(input())
for t in range(1, 1+T):
    a = int(input())
    for i in range(a):
        n,m = list(map(int,input().split()))
        print(n, m)

# 문제 5
for i in range(1, 10):
    print(input())

# 문제 6
T = int(input())
for t in range(1, 1+T):
    n = int(input())
    for i in range(n):
        num = list(map(int,input().split()))
        for a in num:
            print(a, end=" ")

# 문제 7
T, N = list(map(int,input().split())) # 테스트 케이스 수

for t in range(1, T+1):
    a = int(input())
    for i in range(N):
        print(a)

# 문제 8
T, N = list(map(int,input().split())) # 테스트 케이스 수

for t in range(1, T+1):
    for i in range(N):
        # 이하 입력 코드
        a, b = list(map(int,input().split()))
        print(a, b)

# 문제 9
T, N = list(map(int,input().split()))
for t in range(1,1+T):
    for i in range(N):
        a, b, c = list(map(int,input().split()))
        print(a,b,c)