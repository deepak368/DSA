def subset(ind, arr, ans, ds, n):
    ans.append(list(ds))
    for i in range(ind, n-1):
        if i != ind and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        subset(i+1, arr, ans, ds, n)
        ds.pop()



arr = [1,2,2,2,3,3]
n = len(arr)
ds = []
ans = []
subset(0, arr, ans, ds, n)
print(ans)