import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("PJT-01/data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
# movie(dictionary) genre_ids : [18, 80] // genre_list(list) id의 value같은거 name value출력
a = []
for i in genres_list:
    if i['id'] in movie['genre_ids']: # dictionary['id']
        a.append(i['name'])
print(a)