# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요. 
str = input()
a = 0
for i in str:
    if 'e' not in str:
        print(-1)   
        break
    if 'e' != i :
        a += 1
    else:
        print(a)
        break

# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
sen = input().split()
dict = {}
for i in sen:
    if i in dict:
        dict[i] = dict[i] + 1
    else :
        dict[i] = 1

for a, b in dict.items():
    print(a, b)

# # 문제 3
# # 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
string = list(input()) 

for i in string:
    if 'e' == i:
        string.remove('e')
print(''.join(string))

# # 문제 4
# # 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요
a, b = input().split() # a 단어 b 알파벳
list_a = list(a)
c = 0
for i in list_a:
    if b == i:
        c += 1
print(c)

# # 문제 5
# # 단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.
sen = input()
for i in sen:
    if i != ' ':
        print(i, end="")
    else:
        print('-', end = "")

# # 문제 6 
# # 양의 정수를 입력받고, 자리수의 합을 출력하세요
# # 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요
# # 양의 정수를 문자열로 변경하지마세요
num = input()
a = 0
if int(num) < 0: 
    print(-1)
else :
    for i in tuple(num):
        a = a + int(i)
    print(a)

# while로 풀어보기
# 들어온 숫자를 10으로 나누고 나머지를 더하면 똑같은 결과를 얻을 수 있음
n = int(input())

if n < 0:
    print(-1)
else :
    result = 0
    while n > 0:
        result = result + n%10 # n에서 들어온 수를 10으로 나눈 나머지값 result에 넣음
        n //= 10 # 나눠줄 때마다 n을 10으로 나눠주고 다시 반복문 돌리고 반복
    print(result)