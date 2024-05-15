### tmdb configuration 확인용 ###
import json
import requests

# TMDB api key
API_KEY = '769830601abcc5047d5d1a90b40dc11c'
# def save_data(url, params, file_name, headers):
#   response = requests.get(url, params=params, headers=headers)

#   if response.status_code == 200:
#     data = response.json()
    
#     # 데이터 json 파일로 저장
#     with open(file_name, 'w', encoding='utf-8') as json_file:
#       json.dump(data, json_file, ensure_ascii=False, indent=4)
#     print('저장 완료')
#   else:
#     print('오류 발생', response.status_code)

# json 파일로 저장하는 함수
def add_data(url, params, file_name, headers):
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        # print(response.json())
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


def discover_movie(page):
    url = 'https://api.themoviedb.org/3/discover/movie'
    headers = {"accept": "application/json"}
    params = {
        'api_key': API_KEY,
        'page': page,
        'with_original_language': 'en'
    }
    file_name = 'discover_en_movie.json'
    add_data(url, params, file_name, headers)

for page in range(1, 501):
    discover_movie(page)
    print(page)