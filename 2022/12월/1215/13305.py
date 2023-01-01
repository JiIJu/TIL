# 13305 주유소

# 도시수 N
N = int(input())
# 도시거리
road = list(map(int,input().split()))
# 기름값
oil = list(map(int,input().split()))

ans = [0]*N

ans[1] = oil[0]*road[0]
now_oil = oil[0]
for i in range(1,N-1):
    if now_oil>oil[i]:
        now_oil = oil[i]
    ans[i+1] = ans[i] + road[i]*now_oil

print(ans[-1])