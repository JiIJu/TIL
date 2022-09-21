T = int(input())

for tc in range(1,T+1):
    a , b = map(int,input().split())
    # a=1 > 1
    # a = 2 > 2 4 8 6
    # a = 3 > 3 9 7 1
    # a = 4 > 4 6
    # a = 5 > 5
    # a = 6 > 6
    # a = 7 > 7 9 3 1
    # a = 8 > 8 4 2 6
    # a = 9 > 9 1
    # a = 10 > 0
    x = [[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
    # data =[]
    result = -1
    # for i in range(1,11):
    #     data.append(i)
    # for i in range(1,11):
    #     if a == data[i-1]:
    result = x[a%10][b%len(x[a%10])-1]
    if result == 0:
        result = 10
    print(result)