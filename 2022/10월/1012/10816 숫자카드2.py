N = int(input())
card = {}
card1 = list(map(int,input().split()))
for i in range(N):
    if card1[i] in card:
        card[card1[i]]+=1
    else:
        card[card1[i]]=1

M = int(input())
a = list(map(int,input().split()))
for i in range(M):
    if a[i] in card:
        print(card[a[i]],end=' ')
    else:
        print(0,end=' ')