# API 명세서

## API 문서

### 유저 API
| URL | Method | Description |
| --- | --- | --- |
| accounts/signup/ | POST | 회원가입 기능 | 
| accounts/login/ | POST | 로그인 기능 | 
| accounts/logout/ | POST | 로그아웃 기능 | 
| accounts/signout/ | DELETE | 회원탈퇴 기능 |

### 영화 API
| URL | Method | Description |
| --- | --- | --- |
| api/movie/ | GET | 메인 페이지 |
| api/movie/boxoffice/ | GET | 현재 상영 중 영화 |
| api/movie/popular/ | GET | 인기 영화 |
| api/movie/search/{search_query}/ | GET | 영화 검색 | 
| api/movie/{movie_pk}/ | GET | 상세 페이지 |
| api/movie/{movie_pk}/comment/ | POST | 댓글 작성
| api/movie/{movie_pk}/comment/{comment_pk} | PUT | 댓글 수정 |
| api/movie/{movie_pk}/comment/{comment_pk} | DELETE | 댓글 삭제 |
| api/movie/{movie_pk}/comment/{comment_pk} | POST | 대댓글 작성 |
| api/movie/{movie_pk}/comment/{comment_pk}/{reply_pk} | PUT | 대댓글 수정 |
| api/movie/{movie_pk}/comment/{comment_pk}/{reply_pk} | DELETE | 대댓글 삭제 |

### 추천 API
| URL | Method | Description |
| --- | --- | --- |
| api/recommend/ | GET | 영화 추천 페이지 |
| api/recommend/ | PUT | 영화 목록 reset |
| api/recommend/genre/ | POST | 장르 별 추천 영화 목록 |
| api/recommend/actor/ | POST | 배우 별 추천 영화 목록 |
| api/recommend/likemovie/ | GET | 사용자가 좋아요한 영화 목록 |

### WhatIsThisMovie API
| URL | Method | Description |
| --- | --- | --- |
| api/WITM/ | GET | 메인 페이지 | 

## DB 모델
