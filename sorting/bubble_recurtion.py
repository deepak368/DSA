def bubble_recurtion(arr,n):
    if n == 1:
        return
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    bubble_recurtion(arr,n-1)

n = int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
sort_list = bubble_recurtion(arr, n)
for i in range(n):
    print(arr[i],end=" ")