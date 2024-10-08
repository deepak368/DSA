def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <=high - 1:
            i+= 1
        while arr[j] >pivot and j >=low:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

n = int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
quick_sort(arr,0,n-1)
print(arr)