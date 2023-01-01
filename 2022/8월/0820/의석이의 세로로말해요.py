T = int(input())

for tc in range(1,T+1):
    data = [list(input()) for _ in range(5)]
    word = ''
    for i in range(15):
        for j in range(5):
            if len(data[j])>i:
                word += data[j][i]
    print(f'#{tc} {word}')

