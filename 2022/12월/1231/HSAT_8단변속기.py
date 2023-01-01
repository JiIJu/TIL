# HSAT_8단변속기

data = list(map(int,input().split()))

num = [0]*7
for i in range(7):
    if data[i+1]-data[i]>0:
        num[i]=1
    else:
        num[i]=-1
cnt1,cnt2 = 0,0

cnt1 = num.count(1)
cnt2 = 7-cnt1
if cnt1 and cnt2:
    print('mixed')
elif cnt1>0 and cnt2==0:
    print('ascending')
else:
    print('descending')