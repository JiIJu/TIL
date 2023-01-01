T = int(input())
for tc in range(1,T+1):
    a , N = input().split()
    data = list(input().split())
    N = int(N)
    n = 0
    s = [0] * 10
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN", " "]
    while n<N:
        if data[n] == num[0]:
            s[0] +=1
        elif data[n] == num[1]:
            s[1] +=1
        elif data[n] == num[2]:
            s[2] +=1
        elif data[n] == num[3]:
            s[3] +=1
        elif data[n] == num[4]:
            s[4] +=1
        elif data[n] == num[5]:
            s[5] +=1
        elif data[n] == num[6]:
            s[6] +=1
        elif data[n] == num[7]:
            s[7] +=1
        elif data[n] == num[8]:
            s[8] +=1
        elif data[n] == num[9]:
            s[9] +=1
        n+=1
    print(a)

    for i in range(10):
        print((num[i] + num[10]) * s[i])