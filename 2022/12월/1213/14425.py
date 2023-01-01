#14425 문자열 집합
import sys
N , M = map(int,input().split())
S = {sys.stdin.readline().rstrip() for _ in range(N)}
check = [sys.stdin.readline().rstrip() for _ in range(M)]

# check에서 S에 몇개가 포함되어있는지?
cnt=0
for i in check:
    if i in S:
        cnt+=1
print(cnt)
