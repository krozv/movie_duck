import json
import requests

# TMDB api key
API_KEY = 'api_key 넣으면 됨'

# json 파일로 저장하는 함수
def add_data(url, params, file_name):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['results'][0]
    
        # 데이터 json 파일로 저장
        with open(file_name, 'a', encoding='utf-8') as json_file:
            json_file.seek(0, 2)
            if json_file.tell() > 0:
                json_file.write(',')
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.write('\n')
            print('저장 완료')
    else:
        print('오류 발생', response.status_code)

# popular movie
def popular(page):
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
    }
    file_name = 'top_rated_movie.json'
    add_data(url, params, file_name)

for page in range(1, 400):
    popular(page)
    print(page)