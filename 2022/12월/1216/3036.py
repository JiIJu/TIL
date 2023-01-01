#3036 링

def find(a,b):
    while b>0:
        a,b = b,a%b
    return a


N = int(input())
data = list(map(int,input().split()))
num = data[0]
for i in range(1,N):
    ans = find(num,data[i])
    print(num//ans,end='')
    print('/',end='')
    print(data[i]//ans)