# API 명세서

## API 문서

### 유저 API
| URL | Method | Description |
| --- | --- | --- |
| api/accounts/signup/ | POST | 회원가입 기능 | 
| api/accounts/login/ | POST | 로그인 기능 | 
| api/accounts/logout/ | POST | 로그아웃 기능 | 

### 영화 API
| URL | Method | Description |
| --- | --- | --- |
| api/movie/ | GET | 메인 페이지 | 
| api/movie/search/{search_query}/ | GET | 영화 검색 페이지 | 

### 게시글 API
| URL | Method | Description |
| --- | --- | --- |
| api/entry/ | GET | 메인 페이지 | 
| api/entry/ | POST | 게시글 작성 | 
| api/entry/{article_pk}/ | GET | 게시글 상세 정보 | 
| api/entry/{article_pk}/ | PUT | 게시글 수정 | 
| api/entry/{article_pk}/ | DELETE | 게시글 삭제 | 
| api/entry/{article_pk}/comment/ | POST | 댓글 작성 | 
| api/entry/{article_pk}/comment/{comment_pk} | PUT | 댓글 수정 | 
| api/entry/{article_pk}/comment/{comment_pk} | DELETE | 댓글 삭제 | 

### WhatIsThisMovie API
| URL | Method | Description |
| --- | --- | --- |
| api/WITM/ | GET | 메인 페이지 | 

## DB 모델