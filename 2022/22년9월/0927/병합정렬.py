def merge_sord(A):
    global cnt
    if len(A) == 1:
        return A
    middle = len(A)//2
    left = []
    right = []

    for i in range(middle):
        left.append(A[i])
    for i in range(middle,len(A)):
        right.append(A[i])

    left = merge_sord(left)
    right = merge_sord(right)
    print(left , right)
    if left[-1]>right[-1]:
        cnt+=1
    return merge(left , right)

def merge(left,right):
    global cnt
    result = []
    l , r = 0,0

    while l<len(left) or r<len(right):
        if l<len(left) and len(right)>r:
            if left[l] <= right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1

        elif len(left)>l:
            result.append(left[l])
            l+=1

        elif len(right)>r:
            result.append(right[r])
            r+=1


    return result

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    cnt=0
    ans = merge_sord(A)
    print(f'#{tc} {ans[N//2]} {cnt}')