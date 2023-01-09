import json
from pprint import pprint
# 아래 코드 수정 금지
movies_json = open("PJT-01/data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
list_key = ['id', 'title', 'overview', 'vote_average', 'genre_ids', 'poster_path']
# movies_list [{},{},{},{},{}....]
# list 없으면 key-value 삭제
for i in movies_list: 
    for a in list(i):         
        if a not in list_key: 
            i.pop(a)  
pprint(movies_list)

# 딕셔너리를 반복문으로 돌리면서 딕셔너리 데이터에 변화를 주게되면 에러가 발생한다
# 그래서 딕셔너리를 반복문 돌릴 때 리스트로 일단 바꾸고 돌림
# 그럼 리스트가 딕셔너리의 key값만으로 이루어진 list로 변환되어 반복문이 돌아감
# key를 제거했다면 딕셔너리의 데이터도 같이 없어짐
# 반복문을 돌리는게 리스트이기 때문에 문제없이 해결이되는 것임
# 이것 역시 데이터타입 특징으로써 데이터타입을 잘 아는게 정말 중요한 것 같음