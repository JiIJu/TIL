import sys

def test(x,y,z):
    global answer
    a = data[x][y]

    for i in range(x,x+z):
        for j in range(y,y+z):
            if data[i][j] != a:
                for k in range(3):
                    for l in range(3):
                        test(x+k*z//3,y+l*z//3,z//3)
                return
    if a==-1:
        answer[0]+=1
    elif a==0:
        answer[1]+=1
    elif a==1:
        answer[2]+=1



N = int(input())

data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = [0]*3

test(0,0,N)
for i in range(3):
    print(answer[i])
