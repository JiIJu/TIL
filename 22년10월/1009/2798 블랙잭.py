# def comb(a):
#     global max_v
#     for i in range(1<<n):
#         res = []
#         for j in range(n):
#             if i & (1<<j):
#                 res.append(a[j])
#                 if len(res)==3:
#                     break
#         if len(res)==3:
#             if sum(res)<m:
#                 max_v = max(max_v,sum(res))

n , m = map(int,input().split())
c = []
num = list(map(int,input().split()))
max_v = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = num[i] + num[j] + num[k]
            if a<=m and a>max_v:
                max_v = a

print(max_v)