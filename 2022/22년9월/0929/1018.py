M,N = map(int,input().split())

data=[list(input()) for _ in range(M)]



a1 = ['W','B','W','B','W','B','W','B']
a2 = ['B','W','B','W','B','W','B','W']

ans1= []
ans2 = []

for i in range(4):
    ans1.append(a1)
    ans1.append(a2)
    ans2.append(a2)
    ans2.append(a1)


minv1 = 99999
minv2 = 99999

for i in range(M-7):
    for j in range(N-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            # if cnt1>=minv1 or cnt1>=minv2 or cnt2>=minv1 or cnt2>=minv2:
            #     break
            for l in range(8):

                if data[i+k][j+l] != ans1[k][l]:
                    cnt1 +=1
                if data[i+k][j+l] != ans2[k][l]:
                    cnt2 +=1
        if cnt1<minv1:
            minv1 = cnt1
        if cnt2<minv2:
            minv2 = cnt2
print(min(minv1,minv2))