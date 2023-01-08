import json


def sorted_best_companies(movies):

    companies_freq = {}

    for movie in movies:
        movie_id = movie.get("id")
        movie_detail_json = open(f"data/movies/{movie_id}.json", encoding="utf-8")
        movie_detail = json.load(movie_detail_json)
        companies = movie_detail.get("production_companies")
        for company in companies:
            if companies_freq.get(company["name"]):
                companies_freq[company["name"]] += 1
            else:
                companies_freq[company["name"]] = 1

    return sorted(companies_freq.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    movies_json = open("data/movies.json", encoding="utf-8")
    movies_list = json.load(movies_json)

    print(sorted_best_companies(movies_list))
