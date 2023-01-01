# 4948 베르트랑 공준

data = [0]*250000

for i in range(2,250000):
    for j in range(2,int(250000**0.5)):
        if i*j<250000:
            data[i*j] = -1
        else:
            break
data[2] = 0


while True:
    ans = int(input())
    if ans==0:
        break
    cnt=0
    for i in range(ans+1,2*ans+1):
        if data[i]==0:
            cnt+=1
    print(cnt)
# print(data)