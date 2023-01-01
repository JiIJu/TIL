s1 = 'BAC'
s2 = 'AAA'
def my_strcmp(str1,str2):
    i = 0
    a = len(str1)
    b = len(str2)
    if a>b:
        a=b
    else:
        pass

    for i in range(a):
        if str1 == str2:
            return 0
            break
        elif ord(str1[i]) == ord(str2[i]):
            pass
        elif ord(str1[i])<ord(str2[i]):
            return -1
            break
        elif ord(str1[i])<ord(str2[i]):
            return 1
            break
print(my_strcmp('123','1234'))

#문자열에 부등호 사용시 문자의 ASCII값을 비교

def my_strcmp(s1,s2):
    if s1<s2:
        return -1
    elif s1>s2:
        return 1
    else:
        return 0
print(my_strcmp('123','124'))