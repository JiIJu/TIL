#2776 암기왕

T = int(input())

for tc in range(T):
    N = int(input())
    note1 = list(map(int,input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    data1 = {}
    data2 = {}
    for i in note1:
        if i in data1:
            data1[i]+=1
        else:
            data1[i] = 1
    for i in note2:
        if i in data1:
            print(1)
        else:
            print(0)