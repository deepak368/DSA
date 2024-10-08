def insertion_recurtion(arr, n, i):
    if i == n :
        return
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j-=1
    insertion_recurtion(arr, n, i+1)

n = int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
sort_list = insertion_recurtion(arr, n, 0)
for i in range(n):
    print(arr[i])