import json


def dec_movies(movies):
    path = 'data/movies/'
    id_list = []
    dict_list = []
    for i in range(len(movies)):
        id_list.append(movies[i]['id'])
    for i in id_list:    
        movies_json = open(f'data/movies/{i}.json', encoding='UTF8')
        movies_list = json.load(movies_json)
        dict_list.append(movies_list)
    release_list = []
    for i in range(len(dict_list)):
        release_list.append(dict_list[i]['release_date'])

    month = []
    for i in range(len(release_list)):
        if release_list[i][5:7] == '12':
            month.append(dict_list[i]['title'])
    print(month)
    #         month.append(release_list[i])
    # print(month)
    # s = []
    # for j in range(len(month)):
    #     for i in range(len(dict_list)):
    #         if month[j] == dict_list[i]['release_date'][5:7]:
    #             s.append(dict_list[i]['title'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))