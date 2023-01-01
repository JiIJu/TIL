#IOIOI

N = int(input())
M = int(input())
S = input()
data = 'I'
data += 'OI'*N
cnt=0
ans = 0
i=0
while i<M-1:
    if S[i:i+3] == 'IOI':
        cnt+=1
        i+=2
        if cnt==N:
            cnt-=1
            ans+=1
    else:
        cnt=0
        i+=1
print(ans)