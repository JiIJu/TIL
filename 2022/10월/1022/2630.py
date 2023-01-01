import sys

def paper(x,y,z):
    a = data[x][y]
    for i in range(x,x+z):
        for j in range(y,y+z):
            if data[i][j]!=a:
                for k in range(2):
                    for l in range(2):
                        paper(x+k*z//2,y+l*z//2,z//2)
                return
    if a==0:
        ans[0]+=1
    else:
        ans[1]+=1

N = int(input())

data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans =[0,0]
paper(0,0,N)
print(ans[0])
print(ans[1])