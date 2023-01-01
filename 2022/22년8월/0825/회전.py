T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    a = M%N
    print(f'#{tc} {data[a]}')
