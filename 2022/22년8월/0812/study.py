# def strlen(a):
#     count = 0
#     count_len = 0
#     for i in a:
#         count_len+=1
#     n = 0
#     while n<count_len :
#         for i in a:
#             if i == '\0':
#                 pass
#             else:
#                 count+=1
#             n+=1
#     return count
# print(strlen(['a','b','c','\0']))

# def strlen1(a):
#     count = 0
#
#     while True:
#         for i in a:
#             if i=='\0':
#                 pass
#             else:
#                 count+=1
#         break
#     return count
# print(strlen1(['a','b','c','\0']))

s = 'Reverse this strings'
#1. 역순으로 쌓기
# def my_reverse(a):
#     i = 0
#
#     for b in a:
#         i+=1
#     c = ''
#     for b in range(i):
#         c += a[i-b-1]
#
#         return c

#2. swap
# def my_reverse2(a):
#     n = len(a)
#     a_list = list(a)
#
#     for i in range(n//2):
#         a_list(i) , a_list(n-i-1) = a_list(i),a_list(n-i-1)
#
#     new_a = ''
#     for c in a_list:
#         new_a += c
#     return new_a
#
#     return str(a_list)
#
# print(my_reverse2(s))

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# print(s1==s2)
# print(s1 is s2)
# print(s1 == s4 , s1 is s4)
#
# print(s1 == s5 , s1 is s5)

# s1 = 'BAC'
# s2 = 'AAA'
# def my_strcmp(str1,str2):
#     i = 0
#     a = len(str1)
#     b = len(str2)
#     if a>b:
#         a=b
#     else:
#         pass
#
#     for i in range(a):
#         if str1 == str2:
#             return 0
#             break
#         elif ord(str1[i]) == ord(str2[i]):
#             pass
#         elif ord(str1[i])<ord(str2[i]):
#             return -1
#             break
#         elif ord(str1[i])<ord(str2[i]):
#             return 1
#             break
# print(my_strcmp('123','1234'))
#
# #문자열에 부등호 사용시 문자의 ASCII값을 비교
#
# def my_strcmp(s1,s2):
#     if s1<s2:
#         return -1
#     elif s1>s2:
#         return 1
#     else:
#         return 0
# print(my_strcmp('123','124'))

def atoi(a):
    s = []
    b=0
    while a>1:

        b = a%10
        a = a // 10
        s += [b]
        if a<10:
            s+=[a]
    c = ''
    for i in range(len(s)):
        c += f'{s[len(s)-i-1]}'
    print(c)
atoi(123)