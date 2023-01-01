# 방번호 1475

data = input()
cnt = 0
num = [0]*10

for i in data:
    if i=='9':
        num[6]+=1
    else:
        num[int(i)]+=1
if num[6]%2:
    num[6]=num[6]//2+1
else:
    num[6]=num[6]//2
print(max(num))