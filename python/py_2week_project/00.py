import requests
from pprint import pprint
url = 'https://api.bithumb.com/public/ticker/BTC_KRW' # 원화로 현재가 정보 조회 데이터 url
response = requests.get(url) # 데이터 주세요 찡찡
final = response.json() # 데이터를 json형식으로 해주셈

# closing price 뽑아내기
print(final['data']['closing_price'])
# 23581000