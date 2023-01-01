T = int(input())

for tc in range(1,T+1):
    x1 , y1 ,x2,y2= map(int,input().split())
    n = int(input())
    data =[]
    for i in range(n):
        data.append(list(map(int,input().split())))
    print(data)