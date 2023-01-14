import requests
from pprint import pprint


def search_movie(title):
    # url에 필수로 적어야하는 인증키랑 다른게 또 있는지 Query String 확인잘하자(required)
    url = f'https://api.themoviedb.org/3/search/movie?api_key=필수로적을인증키&query={title}'
    response = requests.get(url)
    final = response.json()
    if final['results'] == []:
        return None
    else:
        return final['results'][0]['id']
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
