def check(i,j):

    chess[i][j]=1
    a,b = i,j
    for k in range(8):
        i,j = a,b
        while 0<=i + di[k]<8 and 0<=j + dj[k]<8:
            i += di[k]
            j += dj[k]
            chess[i][j] = 1



def queen(i,cnt,N):
    global cnt
    if min<cnt:
        return
    if i==N and j ==N:
        if min>cnt:
            min = cnt
    for i in range()






T = int(input())

for tc in range(1,T+1):
    di = [-1,1,0,0,-1,1,1,-1]
    dj = [0,0,-1,1,1,1,-1,-1]

    N = int(input())
    chess = [[0]*8 for _ in range(8)]
    # queen()
    min = 99999
    check(3,3)
    print(chess)