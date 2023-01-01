# 11057 오르막 수

def fact(n):
    if n<2:
        return 1
    else:
        return fact(n-1)*n

N = int(input())

print((fact(9+N)//(fact(N)*fact(9))%10007))