def enq(n):
    global last
    last+=1
    heap[last] = n
    c = n
    p = c//2
    while p and heap[p]< heap[c]:
        heap[p],heap[c] = heap[c],heap[p]
        c = p
        p = c//2
T = int(input())

for tc in range(1,T+1):
    N , M , L = map(int,input().split())
    data = [0] * (N+1)
    for i in range(M):
        a , b  = map(int,input().split())
        data[a] = b
    heap = [0]*1000
    last = 0

    for i in range(N,0,-1):
        if i//2>0:
            data[i//2]+=data[i]
    print(data[L])