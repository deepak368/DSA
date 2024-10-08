def selection_sort(arr, n):
    for i in range (n-1):
        min = i
        for j in range(i,n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

n = int(input("enter the number of element: "))
arr = []
for i in range(n):
    element = int(input(f"enter the {i+1} element: "))
    arr.append(element)
sort_list = selection_sort(arr, n)
print(sort_list)