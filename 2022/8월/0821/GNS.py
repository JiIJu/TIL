T = int(input())

for tc in range(1,T+1):
    t , N = input().split()
    N = int(N)

    data = list(input().split())
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count = [0]*10
    for i in range(N):
        for j in range(10):
            if data[i] == num[j]:
                count[j] +=1
                break
    a = ''
    for i in range(10):
        a += (num[i]+' ')*count[i]
    print(t)
    print(a)
