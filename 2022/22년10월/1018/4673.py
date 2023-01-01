# 4673 셀프넘버

def self_num(n):
    global data
    if n>10000:
        return
    a = str(n)
    new_n = int(a)
    for i in a:
        new_n += int(i)
    if new_n<10001:
        data[new_n] = 1
        self_num(new_n)
data = [0] * 10001
data[0] = 1

for i in range(1,10001):
    self_num(i)
for i in range(10001):
    if data[i]==0:
        print(i)
