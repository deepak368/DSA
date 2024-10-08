def printsub(ind, ds, arr, n):
    if(ind == n):
        for i in range(len(ds)):
            print(ds[i], end =" ")
        if(len(ds) == 0):
            print('{}')
        print(' ')
        return
    ds.append(arr[ind])
    printsub(ind+1, ds, arr, n)
    ds.pop()
    printsub(ind+1, ds, arr, n)
    


arr = [3,1,2]
n = 3
ds = []
printsub(0, ds, arr, n)