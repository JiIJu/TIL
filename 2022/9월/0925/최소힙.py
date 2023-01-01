def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] > heap[c]:
        heap[p],heap[c] = heap[c], heap[p]

        c = p
        p = c//2

def enq(n):
    global last
    last+=1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p]>heap[c]:
        c = p
        p = c//2

T = int(input())
for tc in range(1,T+1):
    heap = [0] * 500
    last = 0
    N = int(input())
    data = list(map(int,input().split()))
    for i in range(N):
        enq(data[i])
    print(heap)
    # sum = 0
    # while N!=0:
    #     N = N//2
    #     sum += heap[N]
    # print(f'#{tc} {sum}')
