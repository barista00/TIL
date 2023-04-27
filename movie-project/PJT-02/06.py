import requests
from pprint import pprint


def credits(title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key=2f09c337bcd7d89574fbb26c60f58b98&query={title}' # 영화제목검색 url
    response = requests.get(url) # 제목을 적고 데이터를 요청해서 받는다 
    final = response.json()
    # movie_id = final['results'][0]['id'] 이 위치에서 있었을 때(list index out of range오류남)
    # 알수없음을 넣은 결과에서 출력 결과물이 다르기 때문에 해당 인덱싱을 적용할 수 없어서 생긴 에러이다. 15번줄로 넣으면 해결된다
    # 파이썬이 위에서 한줄씩 차례대로 읽는점을 잊지말자
    dict = {'cast' : [], 'crew' : []} # 딕셔너리 안 리스트에 append 할 수 있음
    if final['results'] == []:
        return None
    else:
        movie_id = final['results'][0]['id']
        url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=2f09c337bcd7d89574fbb26c60f58b98' # 영화의 id번호를 이용해 배우, 스태프목록 url만들기
        response2 = requests.get(url2)
        final2 = response2.json()
        for i in final2['cast']:
            if i['cast_id'] < 10:
                dict['cast'].append(i['name'])
        for a in final2['crew']:
            if a['department'] == 'Directing':
                dict['crew'].append(a['name'])
        return dict
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
