def selection_sort(arr):
    # 재귀적 정의
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
    # 기저 조건
            selection_sort(arr)
    return arr
    # 작은 문제의 결과를 통해 큰 문제를 해결하는 유도 조건
arr = [2 , 1, 3 , 4 , 5]
print(selection_sort(arr))
# print(arr)