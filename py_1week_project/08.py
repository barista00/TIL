import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("PJT-01/data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
movie_list = ['id', 'title', 'overview', 'vote_average', 'genre_names']
movie['genre_names'] = []
dict = {}

for i in movie:
    if i in movie_list:
        dict[i] = movie[i]
for a in genres_list:
    if a['id'] in movie['genre_ids']:
        dict['genre_names'].append(a['name'])

pprint(dict)
