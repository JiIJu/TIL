N = int(input())

# 람다에 대해 처음 사용해봄 ㄷㄷ
data = []
for i in range(N):
    data.append(input().split())
    data[i][0] = int(data[i][0])
data.sort(key=lambda a : a[0])
for i in data:
    print(*i)