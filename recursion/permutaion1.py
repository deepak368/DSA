def permutaion1(arr, ds, freq, ans):
    if len(ds) == len(arr):
        ans.append(list(ds))
        return
    for i in range(len(arr)):
        if not freq[i]:
            ds.append(arr[i])
            freq[i] = 1
            permutaion1(arr, ds, freq, ans)
            freq[i] = 0
            ds.pop()
            

arr = [1, 2, 3]
freq = [0] * len(arr)
ans = []
ds = []
permutaion1(arr, ds, freq, ans)
print(ans)
