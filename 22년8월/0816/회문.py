T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(input()) for _ in range(N)]
    test = ''
    ans = ''
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                # if M%2 == 0:
                if data[i][j+k] == data[i][j+M-k-1]:
                    test += data[i][j+k]
                    print(test)
                # else:

            if len(test) == M:
                ans = test
            else:
                test = ''
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                # if M%2 == 0:
                if data[j+k][i] == data[j+M-k-1][i]:
                    test += data[j+k][i]
                # else:

            if len(test) == M:
                ans = test
            else:
                test = ''
    # print(f'#{tc} {ans})