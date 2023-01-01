T = int(input())

for tc in range(1,T+1):
    data = [input() for _ in range(5)]

    result = ''
    max = 0
    for i in range(5):
        if max<len(data[i]):
            max = len(data[i])
    emp = [[-1] * max for _ in range(5)]
    for i in range(5):
        for j in range(max):
            if len(data[i])<max and j == len(data[i]):
                break
            emp[i][j] = data[i][j]
    for j in range(max):
        for i in range(5):
            if emp[i][j] != -1:
                result += emp[i][j]
    print(f'#{tc} {result}')