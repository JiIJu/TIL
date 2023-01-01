#1072 게임
import math
X,Y = map(int,input().split())

Z = math.trunc((100*Y/X))
d = (100*Y/X)-Z
tmp = 0
cnt=0
if Z!=99:
    cnt = (((Z+1)*X-100*Y)/(99-Z))
    tmp=1

if tmp==0 or Z >=99:
    print(-1)
else:
    print(math.ceil(cnt))