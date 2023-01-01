def queen(i,j):
    di = [-1,1,0,1,-1,1,1,-1]
    dj = [0,0,-1,1,1,1,-1,-1]
    for k in range(8):
        while 0<=i+di

def chess(N,data,cnt):

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data =[[0]*8 for _ in range(8)]
