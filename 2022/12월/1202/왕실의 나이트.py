# 이코테 왕실의나이트

position = input()

col = position[0]
row = int(position[1])-1

alpa = ['a','b','c','d','e','d','f','g','h']
col_num = alpa.index(col)

step = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
cnt = 0
for i in step:
    a,b = i
    if 0<=col_num+b<8 and 0<=row+a<8:
        cnt+=1
print(cnt)