def combinationSum(ind, arr, target, ans, ds):
    if ind == len(arr):
        if target == 0:
            ans.append(list(ds))
        return 
    if arr[ind] <= target:
        ds.append(arr[ind])
        combinationSum(ind, arr, target - arr[ind], ans, ds)
        ds.pop()
    combinationSum(ind+1, arr, target,ans, ds)
    return ans


arr = [2,3,5]
target = 8
ans = []
ds = []
print(combinationSum(0, arr,target,ans, ds))
