def subSetSum(ind, sum, arr, N, sumset):
    if ind == N:
        sumset.append(sum)
        return
    subSetSum(ind+1, sum + arr[ind], arr ,N, sumset)
    subSetSum(ind+1, sum, arr, N, sumset)

arr = [3,1,2]
N = 3
sumset = []
subSetSum(0, 0, arr, N, sumset)
sumset.sort()
print(sumset)