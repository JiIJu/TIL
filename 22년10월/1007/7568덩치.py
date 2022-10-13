N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append((a,b))
ans = []
for i in range(N): # 부르트포스
    cnt = 1
    for j in range(N):
        if data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            cnt+=1
    print(cnt , end=' ')