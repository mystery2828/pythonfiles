def binarySearch(arr, l, r, x): 
    count=0
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
             r = mid-1
             l = mid+1
             count+=1
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return count

arr = [1,3,3,4,4,5,6,8,9] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(count)