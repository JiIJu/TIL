# 2503 숫자야구
from itertools import permutations
N = int(input())

check = list(permutations([1,2,3,4,5,6,7,8,9],3))
ans = 0
for i in range(N):
    num , strike , ball = map(int,input().split())
    num = str(num)
    remove_cnt = 0
    for j in range(len(check)):
        s_num , b_num = 0,0
        j-=remove_cnt
        for k in range(3):
            if int(num[k]) == check[j][k]:
                s_num+=1
            elif int(num[k]) in check[j]:
                b_num+=1
        if s_num != strike or b_num != ball:
            check.remove(check[j])
            remove_cnt +=1

print(len(check))