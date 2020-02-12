def findleader(arr,n):
    maxi = arr[n-1]
    a = []
    #a.append(maxi)
    for i in range(n-1,-1,-1):
        if arr[i]>=maxi:
            maxi = arr[i]
            a.append(arr[i])
    a.reverse()
    listToStr = ' '.join(map(str, a))
    print(listToStr)
t = int(input())

for i in range(t):
    r = int(input())
    arr = [int(i) for i in input().split()]
    n = len(arr)
    findleader(arr,n)