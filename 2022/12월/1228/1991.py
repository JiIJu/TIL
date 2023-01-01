# 1991 트리순회

def pre(root):
    if root!='.':
        print(root,end='')
        pre(data[root][0])
        pre(data[root][1])

def inorder(root):
    if root!='.':
        inorder(data[root][0])
        print(root,end='')
        inorder(data[root][1])

def last(root):
    if root!='.':
        last(data[root][0])
        last(data[root][1])
        print(root,end='')

N = int(input())
data = {}

for i in range(N):
    root,left,right = input().split()
    data[root] = [left,right]

pre('A')
print()
inorder('A')
print()
last('A')