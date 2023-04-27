# 이상한 곱셈(1225)
n, m = map(str, input().split())
lst = list(n)
lst2 = list(m)
plus = 0
while lst:
    for i in lst2:
        plus += int(lst[-1]) * int(i)
    lst.pop()
print(plus)

# 별찍기 -1(2438)
N = int(input())
for i in range(1,1+N):
    print('*'*i)

# 구구단(2739)
N = int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}')

# 나는 요리사다(2953)
lst = []
for i in range(1,6):
    N = list(map(int, input().split()))
    lst.append((i, sum(N)))
lst2 = sorted(lst, key=lambda x:x[1])
print(*lst2[-1])

# 직사각형 네개의 합집합의 면적 구하기(2669)
arr = [[0]*100 for _ in range(100)] # 0으로된 리스트100개 x좌표 y좌표 100 X 100
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(b, d): # 행
        for j in range(a, c): # 열
            arr[i][j] = 1 # i 행에서 a~c-1까지 0을 1로 바꾸기 
lst2 = []
for i in arr:
    lst2.append(sum(i))
print(sum(lst2))