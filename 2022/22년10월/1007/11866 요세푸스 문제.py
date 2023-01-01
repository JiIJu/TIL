N , K =map(int,input().split())

data =[]
for i in range(1,N+1):
    data.append(i)
ans = []

cnt = 0
a = 0
while True:
    for i in range(len(data)):
        if data[i]!=-1:
            cnt+=1
        if cnt == K:
            ans.append(i+1)
            data[i]=-1
            cnt = 0

    if sum(data)==(-N):
        break


print('<' , end='')
for i in range(len(ans)-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')