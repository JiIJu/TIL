for tc in range(1,11):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    max = 0

    for i in range(100):
        count = 0
        for j in range(100):
            count += data[i][j]
        if count>max:
            max = count
    for i in range(100):
        count = 0
        for j in range(100):
            count += data[j][i]
        if count>max:
            max = count
    count = 0
    for i in range(100):
        count += data[i][i]
        if count > max:
            max = count
    count = 0
    for i in range(100):
        count += data[99-i][99-i]
        if count > max:
            max = count



    print(f'#{tc} {max}')