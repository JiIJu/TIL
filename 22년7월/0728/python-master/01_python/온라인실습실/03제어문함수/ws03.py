infos = [{"name": "kim", "age": 12}, {"name": "lee", "age": 4}]

age_sum = 0

for dic in infos:
    for key, value in dic.items():
        if key == "age":
            age_sum += value

print(age_sum)
