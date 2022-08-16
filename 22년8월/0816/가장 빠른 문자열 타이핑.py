T = int(input())

for tc in range(1,T+1):
    A,B = input().split()
    a = len(A)
    b = len(B)
    count =0
    i,j = 0,0
    while i<a and j<b:
        if A[i] != B[j]:
            i = i-j
            j = -1
        i +=1
        j +=1
        if j == b:
            count +=1
            j = 0
    print(f'#{tc} {a-b*count+count}')