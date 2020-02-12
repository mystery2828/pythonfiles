def quicksort(arr):
    if len(arr)>=1:
        pivot = arr.pop()
    else:
        return arr
    items_greater = []
    items_lesser = []
    for ele in arr:
        if ele>=pivot:
            items_greater.append(ele)
        else:
            items_lesser.append(ele)
        # print('items greater: {}, items lesser: {}, pivot: {}'.format(items_greater,items_lesser,pivot))
        # print('\n')
    
    return quicksort(items_lesser) + [pivot] + quicksort(items_greater)


print(quicksort([2,6,4,9,8,7,12,10]))