# HSAT 전광판
num = [0]*10
num[0] = (1,1,1,0,1,1,1)
num[1] = (0,0,1,0,0,1,0)
num[2] = (1,0,1,1,1,0,1)
num[3] = (1,0,1,1,0,1,1)
num[4] = (0,1,1,1,0,1,0)
num[5] = (1,1,0,1,0,1,1)
num[6] = (1,1,0,1,1,1,1)
num[7] = (1,1,1,0,0,1,0)
num[8] = (1,1,1,1,1,1,1)
num[9] = (1,1,1,1,0,1,1)
T = int(input())

for tc in range(T):
    A,B = input().split()
    A ,B= list(A),list(B)
    # A,B = A[::-1],B[::-1]
    cnt = 0
    if len(A)>len(B):
        temp = len(A)-len(B)
        for i in range(temp):
            cnt+=sum(num[int(A[0])])
            A.pop(0)
    elif len(A)<len(B):
        temp = len(B) - len(A)
        for i in range(temp):
            cnt += sum(num[int(B[0])])
            B.pop(0)

    for i in range(len(A)):
        if A[i]!=B[i]:
            for j in range(7):
                if num[int(A[i])][j] != num[int(B[i])][j]:
                    cnt+=1
    print(cnt)
    # for i in range(len(A)):

