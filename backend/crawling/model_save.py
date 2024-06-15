from movie.models import Movie, Genre, Provider, Actor, Director, Producer, Video
from pprint import pprint
from . import crawling

def movie_and_genre(data):
    # database는 api 요청 결과임
    # pprint(data)
    genres = data['genre_ids']
    print(genres)
    # 받을 데이터를 movie 모델에 저장해야함
    movie = Movie.objects.create(
            title = data['title'],
            overview = data['overview'],
            movie_id = data['id'],
            adult = data['adult'],
            popularity = data['popularity'],
            poster_path = data.get('poster_path'))
    for genre in genres:
        genre = Genre.objects.get(genre_id=genre)
        movie.genres.add(genre)

def provider(movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    provider_data = crawling.watch_providers(movie.movie_id)
    if provider_data:
        buy_providers = provider_data.get('buy')
        rent_providers = provider_data.get('rent')
        # print(buy_providers)
        if buy_providers:
            for provider in buy_providers:
                # print(provider.get('provider_name'))
                provider_id = provider.get('provider_id')
                provider = Provider.objects.get(provider_id=provider_id)
                movie.Provider.add(provider)
        if rent_providers:
            for provider in rent_providers:
                # print(provider.get('provider_name'))
                provider_id = provider.get('provider_id')
                provider = Provider.objects.get(provider_id=provider_id)
                movie.Provider.add(provider)

def video(movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # print(movie)
    video_data = crawling.videos(movie.movie_id)
    if video_data:
        for data in video_data:
            video_id = data.get('id')
            video_key = data.get('key')
            video_name = data.get('name')
            video_site = data.get('site')
            official = data.get('official')
            video_type = data.get('type')
            video = Video.objects.create(
                video_id = video_id,
                video_key = video_key,  
                video_name = video_name,
                video_site = video_site,
                official = official,
                video_type = video_type,
            )
            movie.video.add(video)

def actor_director(movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    credits = crawling.credits(movie.movie_id)
    if credits:
        # pprint(movie)
        casts = credits.get('cast')
        crews = credits.get('crew')
        if casts:
            for cast in casts:
                if cast.get('popularity') >= 10:
                    # pprint(cast.get('name'))
                    actor_id = cast.get('id')
                    # actor나 director가 모델에 없으면
                    # 쿼리를 작성하여 해당 actor_id를 가진 배우를 가져옴
                    query = f"SELECT * FROM movie_actor WHERE actor_id = {actor_id}"
                    actors = Actor.objects.raw(query)

                    # 만약 actors 리스트가 비어있다면 새로운 배우를 생성
                    if not actors:
                        # print('없음')
                        actor = Actor.objects.create(
                        actor_id = actor_id,
                        actor_name = cast.get('name'),
                        actor_original_name = cast.get('original_name'),
                        actor_popularity = cast.get('popularity'),
                        profile_logo_path = cast.get('profile_path'),
                        )
                        movie.actors.add(actor)
                    # actors가 있다면
                    for actor in actors:
                        # print(actor.id, actor.actor_id, actor.actor_name)  # 예시로 출력하는 필드들입니다.
                        movie.actors.add(actor)
        print('-------------------------')
        if crews:
            for crew in crews:
                if crew.get('job') == 'Producer':
                    # pprint(crew.get('name'))
                    producer_id = crew.get('id')
                    query = f"SELECT * FROM movie_producer WHERE producer_id = {producer_id}"
                    producers = Producer.objects.raw(query)

                    if not producers:
                        # print('없음')
                        producer = Producer.objects.create(
                        producer_id = producer_id,
                        producer_name = crew.get('name'),
                        producer_original_name = crew.get('original_name'),
                        producer_popularity = crew.get('popularity'),
                        )
                        movie.producer.add(producer)
                    for producer in producers:
                        # print(producer.id, producer.producer_id, producer.producer_name)  # 예시로 출력하는 필드들입니다.
                        movie.producer.add(producer)
  
                if crew.get('job') == 'Director':
                    # pprint(crew.get('name'))
                    director_id = crew.get('id')
                    query = f"SELECT * FROM movie_director WHERE director_id = {director_id}"
                    directors = Director.objects.raw(query)

                    if not directors:
                        # print('없음')
                        director = Director.objects.create(
                        director_id = director_id,
                        director_name = crew.get('name'),
                        director_original_name = crew.get('original_name'),
                        director_popularity = crew.get('popularity'),
                        )
                        movie.director.add(director)

                    for director in directors:
                        # print(director.id, director.director_id, director.director_name)  # 예시로 출력하는 필드들입니다.
                        movie.director.add(director)