fruits = "apple,rottenBanana,apple,RoTTenorange,Orange"

fruit_list = fruits.split(",")

fresh_list = []

for fruit in fruit_list:
    if "rotten" in fruit.lower():
        fresh_list.append(fruit.lower().replace("rotten", ""))
    else:
        fresh_list.append(fruit.lower())

print(fresh_list)
