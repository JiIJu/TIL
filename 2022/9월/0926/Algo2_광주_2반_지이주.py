def inorder(n): #전순회
    if n:
        data1.append(data[n])
        inorder(road1[n])
        inorder(road2[n])
def preorder(n): #중위순회
    if n:
        preorder(road1[n])
        data2.append(data[n])
        preorder(road2[n])

def order(n): # 후위순
    if n:
        order(road1[n])
        order(road2[n])
        data3.append(data[n])

def preorder2(n): #최종값을 중위순회할 함
    if n:
        preorder2(road3[n])
        result.append(ans[n])
        preorder2(road4[n])



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [0]*(2*N)
    data1 = [0] # 전위순회 값을 넣을 리스트
    data2 = [0] # 중위순회값을 넣을 리스트
    data3 = [0] # 후위순회 값을 넣을 리스트

    # 전위순회 값과 N에따른 값을 리스트에 넣는다
    for i in range(1,N+1):
        data[i] = i

    # 각노드에서 갈수있는 경로를 구한
    road1 = [0]*(2*20)
    road2 = [0]*(2*20)
    for i in range(1,N):
        road1[i] = data[2*i]
        road2[i] = data[2*i+1]
    inorder(1)
    preorder(1)
    order(1)
    # 전위 , 중위 , 후위순회중 가장 큰값을 넣을 리스
    ans = [0]
    print(data1,data2,data3)
    # 세 순회중 가장 큰값을 ans에 넣는다.
    for i in range(1,len(data2)):
        ans.append(max(data1[i],data2[i],data3[i]))
    for i in range(N+1):
        ans.append(0)
    # ans에서 노드의 길을 찾는다.
    print(ans)
    road3 = [0] * (2 * 20)
    road4 = [0] * (2 * 20)
    for i in range(1, N):
        road3[i] = ans[2*i]
        road4[i] = ans[2*i + 1]
    # 최종값을 넣을 리스트
    result = [0]
    # 중위순회
    # for i in range(1,N+1):
    #     preorder2(i)
    preorder2(1)
    print(f'#{tc}',end=' ')
    for i in range(1,N+1):
        print(result[i],end=' ')
