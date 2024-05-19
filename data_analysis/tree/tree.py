# 영화 정보에 대한 질문 트리
movie_tree = {
    'question': '영화 장르 선택 (액션/로맨스)',
    '액션': {
        'question': '배우/감독 중 아는 정보 선택',
        '배우': {
            'question': '주요 배우를 알려주세요.',
            'TOM CRUISE': '미션 임파서블',
            'KEANU REEVES': '매트릭스'
        },
        '감독': {
            'question': '주요 감독을 알려주세요.',
            'CHRISTOPHER NOLAN': '인셉션',
            'JAMES CAMERON': '터미네이터 2: 심판의 날'
        }
    },
    '로맨스': {
        'question': '배우/감독 중 아는 정보 선택',
        '배우': {
            'question': '주요 배우를 알려주세요.',
            'RYAN GOSLING': '라라랜드',
            'JULIA ROBERTS': '노팅 힐'
        },
        '감독': {
            'question': '주요 감독을 알려주세요.',
            'RICHARD LINKLATER': '비포 선라이즈',
            'GARRY MARSHALL': '프리티 우먼'
        }
    }
}

# 대문자로 변환하여 사용자 응답을 처리하는 함수
def process_response(response):
    return response.upper()

# 유효한 응답인지 확인하는 함수
def is_valid_response(response, current_node):
    return response in current_node

# 트리를 순회하면서 사용자에게 질문하고, 영화 제목을 찾는 함수
def find_movie(movie_tree):
    current_node = movie_tree
    while True:
        if 'question' in current_node:
            print(current_node['question'])
            response = input().strip()
            response = process_response(response)
            if is_valid_response(response, current_node):
                current_node = current_node[response]
            else:
                print("유효한 응답이 아닙니다. 다시 입력하세요.")
        else:
            return current_node

# 영화 제목 찾기
movie_title = find_movie(movie_tree)
print(f'혹시 찾으시는 영화가 {movie_title}인가요?')
