import json
import requests

API_KEY = '769830601abcc5047d5d1a90b40dc11c'

### popular movie  
# url = 'https://api.themoviedb.org/3/movie/popular'
# params = {
#   'language': 'ko',
#   'page': '500',
#   'api_key': API_KEY,
# }

### movie_id에 따른 details
movie_id = 653346
url = f'https://api.themoviedb.org/3/movie/{movie_id}'
params = {
  'language': 'ko',
  'api_key': API_KEY,
}



response = requests.get(url, params=params)

if response.status_code == 200:
  data = response.json()
  
  # 데이터 json 파일로 저장
  with open('detail.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
  print('저장 완료')
else:
  print('오류 발생', response.status_code)