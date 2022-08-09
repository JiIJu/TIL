import requests
from pprint import pprint


def credits(title):
     
    # 여기에 코드를 작성합니다.  
    params = {"api_key": "1cc991c3c4ede5f1631fb06af01f8fd8",
          "query" : f'{title}',
          "page" : 1,
          "language": "ko",
          "region" : "KR"
          }
    
    url = 'https://api.themoviedb.org/3/search/movie'
    response = requests.get(url, params=params).json()
    search = []
    empty = []
    if len(response['results']) >0:
            search.append(response['results'][0]['id'])
    else:
        return None
            
            
    params1 = {"api_key": "1cc991c3c4ede5f1631fb06af01f8fd8",
        "movie_id" : f'{search[0]}',
          "page" : 1,
          "language": "ko",
          }

    url = f'https://api.themoviedb.org/3/movie/{params1["movie_id"]}/credits?api_key=1cc991c3c4ede5f1631fb06af01f8fd8&language=KO'
    response1 = requests.get(url).json()
    cast = []
    directing = []
    for i in range(len(response1['cast'])):
        if response1['cast'][i]['cast_id'] <10:
            cast.append(response1['cast'][i]['original_name'])
    
    for i in range(len(response1['crew'])):
        if response1['crew'][i]['department']  == 'Directing':
            directing.append(response1['crew'][i]['original_name'])
    dict = {'cast' : cast , 'directing' : directing}
    return dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
