### tmdb configuration 확인용 ###
import json
import requests

# TMDB api key
API_KEY = '769830601abcc5047d5d1a90b40dc11c'
def save_data(url, params, file_name, headers):
  response = requests.get(url, params=params, headers=headers)

  if response.status_code == 200:
    data = response.json()
    
    # 데이터 json 파일로 저장
    with open(file_name, 'w', encoding='utf-8') as json_file:
      json.dump(data, json_file, ensure_ascii=False, indent=4)
    print('저장 완료')
  else:
    print('오류 발생', response.status_code)

def config_details():
  url = f'https://api.themoviedb.org/3/configuration'
  headers = {"accept": "application/json"}
  params = {
    'api_key': API_KEY,
  }
  file_name = 'config_details.json'
  save_data(url, params, file_name, headers)

def config_countries():
  url = 'https://api.themoviedb.org/3/configuration/countries'
  headers = {"accept": "application/json"}
  params = {
    'api_key': API_KEY,
  }
  file_name = 'config_countrie.json'
  save_data(url, params, file_name, headers)

def config_languages():
  url = 'https://api.themoviedb.org/3/configuration/languages'
  headers = {"accept": "application/json"}
  params = {
    'api_key': API_KEY,
  }
  file_name = 'config_languages.json'
  save_data(url, params, file_name, headers)

def discover_movie(page):
  url = 'https://api.themoviedb.org/3/discover/movie'
  headers = {"accept": "application/json"}
  params = {
    'api_key': API_KEY,
    'page': page,
    'with_original_language': 'ko'
  }
  file_name = 'discover_movie.json'
  save_data(url, params, file_name, headers)


# config_details()
# config_countries()
# config_languages()
discover_movie()