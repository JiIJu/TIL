# 12865 평범한배낭

N,K = map(int,input().split())
data = [[0,0]]
back = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    W , V = map(int,input().split())
    data.append([W,V])


for i in range(1,N+1):
    for j in range(1,K+1):
        weight,value = data[i][0],data[i][1]

        if j<weight:
            back[i][j] = back[i-1][j]
        else:
            back[i][j] = max(back[i-1][j-weight]+value,back[i-1][j])
print(back[N][K])
