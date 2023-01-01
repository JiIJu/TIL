#이코테 큰수의 법칙

# N:배열길이 M :합개수 K : 연속가능횟수
N , M , K = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
data = data[::-1]
sumV = 0
count = 0
for i in range(M):
    if count<K:
        sumV += data[0]
        count+=1
    else:
        sumV += data[1]
        count=0
print(sumV)