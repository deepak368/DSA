def reverse_arr(l, r):
    if l >= r:
        return 
    arr[l], arr[r] = arr[r], arr[l]
    reverse_arr(l+1,r-1)

arr = [6,7,3,9,2,1,10]
m = len(arr)
reverse_arr(0,m-1)
print(arr)

def rev_1arg(i):
    if i >= n/2:
        return
    arr1[i],arr1[n-i-1] = arr1[n-i-1], arr1[i]
    rev_1arg(i+1)

arr1 = [3,4,5,6,2,3,4]
n = len(arr1)
rev_1arg(0)
print(arr1)
