def inorder(n):
    global tree , N
    global count
    if (N) >= (n * 2):
        inorder(n * 2)
    tree[n] = count
    count += 1
    if (N) >= (n * 2) + 1:
        inorder(n * 2 + 1)

number_of_test = int(input())

for test in range(number_of_test):
    N = int(input())
    tree = [0] * (N + 1)
    count = 1

    inorder(1)
    print(tree)
    print(f"#{test + 1} {tree[1]} {tree[(N // 2)]}")