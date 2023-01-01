# 15965 K번째 소수

K = int(input())

num = [True]*7500001
num[0],num[1]=False,False
ans = []
for i in range(2,7500001):
    if num[i]:
        ans.append(i)
        for j in range(2*i,7500001,i):
            num[j] = False
print(ans[K-1])
