import json
from pprint import pprint


def movie_info(movie, genres):
    
    data = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids')
    }
    
    for i in range(len(data['genre_ids'])):
        for j in range(len(genres)):
            if data['genre_ids'][i] == genres[j]['id']: #data의 장르id에 맞는 장르를 찾아 넣기
                data['genre_ids'][i] = genres[j]['name']
    # data['genre_names'] = data.pop('genre_ids') # key값 이름변경
    print(data.pop('genre_ids'))

movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))