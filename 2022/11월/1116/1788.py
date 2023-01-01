# 1788 피보나치수의 확장

n = int(input())
a = abs(n)
data = [0] * (1000001)
# data = [0] * 201
# a = 100
data[1] = 1
data[2]=1

# if n>=0:
for i in range(3,a+1):
    data[i] = (data[i-1] + data[i-2])%1000000000
if n>0:
    print(1)

elif n==0:
    print(0)

else:
    if a%2:
        print(1)
    else:
        print(-1)
print(data[a])

#     print(abs(data[a+n])%10000000000)
# print(data)
