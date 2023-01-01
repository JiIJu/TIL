N = int(input())
cnt = 0
ans = N
new = ans
while True:
    if new<10:
        new = new*11
    else:
        a = new//10
        b = new%10
        c = (a+b)%10
        new = b*10+c
    cnt+=1
    # print(new,ans)
    if new==ans:
        break
print(cnt)