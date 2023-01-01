#분수찾기 1193

N = int(input())
a = 0
max_num = 0

while max_num<N:
    a+=1
    max_num+=a
gap = max_num-N

if a%2:
    top = a-gap
    bottom = 1+gap
else:
    top = 1+gap
    bottom = a-gap

print(f'{bottom}/{top}')