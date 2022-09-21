T = int(input())
def password(a,word):
    if a == '0001101':
        word = '0'
    elif a == '0011001':
        word = '1'
    elif a=='0010011':
        word = '2'
    elif a == '0111101':
        word = '3'
    elif a == '0100011':
        word = '4'
    elif a == '0110001':
        word = '5'
    elif a == '0101111':
        word = '6'
    elif a == '0111011':
        word = '7'
    elif a == '0110111':
        word = '8'
    elif a == '0001011':
        word = '9'
    else:
        word = ''
    return word
for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(map(int,input())) for _ in range(N)]
    word = ''
    a = ''
    ans = ''
    stop = 0
    cnt =0
    x= []
    for i in range(N):
        for j in range(0,M-7):
            a = ''
            for k in range(7):
                a += f'{data[i][j+k]}'
            word = password(a,word)
            if word != '':
                ans += word
                word = ''
                x = [i,j]
                stop = 1
                break
        if stop ==1:
            break

    word = ''
    ans = ''
    result = ''
    stop = 0
    while True:
        for i in range(x[1],x[1]+56):
            word += f'{data[x[0]][i]}'
            if len(word)==7:
                s = password(word,result)
                if s != '':
                    result += s
                    word = ''
                else:
                    x[1] +=1
                    word = ''
                    result = ''
                    break

                if len(result) ==8:
                    stop = 1
                if stop ==1:
                    break
        if stop ==1:
            break

    odd = []
    even = []
    for i in range(8):
        if i%2 == 0:
            even.append(int(result[i]))
        else:
            odd.append(int(result[i]))

    answer = 0
    answer = sum(odd) + 3*sum(even)
    SUM = 0
    for i in range(8):
        SUM += int(result[i])
    if answer%10 == 0:
        print(f'#{tc} {SUM}')
    else:
        print(f'#{tc} 0')