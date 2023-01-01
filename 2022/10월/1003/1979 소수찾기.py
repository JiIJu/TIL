
num = [0]*1001
num[0] = 1
num[1] = 1
n=2
while n<=500:
    for i in range(2,1000):
        if n*i<=1000:
            num[n*i] = 1
        else:
            break
    n+=1
N = int(input())
data = list(map(int,input().split()))
cnt=0
for i in data:
    if num[i]==0:
        cnt+=1
print(cnt)