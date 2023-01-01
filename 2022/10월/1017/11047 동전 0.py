
N , K = map(int,input().split())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()
data = data[::-1]
money = 0
cnt=0
while money!=K:
     for i in range(len(data)):
         if K-money>=data[i]:
             cnt+=1
             money+=data[i]
             break
print(cnt)