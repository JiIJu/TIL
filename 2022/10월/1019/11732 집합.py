import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    data = sys.stdin.readline().split()

    if len(data)==1:
        if data[0] == 'all':
            S = set([i for i in range(1,21)])
        elif data[0] == 'empty':
            S = set()
    else:
        data[1] = int(data[1])
        if data[0] == 'add':
            S.add(data[1])
        elif data[0] == 'remove':
            if data[1] in S:
                S.discard(data[1])
        elif data[0] == 'check':
            if data[1] in S:
                print(1)
            else:
                print(0)
        elif data[0] == 'toggle':
            if data[1] in S:
                S.discard(data[1])
            else:
                S.add(data[1])

