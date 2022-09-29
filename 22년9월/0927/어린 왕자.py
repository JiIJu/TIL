T = int(input())

for tc in range(1,T+1):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        length1 = ((data[i][0]-x1)**2+(data[i][1]-y1)**2)**0.5
        length2 = ((data[i][0]-x2)**2+(data[i][1]-y2)**2)**0.5

        if length1<data[i][2] and length2<data[i][2]:
            pass
        elif length1<data[i][2]:
            cnt+=1
        elif length2<data[i][2]:
            cnt+=1
    print(cnt)