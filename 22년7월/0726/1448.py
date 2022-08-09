grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
list1 = []

for i in range(len(grain_lst)):
    list1.append(grain_lst[i][1])
max = 0
a = 0
for i in range(len(list1)):
    if list1[i]>max:
        max = list1[i]
        a= i
print(grain_lst[a][0])