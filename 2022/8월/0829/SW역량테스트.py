T = int(input())

for tc in range(1,T+1):
    N , Kmin , Kmax = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()
    A = [0] * 101
    B = []
    for i in range(N):
        A[data[i]] =1
    for i in range(101):
        if A[i] == 1:
            B.append(i)

    a=100

    for i in range(B[0],B[-1]):
        for j in range(B[-1],B[0]-1,-1):
            T1 = i
            T2 = j
            cnt = [0] * 3
            for k in range(N):
                if data[k]>=T2:
                    cnt[2] +=1
                elif T1<=data[k]<T2:
                    cnt[1] +=1
                elif data[k]<T1:
                    cnt[0]+=1
            b = max(cnt)
            c = min(cnt)
            if b<=Kmax and c>=Kmin and a > b-c:
                a = b-c
                if a==0:
                    break
                    break

    if a==100:
        a= -1
    print(f'#{tc} {a}')
