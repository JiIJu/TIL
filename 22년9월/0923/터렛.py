T = int(input())

for tc in range(1,T+1):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if r1<r2:
        r1,r2=r2,r1
        x1 , x2 = x2,x1
        y1,y2=y2,y1
    ans = -1
    length = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if [x1,y1] == [x2,y2] and r1==0 and r2==0:
        ans = 1
    elif [x1,y1,r1] == [x2,y2,r2]:
        ans = -1
    elif length>r1 and (r1+r2) == length:
        ans = 1
    elif length>r1 and (r1+r2) > length:
        ans = 2
    elif length>r1 and r1+r2<length:
        ans=0
    elif length<r1 and  length+r2==r1:
        ans = 1
    elif length<r1 and length+r2>r1:
        ans = 2
    elif length<r1 and length+r2<r1:
        ans= 0
    print(ans)