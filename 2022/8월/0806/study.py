#1009
import sys
T = int(sys.stdin.readline())

for i in range(T):
    a , b = map(int,sys.stdin.readline().split())
    c = a**b % 10
    print(c)