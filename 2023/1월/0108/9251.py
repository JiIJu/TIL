# 9251 LCS

a = list(input())
b = list(input())
n,m = len(a),len(b)

check = [0]*m

for i in range(n):
    cnt = 0
    for j in range(m):
        if cnt<check[j]:
            cnt = check[j]
        elif a[i]==b[j]:
            check[j] = cnt+1
        print(check)
print(max(check))