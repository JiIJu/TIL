서랍의 비밀번호
P , K = map(int,input().split())
if P>=K:
    print(P-K+1)
else:
    print(1000-K+P)
자릿수 더하기
N = input()
sum = 0
for i in N:
    sum += int(i)
print(sum)

최대수 구하기
T = int(input())

for i in range(1,T+1):
    data = list(map(int,input().split()))
    data.sort()

    print(f'#{i} {data[len(data)-1]}')

큰놈 , 작은놈 , 같은놈
T = int(input())

for i in range(1,T):
    a , b = map(int,input().split())
    if a>b:
        print(f'#{i} >')
    elif a==b:
        print(f'#{i} =')
    else:
        print(f'#{i} <')