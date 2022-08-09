str = input()

result = ""

length = len(str)

if length % 2 == 0:
    result = str[int(length / 2) - 1] + str[int(length / 2)]
else:
    result = str[int(length / 2)]

print(result)
