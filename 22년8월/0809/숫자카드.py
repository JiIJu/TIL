T = int(input())

for a in range(1,T+1):
    N = int(input())
    ai = input()
    data = [0]*10
    for i in range(10):
        for j in range(N):
            if i == int(ai[j]):
                data[i] += 1
    max=0
    idx=0
    for i in range(10):
        if data[i]>=max:
            max=data[i]
            idx=i
    for i in range(10):
        for j in range(10-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    print(f'#{a} {idx} {max}')