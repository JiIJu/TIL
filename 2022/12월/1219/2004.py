# 2004 조합 0의 개수

def count_two(n):
    cnt=0
    while n!=0:
        n=n//2
        cnt+=n
    return cnt
def count_five(n):

    cnt=0
    while n!=0:
        n = n//5
        cnt+=n

    return cnt

n,m = map(int,input().split())

print(min(count_two(n)-count_two(n-m)-count_two(m),count_five(n)-count_five(m)-count_five(n-m)))