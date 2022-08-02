import requests


def popular_count():
    
    # 여기에 코드를 작성합니다.  
    params = {"api_key": "1cc991c3c4ede5f1631fb06af01f8fd8",
          "language": "ko",
          "region" : "KR",
          "page" : 1}
    
    # url = 'https://api.themoviedb.org/3/movie/popular?api_key=1cc991c3c4ede5f1631fb06af01f8fd8&language=%22ko%22&page=1&region=%22KR%22'
    url = 'https://api.themoviedb.org/3/movie/popular'
    response = requests.get(url, params=params).json()
    print(len(response['results']))
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    popular_count()