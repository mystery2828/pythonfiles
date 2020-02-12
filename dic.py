#code
for i in range(int(input())):
    n = int(input())
    s = (int(i) for i in input().split())
    t = [0]*(n)
    p=0
    j=n-2
    l=n-1
    for i in s:
        if p>=(n//2):
            if n%2 == 0:
                
                t[j]=i
                j-=2
            else:
                
                t[l]=i
                l-=2

        else:
            k = (p*2)+1
            p+=1
            t[k] = i
        
    for ele in t:
        print(ele,end=' ')
    print('')