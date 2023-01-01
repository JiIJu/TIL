T = int(input())

for tc in range(1,T+1):
    data = [list(map(int,input().split())) for _ in range(9)]
    data_test = []
    result = 1

    temp_row = [[0]*9 for _ in range(9)]
    temp_col = [[0]*9 for _ in range(9)]
    temp = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            temp_row[i][data[i][j]-1] = 1
    for i in range(9):
        for j in range(9):
            if temp_row[i][j] == 0:
                result = 0


    for i in range(9):
        for j in range(9):
            temp_col[data[j][i]-1][i] = 1

    for i in range(9):
        for j in range(9):
            if temp_row[j][i] == 0:
                result = 0


    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                for h in range(3):
                    temp[i+k][j+h] = data[i+k][j+h]

    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                for h in range(3):
                    if temp[i+k][j+h] == 0:
                        result = 0


    print(f'#{tc} {result}')