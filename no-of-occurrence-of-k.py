def first(arr,l,r,k,n):
    if l<=r:
        mid = (l+r)//2
        if (arr[mid] == k and (mid == 0 or k > arr[mid-1])):
            return mid  
        elif (k>arr[mid]):
            return first(arr,mid+1,n-1,k,n)
        else:
            return first(arr,0,mid-1,k,n)
    return -1
def second(arr,l,r,k,n):
    
    if l<=r:
        mid = (l+r)//2
        if (arr[mid] == k and (mid == n-1 or k < arr[mid+1])):
            return mid  
        elif (k>arr[mid]):
            return second(arr,mid+1,n-1,k,n)
        elif (k<arr[mid]):
            return second(arr,l,mid-1,k,n)
    return -1


def search(arr,left,right,key,n):
    modlu = first(arr,left,right,key,n)
    if modlu == -1:
        return -1
    eradu = second(arr,modlu,right,key,n)
    return (eradu-modlu+1)



if __name__ == "__main__":   
    n = 9
    arr = [1,3,3,4,4,5,6,8,9]
    key = 7
    left = 0
    right = n-1
    count = search(arr,left,right,key,n)
    print(count)