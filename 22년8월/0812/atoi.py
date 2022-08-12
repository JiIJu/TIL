# def atoi(a):
#     s = []
#     b=0
#     while a>1:
#
#         b = a%10
#         a = a // 10
#         s += [b]
#         if a<10:
#             s+=[a]
#     c = ''
#     for i in range(len(s)):
#         c += f'{s[len(s)-i-1]}'
#     print(c)
# atoi(123)


def atoi1(a):
    i = 10
    s = ''
    while a>0:
        mod = a%i
        s += chr(ord('0') + mod)
        a //=10
    return s[::-1]

a=1234
print(atoi1(a))