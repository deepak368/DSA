def mergesort(arr,low, heigh):
    if low >= heigh:
        return
    
    mid = (low + heigh) // 2
    mergesort(arr,low,mid)
    mergesort(arr, mid+1, heigh)
    merge(arr, low, mid, heigh)
    

def merge(arr, low, mid, heigh):
    temp = []
    left = low
    right = mid+1
    while left <= mid and right <= heigh:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1
    while left <= mid :
        temp.append(arr[left])
        left +=1
    while right <= heigh:
        temp.append(arr[right])
        right +=1
    for i in range(low, heigh+1):
        arr[i] = temp[i-low]

n= int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
mergesort(arr, 0, n-1)
print(arr)