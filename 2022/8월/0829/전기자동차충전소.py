T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    di1 = [-1,1,0,0]
    dj1 = [0,0,-1,1]
    di2 =[-1,1,1,-1]
    ij2 = [1,1,-1,-1]

    