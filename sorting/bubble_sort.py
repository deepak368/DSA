def bubble_sort(arr,n):
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
sort_list = bubble_sort(arr, n)
print(sort_list)