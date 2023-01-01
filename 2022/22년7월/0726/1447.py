def de_identify(number):
    number = list(number)
    for i in range(6,len(number)):
        number[i] = '*'
    a = ''
    for i in range(len(number)):
        a+=f'{number[i]}'
    return a
print(de_identify('970103-1234567'))