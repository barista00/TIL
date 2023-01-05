# 실습 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.
# count() 함수는 사용하지마세요.
str = input('문자열을 입력하세요 > ')
a = 0
for i in str:
    if i == 'e':
        a += 1
print(a)

# 실습 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)
# count() 함수는 사용하지마세요.
str = input('문자열을 입력하세요 > ')
a = 0 
list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in str:
    if i in list:
        a += 1
print(a)    

# 실습 3
# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}
age = 2023 - int(dict_variable['생년']) + 1
print(f'나이 : {age}세')

# 실습 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.
dict = {}
name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
place = input('거주지를 입력하세요 > ')
dict['이름'] = name
dict['전화번호'] = num
dict['거주지'] = place
print(dict)
print(f'이름 : {name}')
print(f'전화번호 : {num}')
print(f'거주지 : {place}')

# 실습 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
info = {'정우영': 1}
input_info = {}
name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
mail = input('이메일을 입력하세요 > ')
place = input('거주지를 입력하세요 > ')
input_info['이름'] = name
input_info['전화번호'] = num
input_info['이메일'] = mail
input_info['거주지'] = place
info['정우영'] = input_info
print(info)

# 실습 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
text = input('문자열을 입력하세요 > ')
dictionary = {}
for i in text:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else :
        dictionary[i] = 1

for alpha, number in dictionary.items():
    print(alpha, number)