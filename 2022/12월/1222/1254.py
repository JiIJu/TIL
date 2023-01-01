# 1254 팰린드롬만 들기


data = input()

for i in range(len(data)):
    if data[i:] == data[i:][::-1]:
        print(len(data)+i)
        break