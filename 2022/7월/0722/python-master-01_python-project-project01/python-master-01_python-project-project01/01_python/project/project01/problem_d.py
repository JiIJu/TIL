import json


def max_revenue(movies):
    
    path = 'data/movies/'
    id_list = []
    dict_list = []
    for i in range(len(movies)):
        id_list.append(movies[i]['id'])
    # for data in id_list:
    #     for line in open(f'{path}{data}.json',encoding='UTF8'):
    #         dict_list.append(json.load(line))
    for i in id_list:    
        movies_json = open(f'data/movies/{i}.json', encoding='UTF8')
        movies_list = json.load(movies_json)
        dict_list.append(movies_list)
    revenue_list = []
    for i in range(len(dict_list)):
        revenue_list.append(dict_list[i]['revenue'])
    max_revenue = 0
    i = 0
    for i in range(len(revenue_list)):
        if revenue_list[i]>max_revenue:
            max_revenue = revenue_list[i]
    for i in range(len(dict_list)):
        if dict_list[i]['revenue']  == max_revenue:
           a = dict_list[i]['title']
           print(a)
        
#아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
