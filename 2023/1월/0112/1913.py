# 1913 달팽이

N = int(input())
n = int(input())
temp = N*N
data = [[0]*N for _ in range(N)]

di = [1,0,-1,0]
dj = [0,1,0,-1]
i,j=0,0
data[0][0]=temp
ans=[]
if temp == n:
    ans.append(i)
    ans.append(j)
temp-=1
check=0
while 0<=i+di[check%4]<N and 0<=j+dj[check%4]<N and data[i+di[check%4]][j+dj[check%4]]==0:
    data[i + di[check % 4]][j + dj[check % 4]]=temp
    if temp==n:
        ans.append(i + di[check % 4])
        ans.append(j+dj[check%4])
    temp -=1
    i = i+di[check%4]
    j = j+dj[check%4]
    if (i+di[check%4]<0 or i+di[check%4]>=N) or (j+dj[check%4]<0 or j+dj[check%4]>=N) or data[i+di[check%4]][j+dj[check%4]]!=0:
        check +=1
        # i+=di[check%4]
        # j+=dj[check%4]

for i in data:
    print(*i)
print(ans[0]+1,ans[1]+1)
