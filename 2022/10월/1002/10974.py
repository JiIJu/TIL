def dfs():
    if n == len(data):
        print(*data)
        return

    for i in range(1,n+1):
        if i not in data:
            data.append(i)
            dfs()
            data.remove(i)


n = int(input())
data = []
dfs()