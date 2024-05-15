import json
import requests

# TMDB api key
API_KEY = '769830601abcc5047d5d1a90b40dc11c'

### popular movie  
def popular(page):
  url = 'https://api.themoviedb.org/3/movie/popular'
  params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
  }
  save_data(url, params, 'movies.json')

# json 파일로 저장하는 함수
def save_data(url, params, file_name):
  response = requests.get(url, params=params)

  if response.status_code == 200:
    data = response.json()
    
    # 데이터 json 파일로 저장
    with open(file_name, 'w', encoding='utf-8') as json_file:
      json.dump(data, json_file, ensure_ascii=False, indent=4)
    print('저장 완료')
  else:
    print('오류 발생', response.status_code)

### movie_id에 따른 details
def details(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'detail.json'
  save_data(url, params, file_name)

### movid_id에 따른 Credits
def credits(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'credits.json'
  save_data(url, params, file_name)

### movie_id에 따른 해당 영화 keywords 확인 가능
def keywords(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'keywords.json'
  save_data(url, params, file_name)

### movie_id에 따른 Lists
def lists(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/lists'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'lists.json'
  save_data(url, params, file_name)

### movie_id에 따른 Recommendations
# 해당 영화에 대한 다른 추천 영화 리스트
def recommendations(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'recommendations.json'
  save_data(url, params, file_name)

# 사용자 리뷰
def reviews(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'reviews.json'
  save_data(url, params, file_name)

def similar(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'similar.json'
  save_data(url, params, file_name)

# 해당 영화를 볼 수 있는 provider 정보 제공
# appleTV, amazon 등
def watch_providers(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'watch_providers.json'
  save_data(url, params, file_name)

# person id에 따른 인물 정보
def person_details(person_id):
  url = f'https://api.themoviedb.org/3/person/{person_id}'
  params = {
    'language': 'ko',
    'api_key': API_KEY,
  }
  file_name = 'person_details.json'
  save_data(url, params, file_name)

movie_id = 693134
# watch_providers(movie_id)

person_id = 1586047
person_details(person_id)

# popular(1)
