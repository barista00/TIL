# if문 - 특정 조건에서만 코드 실행하고 싶을 때 사용
# 2가지 사용법 
# 1. 부등호사용 < > = true발견시 코드작동
# 2. if 찾는거 in list (list안에 찾는거 있냐) 있으면 동작 (있으면 true가 되겠지)

# 1번 if문
a = 9

if a > 10:
    print('big')
else:
    print('small')

# 2번 if문

a = ['김치', '쌀', '고기']

if '고기' in a:
    print('고기있음')
elif '김치' in a:
    print('김치있음')
else:
    print('굶어라')
# elif, else는 위에서 참에 걸리면 더이상 동작하지 않는다

# for반복문 
# 쓰는 이유는 
# 1. 같은 코드 여러번 반복 해야하는 경우
# 2. list안에 데이터를 하나씩 꺼낼 때 사용
# 2번에서 i는 데이터하나하나의 데이터를 의미한다

# 1번 for문
# for i in 반복할범위(몇번): 코드
for i in range(0,10):
    print(i)


# 2번 for문 (데이터꺼내기)
# for i in list: 코드 (list의 데이터 개수 만큼 반복된다)
car = ['k3', 'k5', 'k7']

for i in car:
    print(i)

# for문 안에 if가 참이여서 continue가 동작되면 다시처음으로 돌아감 false면 실행함 (조건으로 걸어놓은 횟수 끝날 떄 까지 돌림)
# break는 아예 끝내버림

