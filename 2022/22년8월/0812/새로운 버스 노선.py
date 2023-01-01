T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [map(int,input().split()) for _ in range(N)]
    bus = []
    for i in range(N):
            if data[i][0] == 1:
                A = data[i][1]
                B = data[i][2]
                for j in range(B-A):
                    bus.append