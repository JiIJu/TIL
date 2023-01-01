for tc in range(1,11):
    N = int(input())

    data = [list(input()) for _ in range(100)]

    max =0

    for i in range(100):
        for j in range(100):
            count = 0
            for k in range(99,-1,-1):
                if data[i][j] == data[i][k]:
                    word = ''
                    for l in range(j,k+1):
                        word += data[i][l]
                    rev = ''
                    for l in range(len(word)-1,-1,-1):
                        rev += word[l]
                    if word == rev:
                        count = len(word)
                        if count>max:
                            max = count

    for i in range(100):
        for j in range(100):
            count = 0
            for k in range(99,-1,-1):
                if data[j][i] == data[k][i]:
                    word = ''
                    for l in range(j,k+1):
                        word += data[l][i]
                    rev = ''
                    for l in range(len(word)-1,-1,-1):
                        rev += word[l]
                    if word == rev:
                        count = len(word)
                        if count>max:
                            max = count

    print(f'#{tc} {max}')