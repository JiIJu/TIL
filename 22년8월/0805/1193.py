a = int(input())

def fib(a):
    sum = 0
    for i in range(1,a+1):
        sum +=i
    return sum
data = 0
n = 0
for i in range(a):
    if fib(i)<=a:
        data = fib(i)
        n = i
S = a - data
print(f'{S}/{n-S+2}')
