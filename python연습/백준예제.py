# 1
a, b = map(int,input().split())
print(a+b)

# 2
a = int(input())
b = int(input())

print(a+b)

# 3
T = int(input())

for t in range(1,1+T):
    a,b = map(int,input().split())
    print(a+b)

# 4
T = int(input())

for t in range(1,1+T):
    a,b = map(int,input().split(','))
    print(a+b)

# 5
T = int(input())

for t in range(1,1+T):
    a, b = map(int,input().split())
    print(f'Case #{t}: {a+b}')

# 6
T = int(input())

for t in range(1,1+T):
    a, b = map(int,input().split())
    print(f'Case #{t}: {a} + {b} = {a+b}')