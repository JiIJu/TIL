#2304 창고 다각형

N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append((a,b))
data = sorted(data)

max_height,max_index = 0,0
for i in range(N):
    a,b = data[i]
    if b>max_height:
        max_height = b
        max_index=i

ans = max_height
position,height = data[0][0],data[0][1]
for i in range(1,max_index+1):
    if height<=data[i][1]:
        ans+=(data[i][0]-position)*height
        position,height = data[i][0],data[i][1]
position,height = data[-1][0],data[-1][1]
for i in range(N-1,max_index-1,-1):
    if height<=data[i][1]:
        ans+=(position-data[i][0])*height
        position,height = data[i][0],data[i][1]
print(ans)