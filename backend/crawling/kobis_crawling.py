import json
import requests
from pprint import pprint
# kobis api_key
API_KEY = 'c309e1e47c7986fa2e7c766e365c506a'
### 주간 박스오피스 
def weekly_boxoffice(target_data):
  url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
  params = {
    'key': API_KEY,
    'targetDt': target_data,
    'weekGb': '0',
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json().get('boxOfficeResult')
    pprint(data)
    return data
  else:
    print('error', response.status_code)

### 영화 상세정보
def detail(movie_code):
  url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
  params = {
    'key': API_KEY,
    'movieCd': movie_code,
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json().get('movieInfoResult').get('movieInfo')
    return data
  else:
    print('error', response.status_code)