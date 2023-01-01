data = [list(map(int,input().split())) for _ in range(5)]
count = 0
ans = 0
cnt = 0
result = 0
q = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if ans>=3:
                    result =count
                    break
                    break
                    break
                    break
                if q[i][j] == data[k][l]:
                    data[k][l] = -1
                    count +=1

                ans = 0
                for a in range(5):
                    for b in range(5):
                        if data[a][b] == -1:
                            cnt +=1
                    if cnt ==5:
                        ans +=1
                        cnt = 0

                    else:
                        cnt = 0

                for a in range(5):
                    for b in range(5):
                        if data[b][a] == -1:
                            cnt +=1
                    if cnt ==5:
                        ans +=1
                        cnt = 0
                    else:
                        cnt = 0
                for a in range(5):
                    if data[a][a]==-1:
                        cnt+=1
                if cnt ==5:
                    ans+=1
                    cnt = 0
                else:
                    cnt =0
                for a in range(5):
                    if data[a][4-a]==-1:
                        cnt+=1
                if cnt==5:
                    ans+=1
                    cnt = 0
                else:
                    cnt=0


print(result)