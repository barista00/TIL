import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
movie_list = ['id', 'title', 'overview', 'vote_average', 'genre_ids']
movie_info = {}
for i in movie:
    if i in movie_list:
        movie_info[i] = movie[i]
pprint(movie_info)