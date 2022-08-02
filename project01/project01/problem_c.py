import json
from pprint import pprint


def movie_info(movie, genres):
    
    # data = {
    #     'id': movie.get('id'),
    #     'title': movie.get('title'),
    #     'poster_path': movie.get('poster_path'),
    #     'vote_average': movie.get('vote_average'),
    #     'overview': movie.get('overview'),
    #     'genre_ids': movie.get('genre_ids')
    # }
    
    # for i in range(2):
    #     for j in range(len(genres)):
    #         if data['genre_ids'][i] == genres[j]['id']: #data의 장르id에 맞는 장르를 찾아 넣기
    #             data['genre_ids'][i] = genres[j]['name']
    # data['genre_names'] = data.pop('genre_ids') # key값 이름변경
    # return data
    data = []
    for i in range(len(movie)): #data에 movie 정보 넣기
        data.append(movie[i])
    for k in range(len(data)):    
        for i in range(len(data[k]['genre_ids'])):
            for j in range(len(genres)):
                if data[k]['genre_ids'][i] == genres[j]['id']: #data의 장르id에 맞는 장르를 찾아 넣기
                    data[k]['genre_ids'][i] = genres[j]['name']
    for i in range(len(data)):        
        data[i]['genre_names'] = data[i].pop('genre_ids') # key값 이름변경
    return data
movies_json = open('data/movies.json', encoding='UTF8')
movies_list = json.load(movies_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

pprint(movie_info(movies_list, genres_list))
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))