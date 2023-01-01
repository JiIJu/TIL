# 쿼드트리

def comp(x,y,n):
    check = data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=data[i][j]:
                print('(',end='')
                comp(x,y,n//2)
                comp(x,y+n//2,n//2)
                comp(x+n//2,y,n//2)
                comp(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    if check=='1':
        print(1,end='')
        return
    else:
        print(0,end='')
        return
N = int(input())
data = [list(input()) for _ in range(N)]
comp(0,0,N)