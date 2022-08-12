s = 'Reverse this strings'
# 1. 역순으로 쌓기
def my_reverse(a):
    i = 0

    for b in a:
        i+=1
    c = ''
    for b in range(i):
        c += a[i-b-1]

        return c

# 2. swap
def my_reverse2(a):
    n = len(a)
    a_list = list(a)

    for i in range(n//2):
        a_list(i) , a_list(n-i-1) = a_list(i),a_list(n-i-1)

    new_a = ''
    for c in a_list:
        new_a += c
    return new_a

    return str(a_list)

print(my_reverse2(s))

s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1==s2)
print(s1 is s2)
print(s1 == s4 , s1 is s4)

print(s1 == s5 , s1 is s5)