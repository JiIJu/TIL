N = int(input())
data = []
for i in range(N):
    data.append(list(input()))
text = ''
for i in range(N):
    text += f'{data[i][0]}'
cnt = 1
result = ''
text = sorted(text)
for i in range(N-1):
    if text[i] == text[i+1]:
        cnt+=1
        if cnt ==5:
            result+=f'{text[i]}'
    else:
        cnt = 1
if result:
    print(result)
else:
    print('PREDAJA')