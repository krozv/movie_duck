import json
import requests

# 한국영화진흥원 API KEY
API_KEY = 'c309e1e47c7986fa2e7c766e365c506a'

### popular movie  
def search(filename):
  url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json'
  params = {
    'key': API_KEY,
    'peopleCd': '20125838'
  }
  save_data(url, params, filename)

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
    
search('search_people_info.json')