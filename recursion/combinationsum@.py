def combination_sum(ind,arr,target,ans,ds):
    if target == 0:
        ans.append(list(ds))
        return
    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        ds.append(arr[i])
        combination_sum(i+1,arr,target - arr[i],ans,ds)
        ds.pop()

arr = [10,1,2,7,6,1,5]
arr.sort()
ds = []
ans = []
target = 8
combination_sum(0, arr, target, ans, ds)
print(ans)