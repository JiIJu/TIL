def enq(n):
    global last
    last += 1
    heap[last] = n
    # 만약 새로 추가된 원소가 부모 노드보다 더 커버린 경우 자리를 바꿔줘야 한다.
    c = last # 새로 추가된 노드 ( 자식노드 )
    p = c//2 # 부모노드

    while p and heap[p]>heap[c]: # 부모노드가 있고 자식이 부모보다 작으면
        heap[p],heap[c] = heap[c] , heap[p]
        # 혹시 바꾸고 난 다음에도 또 바꿔야 할 수 있으니까
        # 부모와 자식을 바꿔준다.
        c = p
        p = c//2


heap = [0] * 100
last = 0 # 마지막 원소의 위치 (삽입할 원소가 올 위치)