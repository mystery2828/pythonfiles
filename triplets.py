def trip(arr):
    # Take a dictionary(hash-map)
    k = {}
    # A list to check for duplicates
    ssd = []
    # Set initial count to zero
    count = 0
    found = False
    i = 0
    while i < len(arr):
        # Add all the values as key value pairs to the dictionary
        if arr[i] not in k:
            k[arr[i]] = 1

        i += 1
    j = 0
    while j < len(arr) - 1:
        q = j + 1
        while q < len(arr):
            # Check for the sum and duplicate
            if arr[j] + arr[q] in k and [arr[j], arr[q]] not in ssd:
                count += 1
                found = True
                ssd.append([arr[j], arr[q]])
            q += 1
        j += 1
    if found:
        print(count)
    if not found:
        print('-1')


# Driver code for the above code
t = int(input())
for i in range(t):
    n = input()
    s = list(map(int, input().split()))
    trip(s)