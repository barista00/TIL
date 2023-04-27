# 문제 1(몫과 나머지 출력하기)
T = int(input())

for t in range(1, 1+T):
    a, b = list(map(int, input().split()))
    c = a // b
    d = a % b
    print(f'#{t} {c} {d}')

# 문제 2(평균값 구하기)
T = int(input())
a = 0
for t in range(1, 1+T):
    numbers = list(map(int, input().split()))
    for i in numbers:
        a = a + i
        b = round(a/len(numbers))
        a = 0
    print(f'#{t} {b}')

# 문제 3(간단한 계산기)
a, b = list(map(int,input().split()))
def cal(q,w):
        print(q+w)
        print(q-w)
        print(q*w)
        print(q//w)
cal(a,b)

# 문제 4(스탬프 찍기)
T = int(input())
for t in range(1, 1+T):
    print('#',end="")

# 문제 5(최대 수 구하기)
T = int(input())
for t in range(1, 1+T):
    numbers = list(map(int,input().split()))
    print(f'#{t} {max(numbers)}')
