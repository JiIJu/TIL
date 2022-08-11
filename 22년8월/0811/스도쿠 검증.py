T = int(input())

for tc in range(1,T+1):
    data = [list(map(int,input().split())) for _ in range(9)]
    data_test = []
    empty = []
    result= -1
#if not in

    for i in range(9):
        data_test = []
        count = 0
        for j in range(9):
            if data[i][j] not in data_test:
                data_test += [data[i][j]]
                count +=1
        if count != 9:
            result = 0
            break
        elif count == 9:
            result = 1
    for i in range(9):
        data_test = []
        count = 0
        for j in range(9):
            if data[j][i] not in data_test:
                data_test += [data[j][i]]
                count += 1
        if count != 9 or result == 0:
            result = 0
            break
        elif count == 9:
            result = 1

    for i in range(0,7,3):
        for j in range(0,7,3):
            a = []
            count=0
            for k in range(3):
                for h in range(3):
                    if data[i+k][j+h] not in a:
                        a += [data[i][j]]
                        count+=1
            if count != 9 or result == 0:
                result = 0
                break
            elif count == 9:
                result = 1


    print(f'#{tc} {result}')