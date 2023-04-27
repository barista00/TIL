import requests
from pprint import pprint

def popular_count():
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=2f09c337bcd7d89574fbb26c60f58b98'
    response = requests.get(url)
    final = response.json()
    return len(final['results'])
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
