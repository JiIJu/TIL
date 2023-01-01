
N = int(input())
datan = list(map(int,input().split()))

M = int(input())
datam = list(map(int,input().split()))

datan = sorted(datan)
for i in range(M): # 이분탐색구현
    s,e = 0,N-1
    while True:
        mid = (s+e)//2
        if datam[i]==datan[mid]:
            print(1)
            break
        if datam[i]>datan[mid]:
            s = mid+1
        elif datam[i]<datan[mid]:
            e = mid-1

        if s>e:
            print(0)
            break