T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input().split()))
    a = 0
    num = [0] * 10001
    for i in range(10):
        num[data[i]] +=1
    for i in range(10000,-1,-1):
        if num[i]>0:
            a = i
            break
    print(f'#{tc} {a}')