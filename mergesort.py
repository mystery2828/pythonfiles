def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = int(len(arr)/2)
    leftarr,rightarr = mergesort(arr[:mid]),mergesort(arr[mid:])
    return merge(leftarr,rightarr)

def merge(leftarr,rightarr):

    left_pointer = right_pointer = 0 
    res = []
    count = 0
    
    while left_pointer<len(leftarr) and right_pointer<len(rightarr):
        # print(leftarr,rightarr)
        # print('leftpointer: {},rightpointer: {}'.format(left_pointer,right_pointer))
        if leftarr[left_pointer] < rightarr[right_pointer]:
            res.append(leftarr[left_pointer])
            left_pointer+=1
    
        else:
            res.append(rightarr[right_pointer])
            right_pointer+=1
            count+=1
    
    res.extend(leftarr[left_pointer:])
    res.extend(rightarr[right_pointer:])
    # print('result is : ',res)
    # print('\n')
    return count
   

arr = list(map(int,input().split(' ')))
print(mergesort(arr))
