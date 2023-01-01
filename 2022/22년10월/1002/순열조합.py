def comb(n):
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                print(arr[j],end=' ')
        print()


def perm(n, r, p):
    if r == 0:
        print(p)
    else:
        for i in arr:
            if p.count(i) == 0:
                p.append(i)
                perm(n, r-1, p)
                p.remove(i)

arr =[1,2,3,4,5]

# perm(3,2,[])













def perm1(n,r,p):
    if r==0:
        print(p)
    else:
        for i in arr:
            p.append(i)
            perm(n,r-1,p)
            p.remove(i)

perm1(5,2,[])