# 9386 연속한 1의 개수

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     data = list(map(int,input()))
#     count = 0
#     max = 0
#     for i in range(N):
#         if data[i] == 1:
#             count +=1
#             if count>max:
#                 max = count
#         elif data[i] !=1:
#             count=0
#     print(f'#{tc} {max}')

# 14229 백만개의 정수 정렬

# data = list(map(int,input().split()))
#
# emp = [0] * 1000001
# b = [0] * 1000000
# for i in range(1000000):
#     emp[data[i]] +=1
# for i in range(1,1000001):
#     emp[i] += emp[i-1]
# for i in range(999999,-1,-1):
#     emp[data[i]] -=1
#     b[emp[data[i]]] = data[i]
# print(b[500000])

# 고대유적
# T = int(input())
#
# for tc in range(1,T+1):
#     N , M = map(int,input().split())
#     data = [list(map(int,input().split())) for _ in range(N)]
#     max = 0
#     for i in range(N):
#         count = 0
#         for j in range(M):
#             if data[i][j] == 1:
#                 count +=1
#                 if count>=max:
#                     max = count
#             elif data[i][j]==0:
#                 count=0
#
#     for i in range(M):
#         count = 0
#         for j in range(N):
#             if data[j][i] == 1:
#                 count += 1
#                 if count >= max:
#                     max = count
#             elif data[j][i] == 0:
#                 count = 0
#
#     print(f'#{tc} {max}')

# 파리퇴치3

# T = int(input())
#
# for tc in range(1,T+1):
#     N , M = map(int,input().split())
#     data = [list(map(int,input().split())) for _ in range(N)]
#
#     dx = [-1 ,1 ,0 ,0]
#     dy = [0 ,0 ,-1 ,1] #좌우 상하
#
#     da = [-1 ,-1 ,1 ,1]
#     db = [-1 ,1 ,-1 ,1] # 왼위 왼아래 오른위 오른아래
#
#     x = 0
#     y = 0
#     max = 0
#     k = 0
#     for i in range(N):
#         for j in range(N):
#            sum = data[i][j]
#            for k in range(4):
#                for l in range(1,M):
#                    if 0<=i+l*dy[k]<N and 0<=j+l*dx[k]<N:
#                         sum += data[i+l*dy[k]][j+l*dx[k]]
#                    if sum>max:
#                        max=sum
#     for i in range(N):
#         for j in range(N):
#            sum = data[i][j]
#            for k in range(4):
#                for l in range(1,M):
#                    if 0<=i+l*da[k]<N and 0<=j+l*db[k]<N:
#                        sum += data[i+l*da[k]][j+l*db[k]]
#                    if sum>max:
#                        max=sum
#
#     print(f'#{tc} {max}')

# 새로운 버스노선
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     stop = [0] * 1001
#     data = [list(map(int,input().split())) for _ in range(N)]
#
#     for i in range(N):
#         if data[i][0] == 1:
#             for j in range(data[i][1],data[i][2]+1):
#                 stop[j] +=1
#         elif data[i][0] == 2:
#             if data[i][1]%2 == 0:
#                 for j in range(data[i][1],data[i][2]):
#                     if j%2==0:
#                         stop[j]+=1
#             elif data[i][1]%2 ==1:
#                 for j in range(data[i][1],data[i][2]):
#                     if j%2==1:
#                         stop[j]+=1
#             stop[data[i][2]] +=1
#
#         elif data[i][0] == 3:
#             if data[i][1]%2 == 0:
#                 for j in range(data[i][1]+1,data[i][2]):
#                     if j%4 == 0:
#                         stop[j] +=1
#             elif data[i][1]%2 == 1:
#                 for j in range(data[i][1]+1,data[i][2]):
#                     if j%3 ==0 and j%10 !=0:
#                         stop[j] +=1
#             stop[data[i][1]] +=1
#             stop[data[i][2]] += 1
#     stop = sorted(stop)
#     print(f'#{tc} {stop[-1]}')


# 회문2

for tc in range(1, 11):
    N = int(input())
    data = [list(input()) for _ in range(100)]
    count = 0
    max = 0
    emp = []
    for i in range(100):
        for j in range(100):
            count=0
            for a in range(99, -1, -1):
                if data[i][j] == data[i][a]:
                    emp = []
                    for k in range(j,a+1):
                        emp += [data[i][k]]
                    if emp == emp[::-1]:
                        count = len(emp)
                        if max<count:
                            max=count
                    else:
                        emp = []



    for i in range(100):
        for j in range(100):
            count = 0
            for a in range(99, -1, -1):
                if data[j][i] == data[a][i]:
                    emp = []
                    for k in range(j, a + 1):
                        emp += [data[k][i]]
                    if emp == emp[::-1]:
                        count = len(emp)
                        if max < count:
                            max = count



    print(max)
