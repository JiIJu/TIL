# 1789 수들의합

N = int(input())
a = 0
b = 0
while True:
    a+=1
    b+=a
    if b>N:
        break
print(a-1)