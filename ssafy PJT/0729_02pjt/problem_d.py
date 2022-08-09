import requests
from pprint import pprint


def recommendation(title):
    
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

        url = f'https://api.themoviedb.org/3/movie/{params1["movie_id"]}/recommendations?api_key=1cc991c3c4ede5f1631fb06af01f8fd8&language=KO&page=1'
        response1 = requests.get(url).json()
        rec = []
        
        if len(response1['results']) >0:
            for i in range(len(response1['results'])):
                rec.append(response1['results'][i]['title'])
            return rec
        elif len(response1['results']) ==0:
            return empty

        
    #     for j in range(len(response['results'])):
    #         if response['results'][j]['title'] == title:
    #             search.append(response['results'][j])
    #             break
    #     if len(search) !=0:
    #         break
    # if search
    #     return search


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
