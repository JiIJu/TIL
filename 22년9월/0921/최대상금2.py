def find(n,N):
    global max
    if n == N:
        tmp = int(''.join(data))
        if max<tmp:
            max = tmp
    else:
        for i in range(len(data)-1):
            for j in range(i+1,len(data)):
                data[i] , data[j] = data[j] , data[i]
                tmp = int(''.join(data))
                ans.add(tmp)
                print(ans)
                # find(n+1,N)
                data[j] , data[i] = data[i] , data[j]

T = int(input())
for tc in range(1,T+1):
    data , N = input().split()
    data = list(data)
    N = int(N)
    max = 0
    ans = set()
    find(0,N)
    # print(ans)
    print(f'#{tc} {max}')