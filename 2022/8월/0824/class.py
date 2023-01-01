# 큐 생성
n = 5
q = [0] * n

front = rear = -1

def enQueue(item): # 큐에 원소를 삽입하는 연산 rear 1씩 증가
    global rear
    # 만약 큐가 꽉 차있다면 삽입불가 처리
    if isFull():
        print('FULL!!')
    # 그게 아니면 rear를 1 증가시키고 큐에 원소삽입
    else:
        rear +=1
        q[rear] = item
def deQueue(): #큐에 원소를 하나 빼내고 삭제하는 연산 front 1씩 증가
    global front
    # 큐가 만약 비어있다면 삭제 불가 처리
    if isEmpty():
        print('EMPTY!!')
    #그게 아니면 front를 1증가시키고 큐의 원소 하나 삭제
    else:
        front +=1
        return q[front]


def isFull(): #큐가 꽉 찼는지 확인해주는 함수
    return rear == len(q)-1

def isEmpty(): #큐가 비어있는지 확인해주는 함수 (큐 안에 들어있는 원소갯수가 0인지)
    return front == rear

for i in range(5):
    enQueue(i)

print(isFull())
enQueue(5)

for i in range(5):
    print(deQueue())

print(isEmpty())
deQueue()