T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [[0]*10 for _ in range(10)]

    for n in range(N):
        r1,c1,r2,c2,color = map(int,input().split())

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if data[i][j] == 1 and color == 2:
                    data[i][j] = 3
                elif data[i][j] == 2 and color == 1:
                    data[i][j] = 3
                elif data[i][j] != color and data[i][j] != 3:
                    data[i][j] = color
    count = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                count+=1
    print(f'#{tc} {count}')