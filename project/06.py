import json
from pprint import pprint
# 아래 코드 수정 금지
movies_json = open("PJT-01/data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
list1 = ['id', 'title', 'overview', 'vote_average', 'genre_ids', 'poster_path']
# movies_list [{},{},{},{},{}....]
# list 없으면 key-value 삭제
for i in movies_list: 
    for a in list(i):         
        if a not in list1: 
            i.pop(a)  
pprint(movies_list)