
# to print all the subsequence
def subsum(ind, ds, sum, k, arr, n):
    if ind == n:
        if k == sum:
            for i in range(len(ds)):
                print(ds[i], end=" ")
            print('')
        return
    ds.append(arr[ind])
    sum += arr[ind]
    subsum(ind+1, ds, sum, k, arr, n)
    sum -=arr[ind]
    ds.pop()
    subsum(ind+1, ds, sum, k, arr, n)
    


arr = [1,2,1]
n = 3
ds = []
k = 2
subsum(0, ds, 0, k, arr, n)



# if we want to print only one subsequence
def subsum1(ind, ds, sum, k, arr, n):
    if ind == n:
        if k == sum:
            for i in range(len(ds)):
                print(ds[i], end=" ")
            return True
            print('')
        return False
    ds.append(arr[ind])
    sum += arr[ind]
    if(subsum1(ind+1, ds, sum, k, arr, n) == True):
        return True
    sum -=arr[ind]
    ds.pop()
    if(subsum1(ind+1, ds, sum, k, arr, n) == True):
        return True
    return False

subsum1(0, ds, 0, k, arr, n)


# if we want to print the count of subsequence 
def countsub(ind, sum, k, arr, n):
    if ind == n:
        if sum == k:
            return 1
        return 0
    sum += arr[ind]
    l = countsub(ind+1, sum, k, arr, n)
    sum -= arr[ind]
    r = countsub(ind+1, sum, k, arr, n)
    return(l+r)
print('')
print(countsub(0,0, k, arr, n))
