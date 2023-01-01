def f1(i,k,t):
    global cnt
    cnt +=1
    if i==k:
        s=0
        for j in range(10):
            if bit[j]:
                s+=A[j]
        if s==t:
            for j in range(10):
                if bit[j]:
                    print(A[j],end=' ')
            print()
        else:
            bit[i]=0
            f1(i+1,k,t)
            bit[i]=1
            f2(i+1,k,t,s+A[i])
        return