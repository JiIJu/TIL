N = input()
n = int(N)

ans = []
while n>1:
    n-=1
    b = str(n)
    a = int(n)
    for i in range(len(b)):
        a += int(b[i])

    if a==int(N):
        ans.append(n)

print(min(ans))
