# def step(n,a,s):
#     global maxv
#     # print(s)
#     if n==N-1:
#         maxv = max(s[n],maxv)
#         return
#
#     if a==0 and n+2<N:
#         if s[n+2]<data[n]+data[n+2]:
#             s[n+2] = data[n]  + data[n+2]
#             step(n+2,1,s)
#             s[n+2] -= (data[n]  + data[n+2])
#     if a==0 and n+1<N:
#         if s[n+1]<data[n]+data[n+1]:
#             s[n+1] = data[n] + data[n+1]
#             step(n+1,1,s)
#             s[n+1] -= (data[n] + data[n+1])
#     if a==1 and n+1<N:
#         if s[n+1]<s[n]+data[n+1]:
#             s[n+1] = s[n] + data[n+1]
#             step(n+1,2,s)
#             s[n+1] -= (s[n] + data[n+1])
#     if a==1 and n+2<N:
#         if s[n+2]<s[n]+data[n+2]:
#             s[n+2] = s[n] + data[n+2]
#             step(n+2,1,s)
#             s[n+2] -= (s[n]+data[n+1])
#     if a==2 and n+2<N:
#         if s[n+2]<s[n]+data[n+2]:
#             s[n+2] = s[n] + data[n+2]
#             step(n+2,1,s)
#             s[n+2] -= (s[n]+data[n+2])

N = int(input())
data = [0]*301

for i in range(N):
    data[i]=(int(input()))
s= [0]*(301)
n=0

s[0] = data[0]
s[1] = data[0]+data[1]
s[2] = max(data[0]+data[2],data[1]+data[2])
for i in range(3,N):
    s[i] = max(s[i-3]+data[i-1]+data[i],s[i-2]+data[i])
print(s[N-1])