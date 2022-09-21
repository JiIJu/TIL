text = list(input())
cnt = 1
if text[0]==' ':
    cnt-=1
if text[-1]==' ':
    cnt-=1
for i in range(len(text)):
    if text[i]==' ':
        cnt +=1
print(cnt)