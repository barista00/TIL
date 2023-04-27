import requests
from pprint import pprint


def recommendation(title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key=2f09c337bcd7d89574fbb26c60f58b98&query={title}' 
    response = requests.get(url) # 제목을 적고 데이터를 요청해서 받는다 
    final = response.json() # json형태로 바꾼다
    a = []
    if final['results'] == []: # 영화제목이 없는 제목이면 None을 리턴한다
        return None
    else:   # 아니라면 처음 받은 데이터에서 id value값을 변수에 저장 
        id_num = final['results'][0]['id']
        reco_url = f'https://api.themoviedb.org/3//movie/{id_num}/recommendations?api_key=2f09c337bcd7d89574fbb26c60f58b98&language=ko-KR'
        response2 = requests.get(reco_url) # id value값을 이용해 추천영화목록을 요청한다
        recom = response2.json() # json으로 바꿔서 받는다
        for i in recom['results']: # 반복문을 이용해 추천영화 제목을 비어있는 리스트에 집어넣는다
            a.append(i['title'])
        return a
    # 여기에 코드를 작성합니다.



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
