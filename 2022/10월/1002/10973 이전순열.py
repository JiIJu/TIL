def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in arr]
        return result
    for i in range(len(arr)):
        elem = arr[i]
        p = permutation(arr[:i]+arr[i+1:], n-1)
        for rest in p:
            result.append([elem]+rest)
    return result

n = int(input())

data = list(map(int,input().split()))
num = []
for i in range(1,n+1):
    num.append(i)
visited = [0 for _ in range(len(l))]
answer = []




permutation(num,n)
print(answer)