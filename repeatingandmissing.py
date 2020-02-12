for _ in range(int(input())):
    n=int(input())
    ar=(int(i) for i in input().split())
    t=[0]*(n+1)
    for i in ar:
        if(t[i]>=0):
            t[i]=-1
        else:
            r=i
    for i in range(1,n+1):
        if(t[i]==0):
            m=i
            break
    print(r,m)