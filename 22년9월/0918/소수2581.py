M = int(input())
N = int(input())


data = []
if M == 1:
    M+=1
for i in range(M,N+1):
    ans = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            ans = 1
            break
    if ans ==0:
        data.append(i)

# if M==N:
#     data = []
#     for i in range(2,M//2):
#         ans = 0
#         if M%i == 0:
#             ans = 1
#             break
#     if ans ==0:
#         data.append(M)
# print(data)
if len(data)==0:
    print(-1)
else:
    print(sum(data))
    print(min(data))