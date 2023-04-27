# 유학 금지(2789)
string = input()
for i in string:
    if i not in 'CAMBRIDGE':
        print(i, end="")

# 문자열 반복(2675)
T = int(input())
for t in range(1, 1 + T):
    problem = input().split()
    for i in problem[1]:
        print(i*int(problem[0]),end="")
    print('')

# 팰린드롬인지 확인하기(10988)
string = input()
if string == string[::-1]:
    print(1)
else:
    print(0)

# 태보태보 총난타(17249)
taebo = input()
a = 0
for i in taebo:
    if i == '@':
        a += 1
    elif i == '(':
        print(a, end=" ")
        a = 0
print(a)

# 크로아티아 알파벳(2941)
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
N = input()
for i in lst:
    N = N.replace(i,'a') # 크로아티아 단어를 그냥 한단어로 바꿔버림 하나의 단어를 1개로 인식 하기만 하면 되는거임 
print(len(N))

# 알파벳찾기(10809)
import string # string 모듈불러오기
alpha = string.ascii_lowercase
N = input()
for i in alpha:
    if i in N:
        print(N.index(i), end=" ") # 인풋문자에 알파벳의 위치출력
    else:
        print(-1,end=" ")

