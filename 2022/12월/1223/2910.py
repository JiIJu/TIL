#2910 빈도정렬

N ,C = map(int,input().split())

data = list(map(int,input().split()))
ans = {}
for i in data:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
ans = sorted(ans.items(),key=lambda x:-x[1])
for i in ans:
    a,b = i
    for j in range(b):
        print(a,end=' ')