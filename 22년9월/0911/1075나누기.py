N = int(input())
F = int(input())

# for i in range(100):
n = N%100
N = N-n
for i in range(100):
    if (N+i)%F==0:
        N = N+i
        break
if N%100<10:
    print(f'0{N%100}')
else:
    print(N%100)