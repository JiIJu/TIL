def strlen(a):
    count = 0
    count_len = 0
    for i in a:
        count_len+=1
    n = 0
    while n<count_len :
        for i in a:
            if i == '\0':
                pass
            else:
                count+=1
            n+=1
    return count
print(strlen(['a','b','c','\0']))

def strlen1(a):
    count = 0

    while True:
        for i in a:
            if i=='\0':
                pass
            else:
                count+=1
        break
    return count
print(strlen1(['a','b','c','\0']))