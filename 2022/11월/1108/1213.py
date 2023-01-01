# 1213 팰린드롬 만들기

name = list(input())

name.sort()
alpa = {}
for i in name:
    if i in alpa:
        alpa[i]+=1
    else:
        alpa[i]=1
cnt = 0
palendrom = ''
odd = ''
for key,val in alpa.items():

    if val%2==1:
        odd+=key

if len(odd)>1:
    print("I'm Sorry Hansoo")
else:
    new = sorted(alpa.items())
    for i in new:
        print(i[0]*(int(i[1])//2),end='')
    print(odd,end='')
    for i in new[::-1]:
        print(i[0]*(int(i[1])//2),end='')