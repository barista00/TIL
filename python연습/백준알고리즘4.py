# 홀수 (2576)
# 7개의 자연수 들어온다
# 홀수만 골라 다 더한다 출력
# 홀수 중 가장 작은 수 출력
arr = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        arr.append(num)
if len(arr) == 0:
    print(-1)
else:
    arr.sort()
    print(sum(arr))
    print(arr[0])

# 더하기(10822)
nums = list(map(int,input().split(',')))
print(sum(nums))

# 학점계산(2754)
score = {
    'A+':4.3,'A0':4.0,'A-':3.7,
    'B+':3.3,'B0':3.0,'B-':2.7,
    'C+':2.3,'C0':2.0,'C-':1.7,
    'D+':1.3,'D0':1.0,'D-':0.7,
    'F': 0.0
}
point = input()
print(score[point])

# 다이얼(5622)
p_number = {
    'ABC': 3, 'DEF': 4, 'GHI': 5,
    'JKL': 6, 'MNO': 7, 'PQRS': 8,
    'TUV': 9, 'WXYZ':10
}
call = list(map(str,input()))
a = 0
for i in p_number:
    for j in call:
        if j in i:
            a = a + p_number[i]
print(a)

# 숫자의 개수(2577) import로도 풀어보기
cal_num = 1
for i in range(3):
    num = int(input())
    cal_num = cal_num * num
num_dict = {
    '0':0,'1':0,'2':0,'3':0,
    '4':0,'5':0,'6':0,'7':0,
    '8':0,'9':0
}
str_cal_num = str(cal_num)
a = 0
for i in str_cal_num:
    if i in num_dict:
        num_dict[i] = num_dict[i] + 1
for i in num_dict:
    print(num_dict[i])

# 회사에 있는 사람(7785)
T = int(input())
dict = {}
for t in range(1, 1+T):
    in_out = input().split()
    dict[in_out[0]] = in_out[1] 
lst = []
for i in dict:
    if dict[i] == 'enter':
        i.lower()
        lst.append(i)
# 대문자, 소문자는 그냥 정렬하면 안되네
lst.sort()
for i in lst[::-1]: # 역순으로 출력하기
    for j in i:
        j[0].upper() # 리스트 데이터들 앞글자 대문자 변경
    print(i)

