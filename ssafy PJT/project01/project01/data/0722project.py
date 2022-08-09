import json

movie = open('movie.json', encoding='utf-8')
movie_detail = json.load(movie)

print(movie_detail)

genre_ids = {
        'id': movie_detail.get('id'),
        'title': movie_detail.get('title'),
        'poster_path': movie_detail.get('poster_path'),
        'vote_average': movie_detail.get('vote_average'),
        'overview': movie_detail.get('overview')
    }

print(data)
def movie_info(genre_ids):
    